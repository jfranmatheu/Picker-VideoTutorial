from bpy.types import Operator, SpaceView3D
from bpy.props import StringProperty
from mathutils import Vector

from . picker import Picker


class PK_OT_picker(Operator):
    bl_idname = "pk.picker"
    bl_label = "Picker"
    bl_description = "A cool picker interface!"

    filepath: StringProperty(subtype="FILE_PATH", name="Image Path")

    @classmethod
    def poll(cls, context):
        return context.mode == 'POSE'

    @staticmethod
    def get_mouse_pos(event: 'Event'):
        return Vector((event.mouse_region_x, event.mouse_region_y))
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        self.picker = Picker(context, self.filepath)

        # Create the draw handler.
        self._draw_handler = SpaceView3D.draw_handler_add(self.draw_callback, (context,), 'WINDOW', 'POST_PIXEL')
        context.area.tag_redraw()
        self.ctx_area = context.area

        # Create and run modal operation.
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        # Exit condition.
        if event.type == 'ESC' and event.value == 'PRESS':
            self.finish(context)
            return {'FINISHED'}

        context.region.tag_redraw()
        # Pass events through Picker so that it can handle those events.
        if self.picker._on_event(event, PK_OT_picker.get_mouse_pos(event)):
            return {'RUNNING_MODAL'}

        return {'PASS_THROUGH'}

    def draw_callback(self, context):
        # It is being drawn in another editor!
        if context.area != self.ctx_area:
            return

        self.picker.draw()

    def finish(self, context):
        context.area.tag_redraw()
        SpaceView3D.draw_handler_remove(self._draw_handler, 'WINDOW')
