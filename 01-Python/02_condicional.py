# truthy
# Falsy

if True:
    print("Es verdad")
else:
    print("No es verdad")

nombre = "Alex"

if nombre: #Truthy
    print("Si")
else:
    print("No")

if 0: #Falsy
    print("Si")
else:
    print("No")

if 1 == 1: #Truthy
    print("Si")
else:
    print("No")

if not None: #Truthy
    print("Si")
else:
    print("No")

if 1 and 0:  # Truthy
    print("Si")
else:
    print("No")

if "a,b".split(","): #Truthy
    print("Si")
else:
    print("No")