import bpy


#scene = bpy.context.scene



for scene in bpy.data.scenes:
    
    scene.use_nodes = True
    nodes = scene.node_tree.nodes
    render_layers = nodes['Render Layers']
    bpy.context.window.scene = scene
    
    

    for node in  scene.node_tree.nodes:
        if node.name.startswith('File Output'):
           scene.node_tree.nodes.remove(node)
           
    output_file = scene.node_tree.nodes.new("CompositorNodeOutputFile")
    scene.node_tree.links.new(render_layers.outputs['Image'], output_file.inputs['Image'])
        
    scene.node_tree.nodes["File Output"].base_path = '//{sceneName}/'.format(
    file=bpy.data.filepath.rpartition('.')[0], sceneName=scene.name, camera=scene.camera.name)
    
    scene.node_tree.nodes["File Output"].file_slots[0].path = scene.name
            

