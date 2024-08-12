import os
import shutil
import json
from tools.clear_editor import clear_editor

RESPONSE_OPTIONS = ['yes', 'no']

def open_file(file_path, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if not file_path:
        print('No se proporcionó ninguna ruta de archivo.')
        return

    if not os.path.exists(file_path):
        print(f'El archivo {file_path} no existe. ¿Deseas crearlo? (yes, no)')
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
        return

    # Crear el archivo de scratch agregando '_scratch' antes de la extensión
    base_name, extension = os.path.splitext(file_path)
    scratch_file_path = f"{base_name}_scratch{extension}"
    shutil.copy(file_path, scratch_file_path)

    # Actualizar el estado del editor
    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        state['awaiting_orders'] = False
        state['working_file_path'] = file_path
        state['scratch_file_path'] = scratch_file_path
        state_file.seek(0)
        json.dump(state, state_file, indent=4)
        state_file.truncate()

    print(f'Archivo {file_path} abierto con éxito y copiado a {scratch_file_path}.')

def handle_response(response, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if response not in RESPONSE_OPTIONS:
        print(f'Respuesta inválida: {response}. Operación cancelada.')
        clear_editor(state_file_path)
        return

    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        file_path = state['working_file_path']
        if response == 'yes':
            open(file_path, 'w').close()  # Crear el archivo vacío
            open_file(file_path, state_file_path)
        else:
            print('Operación cancelada por el usuario.')
            clear_editor(state_file_path)
