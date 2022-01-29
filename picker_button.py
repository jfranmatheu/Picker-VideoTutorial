import bpy

from . ui_button import UIButton


class PickerButton(UIButton):
    name = 'Picker Button'

    def __init__(self, picker: 'Picker', bone: 'Bone', color: tuple = (0, .6, .9, 1)):
        self.picker = picker
        self.bone = bone
        self.bone_hash = hash(bone)
        
        super().__init__(bone.name, color)

    def on_leftmouse_press(self, event: 'Event', mouse: 'Vector'):
        print("Clicked picker button!", self.label)
        if hash(self.bone) != self.bone_hash:
            arm_bones = self.picker.arm_obj.data.bones
            self.bone = arm_bones.get(self.label, None)

        if not self.bone:
            return

        if not event.shift:
            bpy.ops.pose.select_all(action='DESELECT')

        self.bone.select = True
        arm_bones.active = self.bone

