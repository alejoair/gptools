import sys
import json
import argparse
import urllib.parse
from tools.open_file import open_file
from tools.clear_editor import clear_editor
from tools.replace_lines import replace_lines
from tools.save_file import save_file
from tools.insert_lines import insert_lines
from tools.delete_lines import delete_lines

def is_url_encoded(s):
    # Comprobar si la cadena está codificada en URL
    return urllib.parse.quote(urllib.parse.unquote(s)) == s

def decode_url_lines(encoded_lines):
    for line in encoded_lines:
        if not is_url_encoded(line):
            print("Error: Las líneas nuevas deben estar codificadas en URL.")
            print("Ejemplo real de uso correcto:")
            print("python3 text_editor.py --operation insert_lines --file_path /ruta/al/archivo.py --starting_line_number 10 "
                  "--new_lines \"def%20mi_funcion%28%29%3A%0A%20%20%20%20print%28%27Hola%2C%20mundo%21%27%29\"")
            print("Donde:")
            print(" - 'def%20mi_funcion%28%29%3A%0A%20%20%20%20print%28%27Hola%2C%20mundo%21%27%29' representa el código:")
            print("   def mi_funcion():")
            print("       print('Hola, mundo!')")
            print("IMPORTANTE: Siempre debes abrir el archivo con `--operation open_file` antes de intentar modificarlo. "
                  "No hacerlo puede corromper los datos y causar problemas graves. Una vez abierto el archivo se pueden aplicar modificaciones de forma secuencial, por ejemplo se puede insertar lineas, reemplazar lineas, etc sin tener que abrir el archivo en cada una, luego de terminar las ediciones se debe llamar a save_file, esto cerrara el archivo, lo que significa que se tendria que volver a abrir si se quiere editarlo nuevamente")
            sys.exit(1)
    return [urllib.parse.unquote(line) for line in encoded_lines]

def handle_response(state, args):
    if not args.response:
        pending_function = state["pending_function"]
        options = ", ".join(state["pending_function_options"])
        print("El editor está esperando una respuesta para la función " + pending_function + " con las opciones " + options)
        print("Forma correcta de llamar al editor: --response <" + options + ">")
        return

    print("Intentando importar la función desde: tools." + state["pending_function"])

    try:
        pending_function_module = __import__("tools." + state["pending_function"], fromlist=["handle_response"])
        pending_function_module.handle_response(args.response)
        print("Respuesta " + args.response + " procesada por la función " + state["pending_function"])
    except ImportError as e:
        print("Error al importar el módulo para " + state["pending_function"] + ": " + str(e))
    except AttributeError as e:
        print("Error al encontrar la función handle_response en " + state["pending_function"] + ": " + str(e))

def main():
    parser = argparse.ArgumentParser(description="Editor de texto por línea de comandos.")
    parser.add_argument("--file_path", help="Ruta del archivo", required=False)
    parser.add_argument("--operation", help="Operación a realizar (ej. open_file, clear_editor, save_file, insert_lines, delete_lines, replace_lines)", required=False)
    parser.add_argument("--response", help="Respuesta a una función pendiente", required=False)
    parser.add_argument("--starting_line_number", help="Número de línea inicial", type=int, required=False)
    parser.add_argument("--ending_line_number", help="Número de línea final", type=int, required=False)
    parser.add_argument("--new_lines", help="Nuevas líneas a insertar (codificadas en URL)", required=False)

    args = parser.parse_args()

    # Decodificar líneas nuevas con validación de URL encoding
    if args.new_lines:
        try:
            args.new_lines = decode_url_lines([args.new_lines])
        except Exception as e:
            print(str(e))
            return

    # Leer el archivo de estado
    with open("/tmp/gptools/text_editor/temp/editor_state.json", "r") as state_file:
        state = json.load(state_file)

    # Manejo de respuestas
    if state["awaiting_orders"]:
        handle_response(state, args)
        return

    # Realizar operaciones
    if args.operation == "open_file":
        open_file(args.file_path)
    elif args.operation == "clear_editor":
        clear_editor()
    elif args.operation == "save_file":
        save_file()
    elif args.operation == "insert_lines":
        insert_lines(start_line=args.starting_line_number, 
                     new_lines=args.new_lines,
                     args=args)
    elif args.operation == "delete_lines":
        delete_lines(start_line=args.starting_line_number, 
                     end_line=args.ending_line_number,
                     args=args)
    elif args.operation == "replace_lines":
        replace_lines(start_line=args.starting_line_number,
                      end_line=args.ending_line_number,
                      new_lines=args.new_lines,
                      args=args)
    else:
        print("Operación " + args.operation + " no reconocida.")
        print("Operaciones válidas: open_file, clear_editor, save_file, insert_lines, delete_lines, replace_lines")

if __name__ == "__main__":
    main()
