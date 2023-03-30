import bpy

def rename_materials():
    # Recorremos todos los materiales de la escena
    for material in bpy.data.materials:
        # Si el material ya tiene el nombre deseado, pasamos al siguiente
        if material.name.islower() and "_" not in material.name and material.name.isalnum():
            continue
        # Creamos un nuevo nombre para el material
        new_name = ''.join(c if c.isalnum() else "_" for c in material.name.lower())
        # Si el nombre ya existe, agregamos un número al final
        i = 0
        while new_name in bpy.data.materials and material.name != new_name:
            i += 1
            new_name = ''.join(c if c.isalnum() else "_" for c in material.name.lower()) + f"_{i}"
        # Renombramos el material
        material.name = new_name