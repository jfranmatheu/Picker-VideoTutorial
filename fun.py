import bpy
from os.path import exists, isfile


def load_image_from_path(image_path: str):
    if not exists(image_path) or not isfile(image_path):
        return None
    image = bpy.data.images.load(image_path, check_existing=True)
    return image
