bl_info = {
    "name": "mggx_blend",
    "description": "Funciones para procesos recurrentes y en lote",
    "author": "Mi nombre",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Sidebar",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

import bpy

def register():
    print("El complemento ha sido registrado.")

def unregister():
    print("El complemento ha sido desregistrado.")
    
if __name__ == "__main__":
    register()
