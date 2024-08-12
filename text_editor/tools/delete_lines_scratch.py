import json
def delete_lines(state_file_path='/tmp/gptools/text_editor/temp/editor_state.json', start_line=1, end_line=1):
    if start_line is None or end_line is None:
        print('Error: Debes proporcionar los argumentos starting_line y end_line.')
        return
    with open(state_file_path, 'r+') as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get('scratch_file_path')
        if not scratch_file_path:
            print('No se encontró el archivo de scratch.')
            return
        with open(scratch_file_path, 'r') as file:
            lines = file.readlines()
        if start_line > len(lines) or end_line > len(lines):
            print(f'Advertencia: Las líneas a eliminar están fuera del rango del archivo.')
            return
        del lines[start_line-1:end_line]
        with open(scratch_file_path, 'w') as file:
            file.writelines(lines)
        print(f'Líneas {start_line} a {end_line} eliminadas del archivo {scratch_file_path}.')
        print(f'Contenido del archivo scratch después de la eliminación:')
        with open(scratch_file_path, 'r') as file:
            content = file.read()
            print(content)
        print('\nLos cambios no se han guardado en el archivo original. Para guardar los cambios, ejecute:')
        print('python3 /tmp/gptools/text_editor/text_editor.py --operation savefile\n')
        # Mensaje de advertencia sobre revisar el código
        print("\nVerifica detenidamente que las líneas eliminadas no hayan afectado la indentación o que no haya errores.")
