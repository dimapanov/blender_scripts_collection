import bpy

# Retrieve the current active collection from the view layer.
a = bpy.context.view_layer.active_layer_collection.collection

# Find the collection in the global list of collections using the active collection's name.
col = bpy.data.collections.get(a.name)

# Get the child elements (sub-collections) of the active collection.
coll = bpy.data.collections.get(a.name).children

# Create a new scene with the name of the active collection.
bpy.data.scenes.new(name=a.name)
