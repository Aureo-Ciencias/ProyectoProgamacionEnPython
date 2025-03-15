# ProyectoProgamacionEnPython
 Proyecto Programacion en Python DGTIC-UNAM

## Sistema de Registro de Estudiantes para una Escuela

Este proyecto es un sistema de gestión para el registro de estudiantes en una escuela. Permite realizar las siguientes operaciones mediante una interfaz de línea de comandos:

- **Registrar nuevos estudiantes:** Añade un registro con datos como ID, nombre, apellido, edad y grado.
- **Eliminar registros de estudiantes:** Permite eliminar un registro existente tras confirmar la operación.
- **Actualizar información de estudiantes:** Modifica los datos de un registro seleccionado.
- **Mostrar todos los registros:** Visualiza la información de los estudiantes en formato tabular.
- **Buscar estudiantes:** Permite buscar registros por nombre o ID.
- **Generar reportes por grado:** Filtra y muestra los estudiantes de un grado específico.

### Características

- **Interfaz interactiva:** Utiliza menús para facilitar la navegación y el uso del sistema.
- **Almacenamiento en CSV:** Los registros se guardan en un archivo CSV, lo que facilita su edición y portabilidad.
- **Rutas dinámicas:** El sistema guarda el archivo CSV en una carpeta `datos` ubicada en el directorio padre de la carpeta `scripts`. Si la carpeta no existe, el programa la crea automáticamente.
- **Uso de bibliotecas estándar:** No se requieren dependencias externas, ya que el proyecto utiliza módulos estándar de Python (`csv` y `os`).

### Estructura del Proyecto

```plaintext
ProyectoProgamacionEnPython/
├── datos/
│   └── Registro_Escolar.csv   # Archivo de base de datos (se crea dinámicamente)
├── scripts/
│   └── main.py                # Código fuente del sistema
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
