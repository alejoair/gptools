import sys
import json
import argparse
from tools.open_file import open_file
from tools.clear_editor import clear_editor
from tools.replace_lines import replace_lines
from tools.save_file import save_file
from tools.insert_lines import insert_lines
from tools.delete_lines import delete_lines

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
        print("Respuesta  + args.response +  procesada por la función " + state["pending_function"])
    except ImportError as e:
        print("Error al importar el módulo para " + state["pending_function"] + ": " + str(e))
    except AttributeError as e:
        print("Error al encontrar la función handle_response en " + state["pending_function"] + ": " + str(e))

def main():
    parser = argparse.ArgumentParser(description="Editor de texto por línea de comandos.")
    parser.add_argument("--file_path", help="Ruta del archivo", required=False)
    parser.add_argument("--operation", help="Operación a realizar (ej. open_file, clear_editor, save_file, insert_lines, delete_lines)", required=False)
    parser.add_argument("--response", help="Respuesta a una función pendiente", required=False)
    parser.add_argument("--starting_line_number", help="Número de línea inicial", type=int, required=False)
    parser.add_argument("--ending_line_number", help="Número de línea final", type=int, required=False)
    parser.add_argument("--new_lines", help="Nuevas líneas a insertar", nargs="*", required=False)

    args = parser.parse_args()

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
        insert_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json", 
                     start_line=args.starting_line_number, 
                     new_lines=args.new_lines)
    elif args.operation == "delete_lines":
        delete_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json", 
                     start_line=args.starting_line_number, 
                     end_line=args.ending_line_number)
    elif args.operation == "replace_lines":
        replace_lines(state_file_path="/tmp/gptools/text_editor/temp/editor_state.json",
                  start_line=args.starting_line_number,
                  end_line=args.ending_line_number,
                  new_lines=args.new_lines)
    else:
        print("Operación " + args.operation + " no reconocida.")
        print("Operaciones válidas: open_file, clear_editor, save_file, insert_lines, delete_lines, replace_lines")

if __name__ == "__main__":
    main()
