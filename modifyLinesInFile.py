import argparse
import sys

def validate_lines_format(lines):
    for line in lines:
        if not (line.startswith('[') and line.endswith(']')):
            return False
    return True

def insert_lines(file_path, line_start, new_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_start = int(line_start) - 1

    for i, line in enumerate(new_lines):
        line_content = line[1:-1]  # Remover los corchetes antes de insertar
        lines.insert(line_start + i, line_content + '\n')

    print_file_with_line_numbers(lines, line_start, len(new_lines), '+')

    with open(file_path, 'w') as file:
        file.writelines(lines)

def overwrite_lines(file_path, line_start, line_end, new_lines):
    print("[DEBUG] Abriendo el archivo:", file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("[DEBUG] Número total de líneas en el archivo:", len(lines))

    if line_end > len(lines):
        print(f"[ERROR] El archivo tiene solo {len(lines)} líneas. El rango {line_start}-{line_end} es inválido.")
        print(f"Para insertar las líneas que faltan, use la función de inserción:")
        print(f"Ejemplo: python3 modifyLinesInFile.py --operation insert --file_path {file_path} --line_start {len(lines) + 1} --new_lines '[Nueva línea]'")
        return

    # Eliminar solo los corchetes de las nuevas líneas, preservando tabulaciones y espacios
    new_lines = [line[1:-1] for line in new_lines]

    for i in range(line_start - 1, line_end):
        line_content = new_lines[i - (line_start - 1)]
        print(f"[DEBUG] Línea después de remover corchetes: '{line_content}'")
        
        lines[i] = line_content + '\n'
        print(f"[DEBUG] Línea sobrescrita en el archivo: '{lines[i].strip()}'")

    print_file_with_line_numbers(lines, line_start - 1, len(new_lines), '~')

    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("[DEBUG] Archivo actualizado exitosamente.")




def print_file_with_line_numbers(lines, start_index, num_lines, symbol):
    for i, line in enumerate(lines):
        line_number = f'{i + 1:05}'
        if start_index <= i < start_index + num_lines:
            print(f'{line_number}>{symbol} {line.strip()}')
        else:
            print(f'{line_number}> {line.strip()}')

def main():
    parser = argparse.ArgumentParser(description='Script para modificar archivos.')
    parser.add_argument('--operation', type=str, required=True, help='Operación a realizar: insert, delete, overwrite')
    parser.add_argument('--file_path', type=str, required=True, help='Ruta del archivo a modificar')
    parser.add_argument('--line_start', type=int, help='Línea inicial para insertar o modificar')
    parser.add_argument('--line_end', type=int, help='Línea final para modificar')
    parser.add_argument('--new_lines', type=str, nargs='+', help='Nuevas líneas a insertar o modificar')

    args = parser.parse_args()

    if args.new_lines and not validate_lines_format(args.new_lines):
        print("[ERROR] Las nuevas líneas deben estar delimitadas por corchetes [ ].")
        print("Ejemplos de líneas válidas:")
        print("  [Nueva línea 1]")
        print("  [Otra línea con texto]")
        print("  [Texto adicional con espacios]")
        sys.exit(1)

    if args.operation == 'insert':
        if not args.line_start or not args.new_lines:
            print("Error: --line_start y --new_lines son obligatorios para la operación insert")
            sys.exit(1)
        insert_lines(args.file_path, args.line_start, args.new_lines)
    elif args.operation == 'overwrite':
        if not args.line_start or not args.line_end or not args.new_lines:
            print("Error: --line_start, --line_end, y --new_lines son obligatorios para la operación overwrite")
            sys.exit(1)
        overwrite_lines(args.file_path, args.line_start, args.line_end, args.new_lines)
    else:
        print(f"Operación '{args.operation}' no implementada.")
        sys.exit(1)

if __name__ == '__main__':
    main()
