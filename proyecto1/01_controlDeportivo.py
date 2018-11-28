def opcionMenu():                                               #Funcion para que la opcion del menu sea un int
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Escoja una opcion del menu: "))
            correcto = True
        except ValueError:
            print('Error, Opcion incorrecta')
    return num

def leer_archivo(path):
    try:
        with open(path)as archivo_abierto:
            arreglo_lineas_archivo = archivo_abierto.readlines()
            for linea in arreglo_lineas_archivo:
                print(linea)
    except Exception:
        print("No se pudo leer el archivo")

def agregar_a_archivo(path, *lineas_a_escribir):        #agrega un nuevo registro al final del archivo
    try:
        with open(path, 'a') as archivo_abierto:
            for linea in lineas_a_escribir:
                archivo_abierto.write("\n" + linea)
    except Exception:
        print("No se pudo leer el archivo")

def modificar_dato(ruta, filas, columna, nuevo_dato):   #modificar un dato seleccionando una id
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila].split('\t')
            columnas[columna] = nuevo_dato
            contenido[fila] = '\t'.join(columnas)
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)

def eliminar_registros(path, id_registro):          #elimina un registro usando la id del registro
    registros = []
    try:
        with open(path) as archivo_abierto:
            for registro in archivo_abierto:
                registros.append(registro)
    except Exception:
        print("No se pudo abrir el archivo")

    del registros[id_registro]

    actualizar_archivo = open(path, 'w')
    for i in range(0, len(registros)):
        actualizar_archivo.write(registros[i])
    actualizar_archivo.close()

salir = False
opcion = 0

while not salir:

    print("\tControl de Registros de Entrenamientos")
    print("1. Leer todos los registros")
    print("2. Crear un registro")
    print("3. Modificar un registro")
    print("4. Eliminar un registro")
    print("5. Salir")

    opcion = opcionMenu()

    if opcion == 1:
        print("Registros Totales")
        leer_archivo('./registros.txt')
        print("\n")
    elif opcion == 2:
        print("Crear un nuevo registro")
        registro = input("Ingrese un nuevo registro\n")
        agregar_a_archivo('./registros.txt', registro)
        #5  Victor Morales  61  M   1.74    68  10  58'45''
        print("\n")

    elif opcion == 3:
        print("Modificacion de los registros existentes")
        leer_archivo('./registros.txt')
        print("\n")
        #id = int(input("Ingrese la ID del registro a modificar: "))
        #nuevo_dato = int(input(f"Modifique el registro\n"))
        modificar_dato('./registros.txt', [4], 2, '28')
        print("Dato modificado")
        leer_archivo('./registros.txt')

    elif opcion == 4:
        print("Eliminacion de un registro")
        id_registro = int(input("Ingrese la id del registro a eliminar"))
        eliminar_registros('./registros.txt', id_registro)
    elif opcion == 5:
        salir = True
    else:
        print("Opcion Invalida")

print("Fin")