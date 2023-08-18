import bpy
from random import choices, random
# require at least 2 materials
assert len(bpy.data.materials) >= 2
foo = bpy.data.materials[-2:] # last 2 of all materials

mat1 = choices(foo, weights=[1, 0]).pop()
mat2 = choices(foo, weights=[0, 1]).pop()

ob = bpy.context.object
me = ob.data
me.materials.append(
        mat1 if random() < 0.2 else mat2
        )