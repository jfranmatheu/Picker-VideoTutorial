from gpu.texture import from_image as gpu_texture_from_image

from . ui_graphics import UIGraphics
from . gpu_shaders import batch_for_shader, shader_2d_image


def vertices_image(x, y, w, h):
    return (
        (x, y),     (x+w, y),
        (x+w, y+h), (x, y+h))


class GrImage(UIGraphics):
    def __init__(self, ui_item: 'UIItem'):
        """ IMPORTANT! Pass a UIItem that actually has a texture image. """
        super().__init__(ui_item, shader_2d_image)

        self.texture = gpu_texture_from_image(self.ui_item.image) if self.ui_item.image else None
        self.update_shader()

    # Method to overwrite!
    def init_batch(self):
        self.update_batch()

    # Method to overwrite!
    def update_shader(self):
        if not self.texture:
            return
        self.shader.bind()
        self.shader.uniform_sampler("image", self.texture)

    # Method to overwrite!
    def update_batch(self):
        self.batch = batch_for_shader(
            self.shader, 'TRI_FAN',
            {
                "pos": vertices_image(*self.ui_item.pos, *self.ui_item.size),
                "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
            },
        )
