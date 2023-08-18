import bpy

for mat in bpy.data.materials:
    if hasattr(mat.node_tree, "nodes"):
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                for input in node.inputs:
                    if input.name == 'Roughness':
                        input.default_value = 0.6