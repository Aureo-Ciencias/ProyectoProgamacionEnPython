# Sistema de registro de estudiantes para una escuela
# Este programa permite registrar, eliminar, actualizar, buscar, mostrar y generar reportes de estudiantes almacenados en un archivo CSV.

# ---------------------------------------------
# Alumno: JORGE AUREO ARMAS CUELLAR
# ---------------------------------------------

# ---------------------------------------------
# IMPORTACIÓN DE BIBLIOTECAS
# ---------------------------------------------
import csv   # Para trabajar con archivos CSV.
import os    # Para interactuar con el sistema de archivos.

# ---------------------------------------------
# DEFINICIÓN DINÁMICA DE RUTAS
# ---------------------------------------------
# Obtener la ruta del directorio donde se encuentra el script actual.
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Determinar el directorio base (carpeta padre del directorio 'scripts').
directorio_base = os.path.dirname(directorio_script)

# Construir la ruta dinámica para la carpeta 'datos', que se encuentra en el mismo nivel que 'scripts'.
directorio_datos = os.path.join(directorio_base, "datos")

# Crear la carpeta 'datos' si no existe.
if not os.path.exists(directorio_datos):
    os.makedirs(directorio_datos)

# Nombre del archivo CSV que actuará como base de datos.
nombre_archivo = "Registro_Escolar.csv"

# Ruta completa donde se guardará la base de datos.
ruta_guardado = os.path.join(directorio_datos, nombre_archivo)

# ---------------------------------------------
# VARIABLES PRINCIPALES Y MENÚS
# ---------------------------------------------
# Definir los encabezados (campos) para el registro de estudiantes.
campos = ["id", "nombre", "apellido", "edad", "grado"]

# Menú principal
menu_principal = '''
--------------------------------------------
                MENÚ PRINCIPAL
--------------------------------------------
1) Registrar nuevo estudiante.
2) Eliminar registro de estudiante.
3) Actualizar información de estudiante.
4) Mostrar todos los estudiantes registrados.
5) Buscar estudiante por nombre o ID.
6) Generar reporte de estudiantes por grado.
7) Salir'''

# Menú para las opciones de búsqueda.
menu_busqueda = '''
--------------------------------------------
                MENÚ BÚSQUEDA
--------------------------------------------
1) Buscar estudiante por nombre.
2) Buscar estudiante por ID.
3) Salir'''

# Menú para eliminar registros.
menu_eliminar = '''
--------------------------------------------
                MENÚ ELIMINAR
--------------------------------------------
1) Eliminar registro de estudiante.
2) Salir'''

# Menú para actualizar registros.
menu_actualizar = '''
--------------------------------------------
                MENÚ ACTUALIZAR
--------------------------------------------
1) Actualizar registro de estudiante.
2) Salir'''

# Separador visual para la interfaz.
separador = "\n--------------------------------------------\n"

# Anchos para la representación tabular de los datos.
anchos = {
    "id": 5,           # Ancho de la columna 'id'
    "nombre": 20,      # Ancho de la columna 'nombre'
    "apellido": 20,    # Ancho de la columna 'apellido'
    "edad": 5,         # Ancho de la columna 'edad'
    "grado": 10        # Ancho de la columna 'grado'
}

# Datos de prueba para inicializar el sistema (se usarán si la BD está vacía).
estudiantes_test = [
    {"id": "1", "nombre": "Juan", "apellido": "Pérez", "edad": "15", "grado": "10"},
    {"id": "2", "nombre": "Ana", "apellido": "Martínez", "edad": "14", "grado": "9"},
    {"id": "3", "nombre": "Luis", "apellido": "García", "edad": "16", "grado": "11"}
]

# Si el archivo no existe, se crea con los encabezados.
if not os.path.exists(ruta_guardado):
    with open(ruta_guardado, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
    print(f"Archivo creado en: {ruta_guardado}")

# ---------------------------------------------
# FUNCIONES DEL SISTEMA
# ---------------------------------------------

def leer_BD(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos.
    """
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

def guardar_BD(ruta_archivo, registros, campos):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """
    try:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(registros)
        print(f"Base de datos guardada exitosamente en {ruta_archivo}.")
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")

def validar_unicidad(registros, campo, valor, registro_actual=None):
    """
    Verifica si un valor ya existe en un campo específico dentro de la base de datos.
    Si se proporciona 'registro_actual', se excluye de la validación.
    """
    for registro in registros:
        if registro[campo] == str(valor) and registro != registro_actual:
            return False
    return True

def entrada_numerica(mensaje="Tu opción: ", tipo=int):
    """
    Solicita una entrada numérica al usuario y valida su tipo.
    """
    while True:
        try:
            if tipo == int:
                return int(input(mensaje))
            elif tipo == float:
                return float(input(mensaje))
        except ValueError:
            print("Entrada inválida, introduce un valor numérico válido.")

def agregar_estudiante(registros):
    """
    Registra un nuevo estudiante con validación de ID único.
    """
    # Validar ID único
    while True:
        id_est = entrada_numerica("Introduce el identificador único del estudiante: ", int)
        if validar_unicidad(registros, "id", id_est):
            break
        else:
            print("El identificador ya existe. Introduce uno único.")
    nombre = input("Introduce el nombre del estudiante: ")
    apellido = input("Introduce el apellido del estudiante: ")
    edad = entrada_numerica("Introduce la edad del estudiante: ", int)
    grado = input("Introduce el grado del estudiante: ")
    nuevo_estudiante = {"id": str(id_est), "nombre": nombre, "apellido": apellido, "edad": str(edad), "grado": grado}
    registros.append(nuevo_estudiante)
    print("Estudiante registrado exitosamente.")

def Eliminar_estudiante(registros):
    """
    Permite eliminar el registro de un estudiante después de confirmar.
    """
    while True:
        print(menu_eliminar)
        if not registros:
            print("No hay registros de estudiantes para eliminar.")
            return
        opcion = entrada_numerica("Selecciona una opción (1 o 2): ", int)
        if opcion == 1:
            print("\nEstudiantes registrados:")
            for i, est in enumerate(registros):
                print(f"{i + 1}. ID: {est['id']}, Nombre: {est['nombre']} {est['apellido']}")
            indice = entrada_numerica("Introduce el número del estudiante a eliminar (Para salir sin borrar: 0): ", int) - 1
            if 0 <= indice < len(registros):
                confirmacion = entrada_numerica("¿Estás seguro de eliminar este registro? Introduce 1 para confirmar: ", int)
                if confirmacion == 1:
                    eliminado = registros.pop(indice)
                    print(f"Registro de {eliminado['nombre']} {eliminado['apellido']} eliminado exitosamente.")
                else:
                    print("Operación cancelada.")
            elif indice == -1:
                print("Saliendo")
            else:
                print("Número de estudiante no válido.")
        elif opcion == 2:
            print("Saliendo del menú de eliminación.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        input("Presiona Enter para continuar...")

def Actualizar_estudiante(registros):
    """
    Permite actualizar la información de un estudiante.
    """
    if not registros:
        print("No hay registros de estudiantes para actualizar.")
        return
    while True:
        print(menu_actualizar)
        opcion = entrada_numerica("Selecciona una opción (1 o 2): ", int)
        if opcion == 1:
            print("\nEstudiantes registrados:")
            for i, est in enumerate(registros):
                print(f"{i + 1}. ID: {est['id']}, Nombre: {est['nombre']} {est['apellido']}")
            indice = entrada_numerica("Introduce el número del estudiante que deseas actualizar: ", int) - 1
            if 0 <= indice < len(registros):
                est = registros[indice]
                print(f"\nRegistro seleccionado: {est}")
                while True:
                    nuevo_id = entrada_numerica(f"Introduce el nuevo ID (actual: {est['id']}): ", int) or int(est["id"])
                    if validar_unicidad(registros, "id", nuevo_id, est):
                        break
                    else:
                        print("El ID ya existe. Introduce uno único.")
                nuevo_nombre = input(f"Introduce el nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
                nuevo_apellido = input(f"Introduce el nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
                nueva_edad = entrada_numerica(f"Introduce la nueva edad (actual: {est['edad']}): ", int) or int(est['edad'])
                nuevo_grado = input(f"Introduce el nuevo grado (actual: {est['grado']}): ") or est["grado"]
                confirmacion = entrada_numerica("¿Estás seguro de actualizar este registro? Introduce 1 para confirmar: ", int)
                if confirmacion == 1:
                    est["id"] = str(nuevo_id)
                    est["nombre"] = nuevo_nombre
                    est["apellido"] = nuevo_apellido
                    est["edad"] = str(nueva_edad)
                    est["grado"] = nuevo_grado
                    print("Registro actualizado exitosamente.")
                else:
                    print("Actualización cancelada.")
            else:
                print("Número de estudiante no válido.")
        elif opcion == 2:
            print("Saliendo del menú de actualización.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
        input("Presiona Enter para continuar...")

def Mostrar_Estudiantes(registros):
    """
    Muestra todos los registros de estudiantes en formato tabular.
    """
    print(f"{'id':<{anchos['id']}} {'nombre':<{anchos['nombre']}} {'apellido':<{anchos['apellido']}} {'edad':<{anchos['edad']}} {'grado':<{anchos['grado']}}")
    print("-" * sum(anchos.values()))
    for est in registros:
        print(f"{est['id']:<{anchos['id']}} {est['nombre']:<{anchos['nombre']}} {est['apellido']:<{anchos['apellido']}} {est['edad']:<{anchos['edad']}} {est['grado']:<{anchos['grado']}}")

def Buscar_Estudiantes(registros):
    """
    Permite buscar estudiantes por nombre o ID.
    """
    while True:
        print(menu_busqueda)
        opcion = entrada_numerica("Tu opción: ", int)
        if opcion == 1:
            nombre_buscar = input("Introduce el nombre del estudiante: ")
            print(f"{'id':<{anchos['id']}} {'nombre':<{anchos['nombre']}} {'apellido':<{anchos['apellido']}} {'edad':<{anchos['edad']}} {'grado':<{anchos['grado']}}")
            print("-" * sum(anchos.values()))
            encontrado = False
            for est in registros:
                if est['nombre'] == nombre_buscar:
                    print(f"{est['id']:<{anchos['id']}} {est['nombre']:<{anchos['nombre']}} {est['apellido']:<{anchos['apellido']}} {est['edad']:<{anchos['edad']}} {est['grado']:<{anchos['grado']}}")
                    encontrado = True
            if not encontrado:
                print("Estudiante no encontrado.")
        elif opcion == 2:
            id_buscar = entrada_numerica("Introduce el ID del estudiante: ", int)
            print(f"{'id':<{anchos['id']}} {'nombre':<{anchos['nombre']}} {'apellido':<{anchos['apellido']}} {'edad':<{anchos['edad']}} {'grado':<{anchos['grado']}}")
            print("-" * sum(anchos.values()))
            encontrado = False
            for est in registros:
                if int(est['id']) == id_buscar:
                    print(f"{est['id']:<{anchos['id']}} {est['nombre']:<{anchos['nombre']}} {est['apellido']:<{anchos['apellido']}} {est['edad']:<{anchos['edad']}} {est['grado']:<{anchos['grado']}}")
                    encontrado = True
            if not encontrado:
                print("Estudiante no encontrado.")
        elif opcion == 3:
            break
        else:
            print("Entrada inválida, introduce una opción válida.")
        input("Presiona Enter para continuar...")

def Reporte_Estudiantes(registros):
    """
    Genera un reporte de estudiantes filtrando por grado.
    """
    grado_reporte = input("Introduce el grado para generar el reporte: ")
    print(f"{'id':<{anchos['id']}} {'nombre':<{anchos['nombre']}} {'apellido':<{anchos['apellido']}} {'edad':<{anchos['edad']}} {'grado':<{anchos['grado']}}")
    print("-" * sum(anchos.values()))
    encontrado = False
    for est in registros:
        if est['grado'] == grado_reporte:
            print(f"{est['id']:<{anchos['id']}} {est['nombre']:<{anchos['nombre']}} {est['apellido']:<{anchos['apellido']}} {est['edad']:<{anchos['edad']}} {est['grado']:<{anchos['grado']}}")
            encontrado = True
    if not encontrado:
        print("No se encontraron estudiantes en el grado especificado.")

# ---------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------
# Cargar la base de datos desde el archivo CSV.
Registro_Escolar = leer_BD(ruta_guardado)
if not Registro_Escolar:
    # Si la base de datos está vacía, se cargan los datos de prueba.
    Registro_Escolar.extend(estudiantes_test)

# Bucle principal del programa.
while True:
    print(menu_principal)
    opcion = entrada_numerica("Tu opción: ", int)
    
    if opcion == 1:
        print(separador + "Registrar nuevo estudiante" + separador)
        agregar_estudiante(Registro_Escolar)
    elif opcion == 2:
        print(separador + "Eliminar registro de estudiante" + separador)
        Eliminar_estudiante(Registro_Escolar)
    elif opcion == 3:
        print(separador + "Actualizar registro de estudiante" + separador)
        Actualizar_estudiante(Registro_Escolar)
    elif opcion == 4:
        print(separador + "Mostrar estudiantes" + separador)
        Mostrar_Estudiantes(Registro_Escolar)
    elif opcion == 5:
        print(separador + "Buscar estudiante" + separador)
        Buscar_Estudiantes(Registro_Escolar)
    elif opcion == 6:
        print(separador + "Reporte de estudiantes por grado" + separador)
        Reporte_Estudiantes(Registro_Escolar)
    elif opcion == 7:
        print("Hasta luego")
        guardar_BD(ruta_guardado, Registro_Escolar, campos)
        break
    else:
        print("Opción inválida, introduce una opción válida.")
    
    input("\nPresiona Enter para continuar...")
