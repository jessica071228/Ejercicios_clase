#Cadena = secuencia de caracteres
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")

print(f"Hola {nombre} {apellidos}, mucho gusto!")

lugar = input("ingresa el lugar de origen: ")
tiempo = int(input("ingresa el tiempo que has vivido en ese lugar: "))

#concatenacion
descripcion = "No conozco " + lugar + " seria bonito visitarlo porque has vivido " + str(tiempo) + " anios ahi"
print("nombre: " + nombre)
print("apellidos: " + apellidos)
print(descripcion)

print(nombre[0])
print(nombre[1])
print(nombre[2])

tamanio = len(nombre)
print("El tamanio del nombre es de: " + str(tamanio) + " letras")
print(nombre[tamanio-1])
print(nombre[0 : 3])
print(nombre[3 : len(nombre)])

for i in range(0 , len(nombre)):
    print(nombre[i], end=" - ")

for i in nombre:
    print(i, end=" - ")

for i in range(len(nombre)-1, -1, -1):
        print(nombre[i], end=" - ")
