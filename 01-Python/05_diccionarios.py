
alex = {
    "nombre": "Alex",
    'apellido': 'Morales',
    'edad': 27,
    'sueldo': 1.01,
    'hijos': [],
    'casado': False,
    'loteria': None,
    'mascota': {
        'nombre': 'Muffy',
        'edad': 4
    }
}
print(alex)

if(alex):
    print("Si")
else:
    print("NO")

print(alex["nombre"])
print(alex["mascota"]["nombre"])