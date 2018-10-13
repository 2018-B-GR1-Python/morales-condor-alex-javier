import sys, traceback

alex = {
    "nombre": "Alex"
}

arregloNumeros = [1,2]

try:
    arregloNumeros["1"] = 0
except KeyError:  # For Keys
    print("Error in key")
except TypeError as type:  # For Types
    print("Error in types")
    print(type)
    print(f"Linea del error: {type.__traceback__.tb_lineno}")

except Exception as err:
    print("Error in error")
    print(err.__traceback__)