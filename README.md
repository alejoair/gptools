#This documentation should be displayed entirely to the user, not a summary
# GPTools text_editor.py README

## URL Encoding Explanation

When encoding in URL, characters that are unsafe or not allowed in the URL must be replaced with their hexadecimal value preceded by a `%`. Below are some common characters and their URL encoding:

- **Space**: Encoded as `%20`.
- **Line Feed (LF)**: Encoded as `%0A`.
- **Carriage Return (CR)**: Encoded as `%0D`.
- **Horizontal Tab**: Encoded as `%09`.
- **Special Characters**: Characters like `!`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `:`, `;`, `=`, `?`, `@`, `[`, `]`, and others are encoded using `%` followed by their hexadecimal value. For example, `#` is encoded as `%23`.
- 
# When you encode the new_lines that will be inserted on a file, you should encode ALWAYS encode ALL the special characters, text_editor.py will throw an error if you dont, also that will cause data corruption with dangerous consecuences for the user, GPTerminal should ALWAYS encode the new lines on a URL format as this:
# python3 /tmp/gptools/text_editor/text_editor.py --operation insert_lines --file_path /tmp/python_project/config.py --line_number 5 --new_lines "def%20my_function()%3A%0A%20%20%20%20print(%27Hello%27)%0A%20%20%20%20return%20True" all the required characters are encoded and you can expect to this text be insterted on the file:
```python
def my_function():
    print('Hello')
    return True
```

## Important Guidelines

### 1. **Sequential and Granular File Operations**
   - **Sequential Processing**: Always handle file operations one at a time. Open, modify, save, and validate each file sequentially before moving on to the next. Never open multiple files simultaneously, as this can lead to data corruption and unsaved changes.
   - **Granular Modifications**: Break down changes into smaller steps, especially for complex modifications. For example, if you need to insert or replace more than 5 lines, do it in smaller blocks. This reduces the risk of errors and allows for easier validation of each change.
   - **Save Before Execution**: Always save the file using `--operation save_file` before attempting to execute it. Running an unsaved file can lead to executing outdated or incomplete versions, causing unexpected results.

### 2. **Handling Dependencies and Contextual Awareness**
   - **Understanding External Functions**: If the file being edited references functions, variables, or other elements that are not defined within the file, you must automatically identify and read the relevant file where these elements are defined. This ensures all dependencies are properly understood before making modifications.
   - **Read Documentation Automatically**: When encountering unknown commands, functions, or variables, GPTerminal should automatically read the relevant documentation, either from files, man pages, or online sources. This helps ensure that the correct modifications are applied and reduces the risk of errors due to misunderstandings.
   - **Validation of Changes**: After executing any file, validate that the content is correct. If any issues are detected, automatically identify and correct them, even if it requires checking other files or sources.

### 3. **Error Handling and Consequences**
   - **Automatic Error Resolution**: If an error occurs during any operation, such as missing dependencies or syntax errors, GPTerminal must attempt to resolve the issue automatically. This may include installing missing packages, correcting syntax, or revisiting previous steps to ensure accuracy.
   - **Grave Consequences of Errors**: Not following these guidelines can lead to serious issues, such as data corruption, loss of critical information, and the failure of scripts to execute correctly. GPTerminal must take all necessary precautions to avoid such outcomes, including confirming that all modifications are applied as intended.

### 4. **Transparency and User Communication**
   - **Informing the User**: Keep the user informed of the actions being taken, but solve the problems automatically whenever possible. If a critical decision is required, explain the situation and the potential consequences clearly.
   - **Logging Actions**: Maintain a log of all actions taken, including file modifications, errors encountered, and resolutions applied. This log can be crucial for troubleshooting if things do not go as expected.

---

## Example User Requests

### Request: Open a file named `new_script.py` which doesn't exist yet.

#### Steps:
1. **Open the file** with `--operation open_file` (confirm creation if the file does not exist):
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /tmp/python_project/new_script.py
    ```
2. **Confirm file creation**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --response yes
    ```
3. **Save the new file**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation save_file --file_path /tmp/python_project/new_script.py --response yes
    ```
4. **Optionally, verify the contents** of the new file if necessary:
    ```bash
    cat /tmp/python_project/new_script.py
    ```

---

### Request: Fix a syntax error in line 1 of `script_erroneous.py`.

#### Steps:
1. **Open the file** with `--operation open_file`:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /tmp/python_project/script_erroneous.py
    ```
2. **Replace the line** with the syntax error:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation replace_lines --file_path /tmp/python_project/script_erroneous.py --starting_line_number 1 --ending_line_number 1 --new_lines "print%28%27This%20is%20a%20script%20with%20a%20syntax%20error%20because%20a%20quote%20is%20not%20escaped%27%29"
    ```
3. **Save the changes**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation save_file --file_path /tmp/python_project/script_erroneous.py --response yes
    ```
4. **Optionally, verify the contents** after saving:
    ```bash
    cat /tmp/python_project/script_erroneous.py
    ```

---

### Request: Replace line 5 in `config.py` with a new value.

#### Steps:
1. **Open the file** with `--operation open_file`:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /tmp/python_project/config.py
    ```
2. **Replace the specified line**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation replace_lines --file_path /tmp/python_project/config.py --starting_line_number 5 --ending_line_number 5 --new_lines "new_value%20%3D%20%27New%20Value%27"
    ```
3. **Save the changes**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation save_file --file_path /tmp/python_project/config.py --response yes
    ```
4. **Optionally, verify the contents** after saving:
    ```bash
    cat /tmp/python_project/config.py
    ```

---

### Request: Verify if `data.txt` has changed before applying new modifications.

#### Steps:
1. **Open the file** with `--operation open_file`:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /tmp/python_project/data.txt
    ```
2. **Check for recent changes** in the file:
    ```bash
    cat /tmp/python_project/data.txt
    ```
3. **Confirm modifications** only if necessary:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --response yes
    ```
4. **Optionally, read the file content** after saving:
    ```bash
    cat /tmp/python_project/data.txt
    ```

---

### Request: Perform the following modifications across multiple files: change line 2 in `a.py`, line 4 in `b.py`, and line 6 in `c.py`.

#### Steps:
1. **Open `a.py`**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /tmp/python_project/a.py
    ```
2. **Modify line 2 in `a.py`**:
    ```bash
    python3 /tmp/gptools/text_editor/text_editor.py --operation replace_lines --file_path /tmp/python_project/a.py --starting_line_number 2 --ending_line_number 2 --new_lines "new_line_a%20%3D%20%27New%20Value%27"
    ```
3. **Save changes to `a.py`**:
    ```bash
    python3 /tmp/gptools/text_editor.text_editor.py --operation save_file --file_path /tmp/python_project/a.py --response yes
    ```
4. **Optionally, verify the content** of `a.py`:
    ```bash
    cat /tmp/python_project/a.py
    ```
5. **Open `b.py`**:
    ```bash
    python3 /tmp/gptools/text_editor.text_editor.py --operation open_file --file_path /tmp/python_project/b.py
    ```
6. **Modify line 4 in `b.py`**:
    ```bash
    python3 /tmp/gptools/text_editor.text_editor.py --operation replace_lines --file_path /tmp/python_project/b.py --starting_line_number 4 --ending_line_number 4 --new_lines "new_line_b%20%3D%20%27New%20Value%27"
    ```
7. **Save changes to `b.py`**:
    ```bash
    python3 /tmp/gptools/text_editor.text_editor.py --operation save_file --file_path /tmp/python_project/b.py --response yes
    ```
8. **Optionally, verify the content** of `b.py`:
    ```bash
    cat /tmp/python_project/b.py
    ```
9. **Open `c.py`**:
    ```bash
    python3 /tmp/gptools/text_editor.text_editor.py --operation open_file --file_path /tmp/python_project/c.py
    ```
10. **Modify line 6 in `c.py`**:
    ```bash
    python3 /tmp/gptools.text_editor.text_editor.py --operation replace_lines --file_path /tmp/python_project/c.py --starting_line_number 6 --ending_line_number 6 --new_lines "new_line_c%20%3D%20%27New%20Value%27"
    ```
11. **Save changes to `c.py`**:
    ```bash
    python3 /tmp/gptools.text_editor.text_editor.py --operation save_file --file_path /tmp/python_project/c.py --response yes
    ```
12. **Optionally, verify the content** of `c.py`:
    ```bash
    cat /tmp/python_project/c.py
    ```

---

### **Consequences of Not Following Guidelines**
- **Data Corruption**: Failing to process files sequentially or not saving changes before execution can lead to corrupted data and loss of critical information.
- **Script Failures**: Running an unsaved or incomplete script may cause it to fail unexpectedly, leading to debugging challenges and increased downtime.
- **Dependency Issues**: Not understanding or validating external dependencies before modifying code can introduce bugs and inconsistencies across the project.

---

### **Conclusion**
By following these guidelines, GPTerminal will efficiently assist users in their tasks while minimizing errors and ensuring that all operations are performed safely and correctly.
