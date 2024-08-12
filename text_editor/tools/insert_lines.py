import json

def insert_lines(state_file_path='/tmp/gptools/text_editor/temp/editor_state.json', start_line=1, new_lines=None):
    if start_line is None:
        print('Error: Debes proporcionar el argumento starting_line_number.')
        return

    if new_lines is None:
        new_lines = []

    # Agregar \n al final de cada línea
    new_lines = [line + '\n' for line in new_lines]

    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get('scratch_file_path')
        if not scratch_file_path:
            print('No se encontró el archivo de scratch.')
            return

        # Leer el archivo de scratch
        with open(scratch_file_path, 'r') as file:
            lines = file.readlines()

        # Manejar el caso donde la posición de inserción excede el número de líneas
        if start_line > len(lines):
            print(f'Advertencia: La posición de inserción ({start_line}) excede el número de líneas ({len(lines)}). Insertando al final del archivo.')
            start_line = len(lines) + 1

        # Insertar las nuevas líneas en la posición especificada
        lines[start_line-1:start_line-1] = new_lines

        # Escribir los cambios de vuelta en el archivo de scratch
        with open(scratch_file_path, 'w') as file:
            file.writelines(lines)

        print(f'Líneas insertadas en el archivo {scratch_file_path} en la línea {start_line}.')

        # Mostrar el contenido del archivo de scratch después de la inserción
        with open(scratch_file_path, 'r') as file:
            content = file.read()
            print("Verifica detenidamente que las lineas insertadas no tengan errores de identacion, y los caracteres se hallan escapado correctamente")
            print(f'Contenido del archivo scratch después de la inserción:\n{content}')

        # Mensaje de advertencia sobre el guardado de cambios
        print("\nLos cambios no se han guardado en el archivo original. Para guardar los cambios, ejecute:")
        print("python3 /tmp/gptools/text_editor/text_editor.py --operation savefile\n")

def handle_response(response):
    pass
