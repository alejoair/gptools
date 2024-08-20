import os
import shutil
import json
from tools.clear_editor import clear_editor

print('Para guardar los cambios, asegúrate de llamar a la función --operation save_file.')
RESPONSE_OPTIONS = ['yes', 'no']

def open_file(file_path, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if not file_path:
        print('No se proporcionó ninguna ruta de archivo.')
        return

    if not os.path.exists(file_path):
        print(f'El archivo {file_path} no existe. ¿Deseas crearlo? para responder "text_editor.py --response [yes, no]"')
        try:
            with open(state_file_path, 'r+') as state_file:
                state = json.load(state_file)
                state['awaiting_orders'] = True
                state['pending_function'] = 'open_file'
                state['pending_function_options'] = RESPONSE_OPTIONS
                state['working_file_path'] = file_path
                state['scratch_file_path'] = ''  # No se define hasta que el archivo se cree
                state_file.seek(0)
                json.dump(state, state_file, indent=4)
                state_file.truncate()
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")
        return
    else:
        # Crear el archivo de scratch agregando '_scratch' antes de la extensión
        base_name, extension = os.path.splitext(file_path)
        scratch_file_path = f"{base_name}_scratch{extension}"
        undo_file_path = f"{base_name}_undo{extension}"

        try:
            shutil.copy(file_path, scratch_file_path)
            shutil.copy(file_path, undo_file_path)
        except IOError as e:
            print(f"Error al copiar archivos: {str(e)}")
            return

        # Actualizar el estado del editor
        try:
            with open(state_file_path, 'r+') as state_file:
                state = json.load(state_file)
                state['awaiting_orders'] = False
                state["undo_file_path"] = undo_file_path
                state['working_file_path'] = file_path
                state['scratch_file_path'] = scratch_file_path
                state_file.seek(0)
                json.dump(state, state_file, indent=4)
                state_file.truncate()
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")

        print(f'Archivo {file_path} abierto con éxito, ahora puedes aplicar operaciones como insert_lines, delete_lines, replace_lines y cuando valides que el archivo esta correcto debes llamar a --operation save_file para guardar los cambios')

def handle_response(response):
    if response == "yes":
        with open(state_file_path, 'r+') as state_file:
            state = json.load(state_file)
            filepath = state['working_file_path'] 
            with open(filepath, "w+") as file:
                pass
            open_file()
    else:
        clear_editor()
