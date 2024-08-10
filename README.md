# GPTools Repository Documentation

## Overview
Este repositorio contiene dos scripts útiles para manipular archivos de texto, mostrando su contenido con números de línea y modificando líneas específicas.

## Scripts

### 1. readFileWithLineNumbers.py
**Descripción**: Este script muestra el contenido de un archivo de texto con los números de línea correspondientes.

**Uso**:
```bash
python3 readFileWithLineNumbers.py <ruta_del_archivo>
```

**Ejemplo**:
```bash
python3 readFileWithLineNumbers.py archivo.txt
```

### 2. modifyLinesInFile.py
**Descripción**: Este script modifica o agrega líneas en un archivo de texto. Recibe la ruta del archivo, el rango de líneas a modificar, y el contenido de cada línea entre comillas.

**Uso**:
```bash
python3 modifyLinesInFile.py <ruta_del_archivo> <línea_inicial> <línea_final> "<contenido_de_línea_1>" "<contenido_de_línea_2>"
```

**Ejemplo**:
```bash
python3 modifyLinesInFile.py archivo.txt 1 3 "import os" "import requests" "api_key = os.getenv(OPENAI_API_KEY)"
```

Este ejemplo sobrescribirá las líneas 1 a 3 en `archivo.txt` con el contenido especificado.

## Requerimientos
- Python 3.x
- Ninguna dependencia externa

## Contribuciones
Las contribuciones a este repositorio son bienvenidas. Si deseas mejorar alguno de los scripts o agregar nuevas funcionalidades, no dudes en hacer un fork y enviar un pull request.

