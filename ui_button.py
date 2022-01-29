from . ui_item import UIItem
from . gr_button import GrButton
from . ui_ext_clickable import Clickable


class UIButton(UIItem, Clickable):
    name = 'UI Button'

    def __init__(self, label: str, color: tuple = (0, .6, .9, 1), on_click_callback: callable = None):
        self.label = label
        self.color = color

        self.on_click_callback = on_click_callback

        super().__init__()

    def init_graphics(self):
        self.graphics = GrButton(self)

    def on_leftmouse_press(self, event: 'Event', mouse: 'Vector'):
        if self.on_click_callback:
            self.on_click_callback()
