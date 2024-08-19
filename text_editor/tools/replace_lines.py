import json

def replace_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json", start_line=1, end_line=None, new_lines=[]):
    if start_line is None or end_line is None or not new_lines:
        print("Error: Debes proporcionar los argumentos starting_line_number, ending_line_number, y new_lines.")
        return

    with open(state_file_path, "r+") as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get("scratch_file_path")
        if not scratch_file_path:
            print("Error: No se encontró el archivo de scratch.")
            print("Instrucciones:")
            print("1. Asegúrate de haber abierto el archivo correctamente con la operación open_file.")
            print("   Ejemplo: --operation open_file --file_path <ruta_del_archivo>")
            print("2. Una vez que el archivo esté abierto, podrás realizar la sustitución de líneas.")
            return

        with open(scratch_file_path, "r") as file:
            lines = file.readlines()

        if start_line > len(lines):
            print("Error: El número de línea inicial es mayor que el número total de líneas en el archivo.")
            return

        if end_line > len(lines):
            end_line = len(lines)

        # Reemplazar las líneas del rango especificado con las nuevas líneas
        lines[start_line-1:end_line] = [new_line + "\n" for new_line in new_lines]

        with open(scratch_file_path, "w") as file:
            file.writelines(lines)

        print(f"Líneas {start_line} a {end_line} reemplazadas correctamente en {scratch_file_path}.")

        print("Advertencia: El contenido del archivo de scratch ahora es el siguiente. Revísalo detenidamente para asegurar que no haya errores:")
        with open(scratch_file_path, "r") as file:
            for line in file:
                print(line, end="")

        print("\nPuedes deshacer estos cambios llamando a text_editor con la operación --operation undo.")