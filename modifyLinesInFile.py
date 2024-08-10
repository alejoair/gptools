import sys

# Descripción:
# Este script permite modificar o agregar líneas en un archivo de texto.
# Recibe cuatro o más argumentos: la ruta del archivo, el número de línea inicial,
# el número de línea final, y los contenidos que se agregarán o modificarán.
# No es necesario pasarle los saltos de línea (\n), ya que el script los añade automáticamente.
# Cada línea debe estar entre comillas y puede contener comillas internas.

if len(sys.argv) < 5:
    print("[ERROR] Se requieren al menos 4 argumentos: el path del archivo, la línea inicial, la línea final, y el contenido a agregar.")
    sys.exit(1)

file_path = sys.argv[1]
line_start = int(sys.argv[2])
line_end = int(sys.argv[3])
new_contents = sys.argv[4:]

try:
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Si el rango supera la cantidad de líneas actuales, agregar líneas vacías.
    if line_end > len(lines):
        print("[INFO] El rango de líneas excede el número total de líneas en el archivo.")
        for i in range(len(lines), line_end):
            lines.append("\n")

    # Sobrescribir las líneas en el rango especificado con el contenido pasado.
    for i in range(line_start - 1, line_end):
        content_index = i - (line_start - 1)
        if content_index < len(new_contents):
            new_content = new_contents[content_index]
            print(f"[INFO] Modificando/agregando línea {i + 1} con el nuevo contenido.")
            lines[i] = f"{new_content}\n"

    # Limpiar cualquier línea adicional fuera del rango especificado.
    if len(lines) > line_end:
        lines = lines[:line_end]

    with open(file_path, "w") as file:
        file.writelines(lines)

    print("[INFO] Modificaciones completadas.")

except FileNotFoundError:
    print(f"[ERROR] No se encontró el archivo: {file_path}")
except Exception as e:
    print(f"[ERROR] Ocurrió un error al modificar el archivo: {str(e)}")
