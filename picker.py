from mathutils import Vector

from . fun import load_image_from_path
from . ui_item import UIItem
from . picker_button import PickerButton
from . gr_rect import GrRect
from . gr_image import GrImage


class Picker(UIItem):
    def __init__(self, context: 'Context', image_path: str = ''):
        self.color = (0.05, 0.05, 0.05, .75) # Background Color.
        self.image_path = image_path
        self.image = None
        self.texture = None

        self.buttons = []

        self.update_armature(context)

        self.image = load_image_from_path(self.image_path)
        size = self.image.size if self.image else (256, 256)

        self.margins = Vector((10, 10, 10, 10))

        super().__init__((50, 50), size)

    def init_graphics(self):
        self.graphics_panel = GrRect(self)
        self.graphics_image = GrImage(self)

    def update_armature(self, context):
        act_obj = context.active_object
        self.arm_obj = act_obj if act_obj.type == 'ARMATURE' else None

    def button(self, position: tuple, bone: 'Bone', color: tuple = (0, .6, .9, 1.0)):
        if not bone:
            return
        button = PickerButton(self, bone, color)
        button.pos = position
        self.buttons.append(button)

    def on_event(self, event: 'Event', mouse: Vector):
        # Quick shortcut to create a button from active bone.
        if event.ctrl and event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.button(tuple(mouse), self.arm_obj.data.bones.active)
            return True

        # Checks if there is some event over some picker button.
        for button in self.buttons:
            if button._on_event(event, mouse):
                return True
        
        # If we click in the background return True so that event
        # doesn't pass to viewport and cause deselecting bones.
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            return True

    def draw(self):
        self.graphics_panel.draw()
        self.graphics_image.draw()

        for button in self.buttons:
            button.draw()
