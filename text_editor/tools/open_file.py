import os
import shutil
import json
from tools.clear_editor import clear_editor
from tools.read_line_numbers import number_lines


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

    if not os.path.exists(file_path):  #Si el archivo no existe
        print(f'El archivo {file_path} no existe. ¿Deseas crearlo? Para responder: "text_editor.py --response [yes, no]"')
        try:
            with open(state_file_path, 'r+') as state_file:
                try:
                    state = json.load(state_file)
                except json.JSONDecodeError:
                    print("no se pudo decodificar el archivo de estado")
                    return
                #Vamos a esperar la respuesta del usuario
                state.update({
                    'awaiting_orders': True,
                    'pending_function': 'open_file',
                    'pending_function_options': RESPONSE_OPTIONS,
                    'working_file_path': file_path,
                })

                update_state(state_file_path, state)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al manejar el estado del editor: {str(e)}")
        return
    
    else:  #Si el archivo si existe
        print(f"Se abrio el archivo {file_path} y su contenido ahora es el siguiente. ahora podras llamar las funciones operation insert_lines, delete_lines, modify_lines y cuando hallas terminado de edtarlo y el archivo se encuentre correcto, llama a --operation save_file, los cambios no se guardaran hasta que lo hagas")
        print(f"Contenido de {file_path}: \n\n")
        
        base_name, extension = os.path.splitext(file_path)
        scratch_file_path = f"{base_name}_scratch{extension}"
        undo_file_path = f"{base_name}_undo{extension}"

        number_lines(file_path) #Imprimimos el contenido del archivo numerado por lineas
        
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
                    'pending_function': '',
                    'pending_function_options': [],
                    'awaiting_orders': False,
                    'working_file_path': file_path,
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

    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        file_path = state.get("working_file_path")
        if response == 'yes':
            # Crear la ruta completa si no existe
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directorio {directory} creado.")

            open(file_path, 'w+').close()  # Crear el archivo
            open_file(file_path, state_file_path)
            return
        else:
            print(f"No se ha creado el archivo {file_path}")

        state.update({
            'awaiting_orders': False,
            'pending_function': None,
            'pending_function_options': None
        })

        update_state(state_file_path, state)
