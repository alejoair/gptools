import json
from tools.read_line_numbers import number_lines

def delete_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json", start_line=1, end_line=None):
    if start_line is None or end_line is None:
        print("Error: Debes proporcionar los argumentos starting_line_number y ending_line_number.")
        return

    with open(state_file_path, "r+") as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get("scratch_file_path")
        if not scratch_file_path:
            print("Error: No se encontró el archivo de scratch.")
            print("Instrucciones:")
            print("1. Asegúrate de haber abierto el archivo correctamente con la operación open_file.")
            print("   Ejemplo: --operation open_file --file_path <ruta_del_archivo>")
            print("2. Una vez que el archivo esté abierto, podrás realizar la eliminación de líneas.")
            return

         try:
            with open(scratch_file_path, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Error: No se encontró el archivo de scratch.")
            print("Instrucciones:")
            print("1. Asegúrate de haber abierto el archivo correctamente con la operación open_file.")
            print("   Ejemplo: --operation open_file --file_path <ruta_del_archivo>")
            print("2. Una vez que el archivo esté abierto, podrás realizar la inserción de líneas.")
            return

        if start_line > len(lines):
            print("Error: El número de línea inicial es mayor que el número total de líneas en el archivo.")
            return

        if end_line > len(lines):
            end_line = len(lines)

        # Eliminar las líneas del rango especificado
        del lines[start_line-1:end_line]

        with open(scratch_file_path, "w") as file:
            file.writelines(lines)

        print(f"Líneas {start_line} a {end_line} eliminadas correctamente en {scratch_file_path}.")
        print("Para guardar los cambios, asegúrate de llamar a la función --operation save_file.")

        # Mostrar el contenido del archivo de scratch con números de línea
        print("Advertencia: El contenido del archivo de scratch ahora es el siguiente. Revísalo detenidamente para asegurar que no haya errores:")
        number_lines(scratch_file_path)

        print("Puedes deshacer estos cambios llamando a text_editor con la operación --operation undo.")
