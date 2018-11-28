"""def eliminar_registros(path, id_registro):
    registros = []
    try:
        archivo_abierto = open(path)
        for registro in archivo_abierto:
            registros.append(registro)
        archivo_abierto.close()
    except Exception:
        print("No se pudo abrir el archivo")

    del registros[id_registro]

    print(registros)
    actualizar_archivo = open(path, 'w')
    for i in range(0, len(registros)):
        actualizar_archivo.write(registros[i])
    actualizar_archivo.close()"""


def modificar_dato(ruta, filas, columna, nuevo_dato):
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila].split('\t')
            columnas[columna] = nuevo_dato
            contenido[fila] = '\t'.join(columnas)
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)

def leer_archivo(path):
    try:
        with open(path)as archivo_abierto:
            arreglo_lineas_archivo = archivo_abierto.readlines()
            for linea in arreglo_lineas_archivo:
                print(linea)
    except Exception:
        print("No se pudo leer el archivo")

#eliminar_registros('./registros.txt',4)
modificar_dato('./registros.txt',[4],2,'28')
leer_archivo('./registros.txt')