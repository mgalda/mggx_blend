import bpy

def rename_materials():
    for material in bpy.data.materials:
        if material.name:
            new_name = material.name.lower().replace(" ", "_")
            new_name = "".join(c if c.isalnum() else "_" for c in new_name)
            material.name = new_name
