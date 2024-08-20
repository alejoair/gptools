import os
import json


def clear_editor(state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    with open(state_file_path, 'r+') as file:
        state = json.load(file)
        scratch_file_path = state.get('scratch_file_path')
        if scratch_file_path and os.path.exists(scratch_file_path):
            os.remove(scratch_file_path)
            print(f'Scratch file {scratch_file_path} eliminado.')
        else:
            print('No se encontró ningún scratch file para eliminar.')
        # Limpiar el estado
        state.update({
            'awaiting_orders': False,
            'working_file_path': '',
            'scratch_file_path': '',
            'pending_function': '',
            'pending_function_options': []
        })
        file.seek(0)
        json.dump(state, file, indent=4)
        file.truncate()
        print('Editor limpiado y estado restablecido.')
