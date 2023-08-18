import bpy

# Get the selected objects
selected_objects = bpy.context.selected_objects

# Create a new collection for each object
for obj in selected_objects:
    collection_name = obj.name + "_collection"
    new_collection = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(new_collection)
    new_collection.objects.link(obj)
n
