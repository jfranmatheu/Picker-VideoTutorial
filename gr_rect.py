from . ui_graphics import UIGraphics
from . gpu_shaders import shader_2d_unif_color, batch_for_shader


def vertices_rectangle(x, y, w, h):
    return (
        (x, y),   (x+w, y),
        (x, y+h), (x+w, y+h))

indices_rectangle = (
    (0, 1, 2), (2, 1, 3))


class GrRect(UIGraphics):
    def __init__(self, ui_item: 'UIItem'):
        super().__init__(ui_item, shader_2d_unif_color)

    # Method to overwrite!
    def init_batch(self):
        self.update_batch()

    # Method to overwrite!
    def update_shader(self):
        self.shader.bind()
        self.shader.uniform_float("color", self.ui_item.color)

    # Method to overwrite!
    def update_batch(self):
        self.batch = batch_for_shader(self.shader, 'TRIS', {"pos": vertices_rectangle(*self.ui_item.pos, *self.ui_item.size)}, indices=indices_rectangle)
