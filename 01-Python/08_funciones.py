def sumar_dos_numeros(num_uno, num_dos):
    if (num_uno == 1):
        return "Hola"
    return num_uno + num_dos

print(sumar_dos_numeros(3, 2))


def imprimir_universidad(nombre_universidad="EPN"):
    print(f"{nombre_universidad} es lo maximo")


imprimir_universidad()
imprimir_universidad("Salford")


def guardar_carros(posicion, placa, usuario, tip, color):
    print(f"Guardamos en {posicion} el auto con placa {placa}"
          f"del usario {usuario}")
    if (color):
        print(f"El color del carro es {color}")
    if (tip):
        print(f"El tipo del carro es {tip}")

guardar_carros(1, "123-ABC", "Alex",color="Amarillo", tip=25.53)

## primero se mandan los parametros normales
## luego los valores por defecto


def sumar_numeros(resta, *numeros, valor_inicial=0):
    for numero in numeros:
        valor_inicial = valor_inicial + numero
    print(resta)
    print(numeros)
    print(valor_inicial)

resultado = sumar_numeros(1,1,2,3,4,5,6,7,8,9,0,1,1,2,3,4,5,6,7,8,4, valor_inicial=10)
print(resultado)

def imprimir_nombre(**kwargs):
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          f"{kwargs['apellido_paterno']} {kwargs['apellido_materno']}")

imprimir_nombre(primer_nombre="Alex",
                segundo_nombre="Javier",
                apellido_paterno="Morales",
                apellido_materno="Condor")


##numero = input("Ingrese un numero: ")
##print(float(numero) + 12.2 + 1)

##opcional = input("Desea para con su orden, ")

#numeros = input("Ingrese numeros ")

#Recibir numeros separados por comas y hacer un split
#1) recibir los numeros -> validar que sean numeros y que esten separados por comas
#  1.1) separar coma
#  1.2) que sean numeros
#2) Convertir los elementos de la tupla en float
#3)


def calculadora(numero_uno, numero_dos, operacion='suma'):
    def sumar_dos_numeros():
        return numero_uno + numero_dos
    def restar_dos_numeros():
        return numero_uno-numero_dos
    def multiplicar_dos_numeros():
        return numero_uno*numero_dos
    def dividir_dos_numeros():
        return numero_uno/numero_dos

    if operacion == "suma":
        print(sumar_dos_numeros())
    elif operacion == "resta":
        print(restar_dos_numeros())
    elif operacion == "multiplicacion":
        print(multiplicar_dos_numeros())
    else:
        print(dividir_dos_numeros())

calculadora(5,3,operacion='asdf')


def leer_archivos():
    try:
        print('Si se pudo leer el archivo')
    except Exception:
        print("No se pudo leer el archivo")
