from clientes import *

# dato = Cliente(359932, "Sergio", 23, 32321)
# print(dato.getDpi())
# print(dato.getNombre())
# print(dato.getEdad())
# print(dato.getNit())

# print("")
# dato.setNombre("Eduardo")
# print(dato.getDpi())
# print(dato.getNombre())
# print(dato.getEdad())
# print(dato.getNit())

# dpi = 323323
# nombre = "Eduardo"
# edad = 31
# nit = 31212

# dato = Cliente(dpi, nombre, edad, nit)
# print(dato.getDpi())
# print(dato.getNombre())
# print(dato.getEdad())
# print(dato.getNit())


# print("Ingrese los datos correspondientes")
# dpi = int(input("Ingrese su dpi: "))
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# nit = int(input("Ingrese su nit: "))

# dato = Cliente(dpi, nombre, edad, nit)

# print("\nDatos")
# print(dato.getDpi())
# print(dato.getNombre())
# print(dato.getEdad())
# print(dato.getNit())

listaClientes = []
opcion = 1

#Primer Cliente
dpi = 3532332
nombre = "Estuardo"
edad = 32
nit = 3231332

dato = Cliente(dpi, nombre, edad, nit)
listaClientes.append(dato)

#Segundo Cliente
dpi = 3452344
nombre = "Sandra"
edad = 18
nit = 432344

dato = Cliente(dpi, nombre, edad, nit)
listaClientes.append(dato)

print("\nListado de clientes")

for i in listaClientes:
    
    print("\nDpi: " + str(i.getDpi()))
    print("Nombre: " + str(i.getNombre()))
    print("Edad: " + str(i.getEdad()))
    print("Nit: " + str(i.getNit()))






