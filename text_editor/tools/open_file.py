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
        print(f'El archivo {file_path} no existe. ¿Deseas crearlo? Para responder: "text_editor.py --response [yes, no]"')
        try:
            # Abrir o crear el archivo de estado
            with open(state_file_path, 'r+') as state_file:
                try:
                    state = json.load(state_file)
                except json.JSONDecodeError:
                    state = {}
                
                # Actualizar el estado con la información necesaria
                state['awaiting_orders'] = True
                state['pending_function'] = 'open_file'
                state['pending_function_options'] = RESPONSE_OPTIONS
                state['working_file_path'] = file_path
                state['scratch_file_path'] = ''  # No se define hasta que el archivo se cree

                # Guardar el estado actualizado
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

        # Actualizar el estado del editor con las rutas de archivo creadas
        try:
            with open(state_file_path, 'r+') as state_file:
                try:
                    state = json.load(state_file)
                except json.JSONDecodeError:
                    state = {}

                state['awaiting_orders'] = False
                state["undo_file_path"] = undo_file_path
                state["scratch_file_path"] = scratch_file_path

                # Guardar el estado actualizado
                state_file.seek(0)
                json.dump(state, state_file, indent=4)
                state_file.truncate()
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")

def handle_response(response, state_file_path='/tmp/gptools/text_editor/temp/editor_state.json'):
    if response not in RESPONSE_OPTIONS:
        print(f'Respuesta inválida: {response}')
        return

    try:
        with open(state_file_path, 'r+') as state_file:
            state = json.load(state_file)

            if response == 'yes':
                # Crear el archivo y el archivo de scratch
                open(file_path, 'w').close()
                open_file(state['working_file_path'], state_file_path)

            # Limpiar estado pendiente
            state['awaiting_orders'] = False
            state['pending_function'] = None
            state['pending_function_options'] = None

            # Guardar el estado actualizado
            state_file.seek(0)
            json.dump(state, state_file, indent=4)
            state_file.truncate()
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al manejar la respuesta: {str(e)}")
