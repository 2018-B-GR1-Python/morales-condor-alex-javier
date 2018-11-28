from collections import Counter
def leer_archivo(path):
    try:
        with open(path)as archivo_abierto:
            genero = []

            arreglo_lineas_archivo = archivo_abierto.readlines()
            for linea in arreglo_lineas_archivo:
                get_genero = linea.split(',')
                genero.append(get_genero[4])

            print(genero)
            genero.remove('Gender')
            print(Counter(genero).values())

    except Exception:
        print("No se pudo leer el archivo")

print("Registros Totales")
leer_archivo('./data/marathon_boston_results_2017.csv')
print("\n")

