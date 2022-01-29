
def header_ext(self, context):
    self.layout.operator('pk.picker')

def register():
    from bl_ui.space_view3d import VIEW3D_HT_header as Header
    Header.append(header_ext)

def unregister():
    from bl_ui.space_view3d import VIEW3D_HT_header as Header
    Header.remove(header_ext)
