import bpy

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


for s in bpy.data.scenes :

    bpy.context.window.scene = s   #set as the active scene
    bpy.ops.render.render()  # for still render
    ShowMessageBox(s.name)    
    