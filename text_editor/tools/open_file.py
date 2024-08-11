import os
import shutil
import json
from tools.clear_editor import clear_editor

RESPONSE_OPTIONS = ["yes", "no"]

def open_file(file_path):
    try:
        with open(file_path, "r") as file:
            print(f"Archivo {file_path} abierto correctamente. Puedes aplicar operaciones en él.")
        scratch_file_path = file_path.replace(".txt", "_scratch.txt")
        shutil.copy(file_path, scratch_file_path)
        with open("/tmp/gptools/text_editor/temp/editor_state.json", "r+") as state_file:
            state = json.load(state_file)
            state["working_file_path"] = file_path
            state["scratch_file_path"] = scratch_file_path
            state["awaiting_orders"] = False
            state["pending_function"] = ""
            state["pending_function_options"] = []
            state_file.seek(0)
            json.dump(state, state_file, indent=4)
            state_file.truncate()
        print(f"Se ha creado un archivo de scratch en {scratch_file_path}.")
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado. ¿Deseas crearlo? (" + ", ".join(RESPONSE_OPTIONS) + ")")
        print(f"Forma correcta de responder: text_editor.py --response " + " ".join(RESPONSE_OPTIONS))
        with open("/tmp/gptools/text_editor/temp/editor_state.json", "r+") as state_file:
            state = json.load(state_file)
            state["awaiting_orders"] = True
            state["pending_function"] = "open_file"
            state["pending_function_options"] = RESPONSE_OPTIONS
            state["working_file_path"] = file_path
            state_file.seek(0)
            json.dump(state, state_file, indent=4)
            state_file.truncate()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def handle_response(response):
    state_file_path = "/tmp/gptools/text_editor/temp/editor_state.json"
    with open(state_file_path, "r") as state_file:
        state = json.load(state_file)
        file_path = state["working_file_path"]
        
        if response.lower() in ["s", "yes"]:
            with open(file_path, "w") as file:
                file.write("")  # Crear un archivo vacío
            print(f"Archivo {file_path} creado correctamente.")
            # Llamar a open_file para abrir el archivo recién creado
            open_file(file_path)
        else:
            print("Operación cancelada por el usuario.")
            # Llamar a clear_editor para limpiar el estado
            clear_editor()
