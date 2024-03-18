
while True:
    # Imprimir el menú
    print("Menu:")
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Selecciona una opcion: ")
    
    # Verificar la opción seleccionada y mostrar el mensaje correspondiente
    if opcion == "1":
        print("Hola, has presionado la opcion Personas")
    elif opcion == "2":
        print("Hola, has presionado la opcion Vehiculos")
    elif opcion == "3":
        print("Hola, has presionado la opcion Universidades")
    elif opcion == "4":
        print("Hola, has presionado la opcion Notas")
    elif opcion == "5":
        print("Saliendo del programa...")
        break  # Salir del bucle while
    else:
        print("Opcion no valida. Por favor, selecciona una opcion del 1 al 5.")
 