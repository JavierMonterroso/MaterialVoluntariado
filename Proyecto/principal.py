from usuario import *

acceso = True
listaUsuario = []

while acceso:
    print("\nBienvenido")
    print("1. Crear una cuenta bancaria")
    print("2. Ver clientes")
    print("3. Limpiar el sistema")
    print("4. Salir")
    opcion = int(input("Ingrese su elección: "))

    if opcion == 1:
        print("\nIngrese los datos del cliente")
        dpi = int(input("Ingrese el DPI: "))
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        usuario = Usuario(dpi, nombre, edad)
        listaUsuario.append(usuario)
        print("\nSe ha creado la cuenta bancaria con éxito")

    elif opcion == 2:

        if listaUsuario != []:
            print("\nVer usuarios")
            contador = 0
            for i in listaUsuario:
                contador = contador + 1
                print("\nUsuario " + str(contador))
                print("DPI: " + str(i.getDpi()))
                print("Nombre: " + str(i.getNombre()))
                print("Edad: " +str(i.getEdad()))
        
        else:
            print("\nEl sistema no tiene usuarios")
    
    elif opcion == 3:
        print("\nEl sistema se ha limpiado con éxito")
        listaUsuario.clear()

    elif opcion == 4:
        acceso = False
        print("\nRegrese pronto")
        
