import bpy
import os

def import_glb_as_scene(filepath):
    # Create a new scene
    scene = bpy.data.scenes.new(name=os.path.basename(filepath))
    
    # Set the new scene as the active scene
    bpy.context.window.scene = scene
    
    # Import the .glb file into the active scene
    bpy.ops.import_scene.gltf(filepath=filepath)

# Directory containing the .glb files
dir_path = ""  # Replace this with the path to your .glb files

# Get all .glb files in the directory
glb_files = [f for f in os.listdir(dir_path) if f.endswith('.glb')]

# Import each .glb file as a separate scene
for glb_file in glb_files:
    import_glb_as_scene(os.path.join(dir_path, glb_file))
