import argparse
import sys
import json

def validate_lines_format(lines):
    if not isinstance(lines, list):
        print("[ERROR] The input must be a JSON array of strings.")
        return False
    for line in lines:
        if not isinstance(line, str):
            print(f"[ERROR] Each line must be a string. Invalid line: {line}")
            return False
    return True

def insert_lines(file_path, line_start, new_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_start = int(line_start) - 1

    for i, line in enumerate(new_lines):
        lines.insert(line_start + i, line + '\n')

    print_file_with_line_numbers(lines, line_start, len(new_lines), '+')

    with open(file_path, 'w') as file:
        file.writelines(lines)

def overwrite_lines(file_path, line_start, line_end, new_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if line_end > len(lines):
        print(f"[ERROR] The file has only {len(lines)} lines. The range {line_start}-{line_end} is invalid.")
        return

    expected_lines = line_end - line_start + 1
    if len(new_lines) != expected_lines:
        print(f"[ERROR] Expected {expected_lines} new line(s), but received {len(new_lines)}.")
        return

    for i in range(line_start - 1, line_end):
        line_content = new_lines[i - (line_start - 1)]
        lines[i] = line_content + '\n'

    print_file_with_line_numbers(lines, line_start - 1, len(new_lines), '~')

    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("[INFO] File successfully updated.")

def delete_lines(file_path, line_start, line_end):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    deleted_lines = lines[line_start-1:line_end]
    lines = lines[:line_start-1] + lines[line_end:]

    with open(file_path, 'w') as file:
        file.writelines(lines)

    print("[INFO] Lines deleted successfully.")
    print("[INFO] File content after deletion:")

    for i, line in enumerate(lines):
        line_number = f'{i + 1:05}'
        print(f'{line_number}> {line}')

    for i, line in enumerate(deleted_lines):
        line_number = f'{line_start + i:05}'
        print(f'{line_number}~ {line}')

def print_file_with_line_numbers(lines, start_index, num_lines, symbol):
    for i, line in enumerate(lines):
        line_number = f'{i + 1:05}'
        if start_index <= i < start_index + num_lines:
            print(f'{line_number}>{symbol} {line}')
        else:
            print(f'{line_number}> {line}')

def main():
    parser = argparse.ArgumentParser(description='Script to modify files.')
    parser.add_argument('--operation', type=str, required=True, help='Operation to perform: insert, delete, overwrite')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the file to be modified')
    parser.add_argument('--line_start', type=int, help='Starting line for insert or overwrite')
    parser.add_argument('--line_end', type=int, help='Ending line for overwrite')
    parser.add_argument('--new_lines', type=str, help='New lines in JSON format to insert or overwrite')

    args = parser.parse_args()

    # Parse the JSON string into a list of lines
    try:
        new_lines = json.loads(args.new_lines) if args.new_lines else None
    except json.JSONDecodeError:
        print("[ERROR] The new lines must be a valid JSON array.")
        print("Example of valid input:")
        print('  python3 script.py --new_lines \'["line 1", "line 2", "line 3"]\'')
        sys.exit(1)

    if new_lines and not validate_lines_format(new_lines):
        print("[ERROR] Invalid format detected in new lines.")
        print("Each line must be a string within a JSON array.")
        print("Example of valid input:")
        print('  python3 script.py --new_lines \'["line 1", "line 2", "line 3"]\'')
        print("Example of valid multi-line input:")
        print('  python3 script.py --new_lines \'["line 1", "line 2", "print(f\'Hello {name}\')"]\'')
        sys.exit(1)

    if args.operation == 'insert':
        if not args.line_start or not new_lines:
            print("Error: --line_start and --new_lines are required for the insert operation")
            sys.exit(1)
        insert_lines(args.file_path, args.line_start, new_lines)
    elif args.operation == 'overwrite':
        if not args.line_start or not args.line_end or not new_lines:
            print("Error: --line_start, --line_end, and --new_lines are required for the overwrite operation")
            sys.exit(1)
        overwrite_lines(args.file_path, args.line_start, args.line_end, new_lines)
    elif args.operation == 'delete':
        if not args.line_start or not args.line_end:
            print("Error: --line_start and --line_end are required for the delete operation")
            sys.exit(1)
        delete_lines(args.file_path, args.line_start, args.line_end)
    else:
        print(f"Operation '{args.operation}' not implemented.")
        sys.exit(1)

if __name__ == '__main__':
    main()
