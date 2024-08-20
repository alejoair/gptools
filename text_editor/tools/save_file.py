import sys
import os
import json
sys.path.append('/tmp/gptools/text_editor')
from tools.clear_editor import clear_editor

RESPONSE_OPTIONS = ['yes', 'no']

def save_file(state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get('scratch_file_path')
        working_file_path = state.get('working_file_path')
        if not scratch_file_path or not working_file_path:
            print('No se encontró información de los archivos de trabajo o scratch.')
            return

        print(f'Deseas guardar los cambios de {scratch_file_path} en {working_file_path}? para responder ejecuta "text_editor.py --response [yes, no]"')
        state['awaiting_orders'] = True
        state['pending_function'] = 'save_file'
        state['pending_function_options'] = RESPONSE_OPTIONS
        state_file.seek(0)
        json.dump(state, state_file, indent=4)
        state_file.truncate()

def handle_response(response):
    state_file_path = '/tmp/gptools/text_editor/temp/editor_state.json'
    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get('scratch_file_path')
        working_file_path = state.get('working_file_path')
        if response == 'yes' and scratch_file_path and working_file_path:
            with open(scratch_file_path, 'r') as src, open(working_file_path, 'w') as dest:
                dest.write(src.read())
            print(f'Cambios guardados en {working_file_path}.')
            clear_editor()
        else:
            print('No se han guardado los cambios, puedes seguir trabajando sobre el archivo y llamar a --operation save_file cuando estes listo para guardar, si lo que quieres es resetear el editor puedes llamar a --operation clear_editor')
            
        state['awaiting_orders'] = False
        state['pending_function'] = ''
        state['pending_function_options'] = []
        state_file.seek(0)
        json.dump(state, state_file, indent=4)
        state_file.truncate()
