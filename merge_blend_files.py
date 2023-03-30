import bpy
import os

def merge_blend_files(folder_paths, output_path):
    """
    Imports all .blend files from the specified folder paths and saves them as a consolidated .blend file.
    
    :param folder_paths: A list of folder paths to search for .blend files.
    :param output_path: The output path for the consolidated .blend file.
    """
    # Import .blend files from the specified folder paths
    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".blend"):
                    filepath = os.path.join(root, file)
                    with bpy.data.libraries.load(filepath) as (data_from, data_to):
                        data_to.objects = data_from.objects

                    # Add the imported objects to the current file
                    for obj in data_to.objects:
                        if obj is not None:
                            bpy.context.scene.collection.objects.link(obj)

    # Save the consolidated .blend file
    bpy.ops.wm.save_as_mainfile(filepath=output_path)
