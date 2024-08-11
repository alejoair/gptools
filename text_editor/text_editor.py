import sys
import json
import argparse
from tools.open_file import open_file
from tools.clear_editor import clear_editor

def handle_response(state, args):
    if not args.response:
        print(f"El editor está esperando una respuesta para la función {state['pending_function']} con las opciones {state['pending_function_options']}")
        print(f"Forma correcta de llamar al editor: --response <{', '.join(state['pending_function_options'])}>")
        return

    # Verificar el valor de state['pending_function']
    print(f"Intentando importar la función desde: tools.{state['pending_function']}")

    try:
        # Importar dinámicamente el módulo de la función pendiente
        pending_function_module = __import__(f"tools.{state['pending_function']}", fromlist=['handle_response'])
        # Llamar a la función handle_response del módulo pendiente
        pending_function_module.handle_response(args.response)
        print(f"Respuesta '{args.response}' procesada por la función {state['pending_function']}")
    except ImportError as e:
        print(f"Error al importar el módulo para {state['pending_function']}: {e}")
    except AttributeError as e:
        print(f"Error al encontrar la función handle_response en {state['pending_function']}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Editor de texto por línea de comandos.')
    parser.add_argument('--file_path', help='Ruta del archivo', required=False)
    parser.add_argument('--operation', help='Operación a realizar (ej. openfile, clear_editor)', required=False)
    parser.add_argument('--response', help='Respuesta a una función pendiente', required=False)

    args = parser.parse_args()

    valid_operations = ['openfile', 'clear_editor']

    with open('/tmp/gptools/text_editor/temp/editor_state.json', 'r') as file:
        state = json.load(file)

    if state['awaiting_orders']:
        if args.operation == 'clear_editor':
            clear_editor()
            return
        else:
            handle_response(state, args)
            return

    if args.operation:
        if args.operation == 'openfile':
            if not args.file_path:
                print('Error: file_path es necesario para la operación openfile.')
                return
            print(f'Operación openfile recibida para el archivo: {args.file_path}')
            open_file(args.file_path)
        elif args.operation == 'clear_editor':
            clear_editor()
        else:
            print(f'Operación "{args.operation}" no reconocida.')
            print(f'Operaciones válidas: {", ".join(valid_operations)}')
    elif args.response:
        handle_response(state, args)
    else:
        print('Error: Debe proporcionar una operación o una respuesta.')

if __name__ == '__main__':
    main()
