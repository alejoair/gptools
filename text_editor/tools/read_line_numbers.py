def number_lines(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line}", end="")
