import gpu
from gpu_extras.batch import batch_for_shader

shader_2d_unif_color = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
shader_2d_image = gpu.shader.from_builtin('2D_IMAGE')
