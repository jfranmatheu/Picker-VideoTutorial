from mathutils import Vector
from . ui_graphics import UIGraphics


class UIItem():
    name = 'UI Item'

    def __init__(self, position: tuple = (0, 0), dimensions: tuple = (50, 50)):
        self._pos  = Vector(position) # Left-bottom corner.
        self._size = Vector(dimensions)
        self.parent = None

        self.hovered = False

        self.init_ui()
        self.init_graphics()

    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, new_pos: tuple):
        self._pos = Vector(new_pos)
        if self.parent:
            # TODO: finish this thing :-))) Also implement parent feature.
            # NOTE: we could have a flag to know if we may clamp the transform so it is contained inside the parent transform.
            # CLAMP: minimums.
            if self.parent.pos.x < self._pos.x:
                self._pos.x = self.parent.pos.x
            if self.parent.pos.y < self._pos.y:
                self._pos.y = self.parent.pos.y

        self.on_move()

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size: tuple):
        self._size = Vector(new_size)
        self.on_resize()

    def init_ui(self):
        pass

    def init_graphics(self):
        self.graphics = UIGraphics(self)

    def update_graphics(self):
        self.graphics.update_batch()
        self.graphics.update_shader()

    def _on_hover(self, point: Vector):
        self.hovered = self.on_hover(point)
        return self.hovered

    def on_hover(self, point: Vector):
        return (self.pos.x < point.x < self.pos.x + self.size.x) and (self.pos.y < point.y < self.pos.y + self.size.y)

    def _on_event(self, event: 'Event', mouse: Vector) -> bool:
        if not self._on_hover(mouse):
            return
        return self.on_event(event, mouse)

    def on_event(self, event: 'Event', mouse: Vector) -> bool:
        return

    def on_move(self):
        self.graphics.update_batch()

    def on_resize(self):
        self.graphics.update_batch()

    def draw(self):
        self.graphics.draw()
