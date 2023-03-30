import bpy
import os

def export_material_images(output_folder):
    # Verificar si la carpeta existe, si no existe la crea
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Función para exportar la imagen del material en formato PNG
    def export_material_image(material, output_path):
        if material.node_tree:
            # Buscar el nodo de color base del material
            color_node = None
            for node in material.node_tree.nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    input = node.inputs.get("Base Color")
                    if input:
                        if input.is_linked:
                            # Si el nodo está conectado, verificar si la fuente es una imagen
                            if input.links[0].from_node.type == 'TEX_IMAGE':
                                color_node = node
                                break
                        else:
                            # Si el nodo no está conectado, verificar si el valor es un color
                            if input.default_value[:3] != (1, 1, 1):
                                color_node = node
                                break

            if color_node:
                # Exportar la imagen en formato PNG
                image_path = os.path.join(output_path, material.name + ".png")
                if color_node.inputs[0].is_linked:
                    image_node = color_node.inputs[0].links[0].from_node
                    if image_node.image:
                        image_node.image.save_render(image_path)
                else:
                    color = [int(c * 255) for c in color_node.inputs[0].default_value[:3]]
                    bpy.data.images.new(material.name, 1, 1).pixels = color * 4
                    bpy.data.images[material.name].save_render(image_path)

    # Lista de los materiales exportados para verificar si ya se exportó un material
    exported_materials = []

    # Recorrer los objetos seleccionados
    for obj in bpy.context.selected_objects:
        # Verificar que el objeto sea un mesh
        if obj.type == 'MESH':
            # Crear una lista de los materiales del objeto
            materials = obj.material_slots
            for material_slot in materials:
                # Obtener el material del slot
                material = material_slot.material
                # Verificar si el material es del tipo Principled BSDF
                if material and material.use_nodes and material.node_tree.nodes.get("Principled BSDF"):
                    # Obtener el nodo de base color del material
                    base_color_node = material.node_tree.nodes.get("Principled BSDF").inputs.get("Base Color")
                    if base_color_node:
                        if base_color_node.is_linked:
                            # Si el nodo está conectado, verificar si la fuente es una imagen
                            if base_color_node.links[0].from_node.type == 'TEX_IMAGE':
                                image_node = base_color_node.links[0].from_node
                                if image_node.image:
                                    # Exportar la imagen en formato PNG
                                    if material.name not in exported_materials:
                                        export_material_image(material, output_folder)
                                        exported_materials.append(material.name)
                        else:
                            # Si el nodo no está conectado, verificar si el valor es un color
                            if base_color_node.default_value[:3] != (1, 1, 1):
                                # Exportar un PNG de un color sólido
                                if material.name not in exported_materials:
                                    image_path = os.path.join(output_folder, material.name + ".png")
                                    color = [int(c * 255) for c in base_color_node.default
