import bpy

# Store the current selection
selected_objects = bpy.context.selected_objects

# Iterate through selected objects
for obj in selected_objects:
    # Set origin to surface
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
    # Reset position
    obj.location = (0, 0, 0)