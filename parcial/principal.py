from item_manager import ItemManager, menu_handler

def main_menu():
    managers = {
        "people": ItemManager("persona"),  # Crear un ItemManager para cada tipo de elemento
        "universities": ItemManager("universidad"),
        "grades": ItemManager("calificación"),
        "subjects": ItemManager("asignatura")
    }

    for manager in managers.values():
        manager.load_from_file()  # Cargar datos desde el archivo para cada tipo de elemento

    while True:
        print("""
MENÚ PRINCIPAL

1. Personas
2. Universidades
3. Calificaciones
4. Asignaturas
5. Salir
""")
        choice = input("Seleccione una opción: ")
        if choice in ['1', '2', '3', '4']:
            selected_manager = managers[list(managers.keys())[int(choice) - 1]]
            menu_handler(selected_manager)
        elif choice == '5':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor seleccione nuevamente.")

if __name__ == "__main__":
    main_menu()