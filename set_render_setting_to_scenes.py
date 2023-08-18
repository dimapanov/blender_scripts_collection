import bpy

for scene in bpy.data.scenes:
    scene.render.engine = 'CYCLES'
    scene.render.resolution_x = 1500
    scene.render.resolution_y = 1500
    scene.render.resolution_percentage = 100
    scene.render.use_border = False
    scene.cycles.use_adaptive_sampling = True
    scene.cycles.device = "CPU"
    scene.cycles.use_denoising = False
    
    
    scene.cycles.preview_samples = 32
    
    scene.cycles.adaptive_threshold = 0.0100
    scene.cycles.samples = 256
    scene.cycles.adaptive_min_samples = 0
    
    scene.cycles.max_bounces = 8
    scene.cycles.diffuse_bounces = 4
    scene.cycles.glossy_bounces = 4
    scene.cycles.transmission_bounces = 8
    scene.cycles.volume_bounces = 0
    scene.cycles.transparent_max_bounces = 8
    
    scene.cycles.caustics_reflective = False
    scene.cycles.caustics_refractive = False
    
    scene.render.film_transparent = True
    
    scene.render.threads_mode = "AUTO"
    scene.cycles.use_auto_tile = False
    
    scene.view_settings.view_transform = 'Filmic'
    
    scene.view_settings.look = 'High Contrast'