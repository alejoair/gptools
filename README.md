### Updated Instructions for modifyLinesInFile.py

**1. Insert a Line:**
```bash
python3 modifyLinesInFile.py --operation insert --file_path <file_path> --line_start <line_number> --new_lines "[\"line1\", \"line2\"]"
```
**2. Overwrite Lines:**
```bash
python3 modifyLinesInFile.py --operation overwrite --file_path <file_path> --line_start <start_line> --line_end <end_line> --new_lines "[\"line1\", \"line2\"]"
```
**3. Delete Lines:**
```bash
python3 modifyLinesInFile.py --operation delete --file_path <file_path> --line_start <start_line> --line_end <end_line>
```

