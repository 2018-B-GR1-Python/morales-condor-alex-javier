print ("Hola Mundo")
edad: int = 20
sueldo = 1.02
print(edad + int(sueldo))

nombre = "Alex"  #comentario
apellido = 'Morales'
apellido_materno = """Condor"""     #tres formas de escribir un string
print (nombre == apellido)
print (apellido == apellido_materno)
print (apellido_materno)

print (int(True))
print (int(False))
print (str(True))
print (str(False))

print ("alex morales".capitalize())
nombre_completo = "alex morales".split(" ")    # ["alex", "morales"}
print (nombre_completo[0].capitalize()+" "+nombre_completo[1].capitalize())
print ("Javier".isalpha())
print ("Javier10".isalpha())  # .isalpha  compara si todos son letras
print ("Javier10".isalnum())  # .isalnum  compara si son alphanumericos

print ("Mi nombre es {0} {1}".format(nombre_completo[0].capitalize(), "Morales"))
print (f"Mi nombre es {nombre_completo[0].capitalize()}")
print (r"Saltos de linea")   #raw
no_existe = None   #null
print (no_existe)