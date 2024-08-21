Documentación del Text Editor
Descripción General
Este documento proporciona instrucciones detalladas sobre cómo utilizar text_editor.py para crear y modificar archivos de texto de manera segura y eficiente.

Flujo de Trabajo Obligatorio
Abrir un Archivo:

Antes de realizar cualquier modificación, es obligatorio abrir el archivo utilizando la operación open_file. Esto asegura que todas las modificaciones se realicen sobre un archivo de scratch, lo que permite revisiones y previene la corrupción accidental del archivo original.
bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /path/to/file.py
Realizar Modificaciones:

Una vez abierto el archivo, utiliza las operaciones insert_lines, delete_lines y replace_lines para modificar el contenido. Es fundamental prestar atención a la indentación y a la correcta utilización de comillas, especialmente cuando se manejan strings o bloques de código anidados.
bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation insert_lines --file_path /path/to/file.py --starting_line_number 1 --new_lines "def mi_funcion():" "    print(\"Hola, mundo\")"
Revisar el Contenido:

Después de aplicar las modificaciones, revisa el contenido del archivo de scratch. Esta revisión es crucial para asegurar que las líneas se han insertado correctamente y que la sintaxis es válida. Esto ayuda a prevenir errores antes de guardar los cambios definitivos.
bash
Copiar código
# La revisión se realiza automáticamente en el editor antes de guardar.
Guardar Cambios:

Si estás satisfecho con las modificaciones, utiliza la operación save_file para guardar los cambios en el archivo original. Este paso cierra el archivo de scratch y finaliza el proceso de edición. Si se requieren más cambios, será necesario volver a abrir el archivo con open_file.
bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation save_file --file_path /path/to/file.py
Ejemplo Completo de Creación de un Script en Python
Paso 1: Abrir el archivo
Antes de hacer cualquier modificación, abre el archivo que deseas editar. Esto crea un archivo de scratch donde se aplicarán todas las modificaciones.

bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation open_file --file_path /path/to/file.py
Paso 2: Insertar o Modificar Líneas
Una vez que el archivo esté abierto, puedes insertar o modificar líneas. Asegúrate de que las líneas estén correctamente indentadas y que los caracteres especiales, como comillas dentro de strings, estén correctamente escapados.

Ejemplo de inserción de líneas:

bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation insert_lines --file_path /path/to/file.py --starting_line_number 1 --new_lines "def mi_funcion():" "    print(\"Hola, mundo\")"
Paso 3: Revisar el Contenido
Revisa el contenido del archivo de scratch para asegurarte de que todo esté en orden. Este paso es fundamental para evitar errores de sintaxis y asegurar que las modificaciones son las deseadas.

Paso 4: Guardar los Cambios
Finalmente, guarda los cambios si estás satisfecho con las modificaciones. Esto escribirá el contenido del archivo de scratch en el archivo original.

bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation save_file --file_path /path/to/file.py
Uso Correcto del Parámetro --new_lines
El parámetro --new_lines es crítico para la correcta inserción de líneas en un archivo. Aquí te explicamos cómo utilizarlo adecuadamente para evitar errores comunes.

Ejemplo Básico
Inserta una función simple en la primera línea de un archivo:

bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation insert_lines --file_path /path/to/file.py --starting_line_number 1 --new_lines "def mi_funcion():" "    print(\"Hola, mundo\")"
Ejemplo Avanzado: Inserción de Múltiples Líneas
Para insertar un bloque de código más complejo, como un condicional dentro de una función:

bash
Copiar código
python3 /tmp/gptools/text_editor/text_editor.py --operation insert_lines --file_path /path/to/file.py --starting_line_number 10 --new_lines "def saludo(persona):" "    if persona:" "        print(f\"Hola, {persona}\")" "    else:" "        print(\"Hola, mundo\")"
Consideraciones Importantes
Indentación: Cada línea que debe estar indentada necesita los espacios apropiados. Python es muy estricto con la indentación, por lo que cualquier error en este aspecto podría causar un fallo en la ejecución del script.
Uso de Comillas: Escapa correctamente las comillas dentro de los strings utilizando \" para evitar errores de sintaxis.
Separación de Líneas: Cada línea debe estar entre comillas dobles y separada por un espacio en el comando.
Multilínea: Cada línea de código a insertar debe estar definida por separado y en el orden correcto.
Errores Comunes a Evitar
Falta de Indentación: Asegúrate de que todas las líneas que deben estar indentadas lo estén. La falta de indentación puede hacer que el código sea sintácticamente incorrecto.
Escape Incorrecto de Caracteres: Asegúrate de escapar las comillas y otros caracteres especiales correctamente.
Formato Incorrecto: No omitas comillas o espacios necesarios en el comando, ya que esto puede resultar en errores durante la ejecución.
Consideraciones Finales
Verificar la Sintaxis: Antes de guardar los cambios, revisa cuidadosamente las líneas para asegurarte de que no hay errores de sintaxis.
Evitar Errores en la Inserción de Líneas: Sigue las prácticas recomendadas para pasar correctamente las líneas al comando --new_lines.
