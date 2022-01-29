

class UIGraphics():
    def __init__(self, ui_item: 'UIItem', shader: 'GPUShader'):
        self.ui_item = ui_item
        self.shader = shader
        self.init_batch()
    
    # Method to overwrite!
    def init_batch(self):
        self.batch = None

    # Method to overwrite!
    def update_shader(self):
        pass

    # Method to overwrite!
    def update_batch(self):
        pass

    def draw(self):
        if self.batch:
            self.update_shader()
            self.batch.draw(self.shader)
