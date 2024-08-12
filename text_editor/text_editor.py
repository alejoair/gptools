import sys
import json
import argparse
from tools.open_file import open_file
from tools.clear_editor import clear_editor
from tools.save_file import save_file
from tools.insert_lines import insert_lines
from tools.delete_lines import delete_lines  # Importar la nueva función

def handle_response(state, args):
    if not args.response:
        print(f"El editor está esperando una respuesta para la función {state['pending_function']} con las opciones {state['pending_function_options']}")
        print(f"Forma correcta de llamar al editor: --response <{', '.join(state['pending_function_options'])}>")
        return

    print(f"Intentando importar la función desde: tools.{state['pending_function']}")

    try:
        pending_function_module = __import__(f"tools.{state['pending_function']}", fromlist=['handle_response'])
        pending_function_module.handle_response(args.response)
        print(f"Respuesta '{args.response}' procesada por la función {state['pending_function']}")
    except ImportError as e:
        print(f"Error al importar el módulo para {state['pending_function']}: {e}")
    except AttributeError as e:
        print(f"Error al encontrar la función handle_response en {state['pending_function']}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Editor de texto por línea de comandos.")
    parser.add_argument("--file_path", help="Ruta del archivo", required=False)
    parser.add_argument("--operation", help="Operación a realizar (ej. openfile, clear_editor, savefile, insert_lines, delete_lines)", required=False)
    parser.add_argument("--response", help="Respuesta a una función pendiente", required=False)
    parser.add_argument("--starting_line_number", help="Número de línea inicial", type=int, required=False)
    parser.add_argument("--ending_line_number", help="Número de línea final", type=int, required=False)
    parser.add_argument("--new_lines", help="Nuevas líneas a insertar", nargs='*', required=False)

    args = parser.parse_args()

    valid_operations = ["openfile", "clear_editor", "savefile", "insert_lines", "delete_lines"]

    with open("/tmp/gptools/text_editor/temp/editor_state.json", "r") as file:
        state = json.load(file)

    if state['awaiting_orders'] and args.operation != "clear_editor":
        handle_response(state, args)
        return

    if args.operation not in valid_operations:
        print(f"Operación {args.operation} no reconocida.")
        print(f"Operaciones válidas: {', '.join(valid_operations)}")
        return

    if args.operation == "openfile":
        open_file(args.file_path)
    elif args.operation == "clear_editor":
        clear_editor()
    elif args.operation == "savefile":
        save_file()
    elif args.operation == "insert_lines":
        insert_lines(
            start_line=args.starting_line_number,
            new_lines=args.new_lines
        )
    elif args.operation == "delete_lines":  # Nueva operación para eliminar líneas
        delete_lines(
            start_line=args.starting_line_number,
            end_line=args.ending_line_number
        )

if __name__ == "__main__":
    main()
