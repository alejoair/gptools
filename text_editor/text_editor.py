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
    return urllib.parse.quote(urllib.parse.unquote(s)) == s

def decode_url_lines(encoded_string):
    if not is_url_encoded(encoded_string):
        print("Error: The new lines must be URL-encoded.")
        print("Correct usage example:")
        print("python3 text_editor.py --operation insert_lines --file_path /path/to/file.py --starting_line_number 10 "
              "--new_lines \"def%20my_function%28%29%3A%0A%20%20%20%20print%28%27Hello%2C%20world%21%27%29\"")
        print("Where:")
        print(" - 'def%20my_function%28%29%3A%0A%20%20%20%20print%28%27Hello%2C%20world%21%27%29' represents the code:")
        print("   def my_function():")
        print("       print('Hello, world!')")
        print("IMPORTANT: Always open the file with `--operation open_file` before attempting to modify it. "
              "Failure to do so may corrupt data and cause serious issues. Once the file is opened, "
              "you can apply modifications sequentially, such as inserting lines, replacing lines, etc., "
              "without having to reopen the file each time. After finishing the edits, you must call save_file, "
              "which will close the file. If you want to edit it again, you will need to open it again.")
        sys.exit(1)
    return urllib.parse.unquote(encoded_string).splitlines()

def handle_response(state, args):
    if not args.response:
        pending_function = state["pending_function"]
        options = ", ".join(state["pending_function_options"])
        print("The editor is awaiting a response for the function " + pending_function + " with the options " + options)
        print("Correct way to call the editor: --response <" + options + ">")
        return

    print("Attempting to import the function from: tools." + state["pending_function"])

    try:
        pending_function_module = __import__("tools." + state["pending_function"], fromlist=["handle_response"])
        pending_function_module.handle_response(args.response)
        print("Response " + args.response + " processed by the function " + state["pending_function"])
    except ImportError as e:
        print("Error importing the module for " + state["pending_function"] + ": " + str(e))
    except AttributeError as e:
        print("Error finding the handle_response function in " + state["pending_function"] + ": " + str(e))

def print_help():
    print("Command-line text editor.")
    print("Usage examples:")
    print("\n1. Open a file for editing:")
    print("   python3 text_editor.py --operation open_file --file_path /path/to/file.py")
    print("\n2. Insert new lines into a file (URL-encoded):")
    print("   python3 text_editor.py --operation insert_lines --file_path /path/to/file.py "
          "--starting_line_number 10 --new_lines \"def%20my_function%28%29%3A%0A%20%20%20%20print%28%27Hello%2C%20world%21%27%29\"")
    print("\n3. Replace lines in a file (URL-encoded):")
    print("   python3 text_editor.py --operation replace_lines --file_path /path/to/file.py "
          "--starting_line_number 10 --ending_line_number 12 --new_lines \"def%20updated_function%28%29%3A%0A%20%20%20%20print%28%27Updated%21%27%29\"")
    print("\n4. Save the file after editing:")
    print("   python3 text_editor.py --operation save_file --file_path /path/to/file.py")
    print("\nIMPORTANT:")
    print(" - Always open the file with `--operation open_file` before making modifications.")
    print(" - Use URL encoding for all new or replacement lines.")
    print(" - After completing your edits, save the file to apply changes.")

def main():
    parser = argparse.ArgumentParser(description="Command-line text editor.", add_help=False)
    parser.add_argument("--file_path", help="Path to the file", required=False)
    parser.add_argument("--operation", help="Operation to perform (e.g., open_file, clear_editor, save_file, insert_lines, delete_lines, replace_lines)", required=False)
    parser.add_argument("--response", help="Response to a pending function", required=False)
    parser.add_argument("--starting_line_number", help="Starting line number", type=int, required=False)
    parser.add_argument("--ending_line_number", help="Ending line number", type=int, required=False)
    parser.add_argument("--new_lines", help="New lines to insert (URL-encoded string)", required=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")

    args = parser.parse_args()

    if args.help:
        print_help()
        return

    # Decode the entire string of new lines with URL encoding validation
    if args.new_lines:
        try:
            args.new_lines = decode_url_lines(args.new_lines)
        except Exception as e:
            print(str(e))
            return

    # Read the state file
    with open("/tmp/gptools/text_editor/temp/editor_state.json", "r") as state_file:
        state = json.load(state_file)

    # Handle pending responses
    if state["awaiting_orders"]:
        handle_response(state, args)
        return

    # Perform operations
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
        print("Operation " + args.operation + " not recognized.")
        print("Valid operations: open_file, clear_editor, save_file, insert_lines, delete_lines, replace_lines")

if __name__ == "__main__":
    main()
