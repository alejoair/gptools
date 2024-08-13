import json

def delete_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json", start_line=1, end_line=1):
    if start_line is None or end_line is None:
        print("Error: Debes proporcionar los argumentos starting_line_number y ending_line_number.")
        return

    with open(state_file_path, "r+") as state_file:
        state = json.load(state_file)
        scratch_file_path = state.get("scratch_file_path")
        if not scratch_file_path:
            print("No se encontró el archivo de scratch.")
            return

        with open(scratch_file_path, "r") as file:
            lines = file.readlines()

        if start_line > len(lines) or end_line > len(lines) or start_line < 1 or end_line < 1:
            print(f"Error: Rango de líneas inválido. El archivo tiene {len(lines)} líneas.")
            return

        # Ajustar índice y eliminar líneas
        del lines[start_line-1:end_line]

        with open(scratch_file_path, "w") as file:
            file.writelines(lines)

        print(f"Líneas {start_line} a {end_line} eliminadas del archivo {scratch_file_path}.")
        print("Contenido del archivo después de la eliminación:")
        for line in lines:
            print(line, end="")

