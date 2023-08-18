bl_info = {
    "name": "Hide selected/hide not selected and unhide from View&Render",
    "author": "Xylvier",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Hides selected/not selected and unhides objects from view and render at the same time",
    "warning": "",
    "wiki_url": "",
    "category": "operator",
}

import bpy

class HideselectedSet(bpy.types.Operator):
    """Hides selected objects from render&viewport"""
    bl_idname = "object.hide_set"
    bl_label = "Hide selected Objects from render&viewport"

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None

    def execute(self, context):
        for ob in context.selected_objects:
            obj.is_holdout = True
        return {'FINISHED'}

class HidenotselectedSet(bpy.types.Operator):
    """Hides not selected objects from render&viewport"""
    bl_idname = "object.invhide_set"
    bl_label = "Hide not selected Objects from render&viewport"

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None

    def execute(self, context):
        for obj in bpy.data.objects:
            if obj not in context.selected_objects:
                    if obj.type == 'MESH': 
                        obj.is_holdout = True
        
        return {'FINISHED'}

class UnhideSet(bpy.types.Operator):
    """Unhides selected objects from render&viewport"""
    bl_idname = "object.unhide_set"
    bl_label = "Unhide Objects from render&viewport"

    def execute(self, context):
        bpy.ops.object.hide_render_clear_all()
        for obj in bpy.data.objects:
            obj.is_holdout = False
        return {'FINISHED'}

def register():
    bpy.utils.register_class(HideselectedSet)
    bpy.utils.register_class(UnhideSet)
    bpy.utils.register_class(HidenotselectedSet)

def unregister():
    bpy.utils.unregister_class(HideselectedSet)
    bpy.utils.unregister_class(UnhideSet)
    bpy.utils.unregister_class(HidenotselectedSet)

if __name__ == "__main__":
    register()