from blf import dimensions as text_dimensions, color as text_color, draw as text_draw, size as text_size, position as text_position

from . gr_rect import GrRect


class GrButton(GrRect):

    # Method to overwrite!
    def update_batch(self):
        super().update_batch()

        dim = text_dimensions(0, self.ui_item.label)
        self.text_pos = (
            int(self.ui_item.pos.x + dim[0] / 2.0),
            int(self.ui_item.pos.y + dim[1] / 2.0),
        )

    def draw(self):
        super().draw()
        #text_color()
        #text_size()
        text_position(0, *self.text_pos, 0)
        text_draw(0, self.ui_item.label)
