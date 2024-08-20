import os
import shutil
import json
from tools.clear_editor import clear_editor

RESPONSE_OPTIONS = ['yes', 'no']

def update_state(state_file_path, state_data):
    try:
        with open(state_file_path, 'r+') as state_file:
            state_file.seek(0)
            json.dump(state_data, state_file, indent=4)
            state_file.truncate()
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al actualizar el estado del editor: {str(e)}")

def open_file(file_path, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if not file_path:
        print('No se proporcionó ninguna ruta de archivo.')
        return

    if not os.path.exists(file_path):
        print(f'El archivo {file_path} no existe. ¿Deseas crearlo? Para responder: "text_editor.py --response [yes, no]"')
        try:
            with open(state_file_path, 'r+') as state_file:
                try:
                    state = json.load(state_file)
                except json.JSONDecodeError:
                    print("no se pudo decodificar el archivo de estado")
                    return

                state.update({
                    'awaiting_orders': True,
                    'pending_function': 'open_file',
                    'pending_function_options': RESPONSE_OPTIONS,
                    'working_file_path': file_path,
                    'scratch_file_path': ''  # No se define hasta que el archivo se cree
                })

                update_state(state_file_path, state)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")
        return
    else:
        base_name, extension = os.path.splitext(file_path)
        scratch_file_path = f"{base_name}_scratch{extension}"
        undo_file_path = f"{base_name}_undo{extension}"

        try:
            shutil.copy(file_path, scratch_file_path)
            shutil.copy(file_path, undo_file_path)
        except IOError as e:
            print(f"Error al copiar archivos: {str(e)}")
            return

        try:
            with open(state_file_path, 'r+') as state_file:
                try:
                    state = json.load(state_file)
                except json.JSONDecodeError:
                    print("Error al decodificar el archivo de estado")

                state.update({
                    'awaiting_orders': False,
                    'undo_file_path': undo_file_path,
                    'scratch_file_path': scratch_file_path
                })

                update_state(state_file_path, state)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")

def handle_response(response, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if response not in RESPONSE_OPTIONS:
        print(f'Respuesta inválida: {response}')
        return

    try:
        with open(state_file_path, 'r+') as state_file:
            state = json.load(state_file)
            file_path = state.get("working_file_path")
            if response == 'yes':
                open(file_path, 'w+').close()
                open_file(file_path, state_file_path)
            else:
                print(f"No se ha creado el archivo {file_path}")
            
            state.update({
                'awaiting_orders': False,
                'pending_function': None,
                'pending_function_options': None
            })

            update_state(state_file_path, state)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al manejar la respuesta: {str(e)}")
