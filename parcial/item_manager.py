class ItemManager:
    def __init__(self, item_type):
        self.items = []  # Lista para almacenar los elementos
        self.item_type = item_type  # Tipo de elemento (por ejemplo, "persona", "universidad", etc.)
        self.filename = f"{item_type}.txt"  # Nombre del archivo para guardar los elementos

        self.load_from_file()  # Cargar elementos desde el archivo cuando se crea un objeto ItemManager

    def create_item(self, name):
        if name:
            self.items.append(name)  # Agregar el nuevo elemento a la lista
            self._save_to_file()  # Guardar la lista actualizada en el archivo
            print(f"{self.item_type.capitalize()} '{name}' creado exitosamente.")
        else:
            print("Nombre inválido.")

    def list_items(self):
        if self.items:
            print(f"Lista de {self.item_type.capitalize()}s:")
            for item in self.items:
                print(f"- {item}")
        else:
            print(f"No se han agregado {self.item_type}s aún.")

    def delete_item(self, name):
        if name in self.items:
            self.items.remove(name)  # Eliminar el elemento de la lista
            self._save_to_file()  # Guardar la lista actualizada en el archivo
            print(f"{self.item_type.capitalize()} '{name}' eliminado exitosamente.")
        else:
            print(f"{self.item_type.capitalize()} '{name}' no encontrado.")

    def _save_to_file(self):
        with open(self.filename, 'w') as f:
            for item in self.items:
                f.write(item + '\n')  # Escribir cada elemento en una línea separada en el archivo

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.items = [line.strip() for line in f.readlines()]  # Cargar elementos desde el archivo
        except FileNotFoundError:
            pass  # Manejar la excepción si el archivo no existe

def menu_handler(manager):
    while True:
        print(f"""
{manager.item_type.capitalize()} MENÚ

1. Crear {manager.item_type}
2. Listar {manager.item_type}s
3. Eliminar {manager.item_type}
4. Volver
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            name = input(f"Ingrese el nombre de la {manager.item_type}: ")
            manager.create_item(name)
        elif choice == '2':
            manager.list_items()
        elif choice == '3':
            name = input(f"Ingrese el nombre de la {manager.item_type} a eliminar: ")
            manager.delete_item(name)
        elif choice == '4':
            break
        else:
            print("Opción inválida. Por favor seleccione nuevamente.")