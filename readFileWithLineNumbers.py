import sys

if len(sys.argv) < 2:
    print("[ERROR] Se requiere un argumento: la ruta del archivo a leer.")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        print(f"[INFO] Leyendo el archivo: {file_path}")
        for line_number, line in enumerate(file, 1):
            print(f"[INFO] Línea {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"[ERROR] No se encontró el archivo: {file_path}")
except Exception as e:
    print(f"[ERROR] Ocurrió un error al leer el archivo: {str(e)}")
