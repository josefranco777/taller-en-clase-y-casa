import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
class BarberiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Barbería")

        # Variables de usuario y contraseña
        self.usuario_correcto = "admin"
        self.clave_correcta = "12345"

        # Inicialización de las listas de datos
        self.cortes_disponibles = []
        self.clientes = []
        self.reservas = []
        self.ventas = 0

        # Ventana de inicio de sesión
        self.ventana_login()

    def ventana_login(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Inicio de Sesión")
        self.login_window.geometry("250x150")

        tk.Label(self.login_window, text="Usuario:").pack()
        self.usuario_entry = tk.Entry(self.login_window)
        self.usuario_entry.pack()

        tk.Label(self.login_window, text="Contraseña:").pack()
        self.clave_entry = tk.Entry(self.login_window, show="*")
        self.clave_entry.pack()

        tk.Button(self.login_window, text="Iniciar Sesión", command=self.verificar_login).pack()

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        clave = self.clave_entry.get()

        if usuario == self.usuario_correcto and clave == self.clave_correcta:
            self.login_window.destroy()
            self.crear_interfaz()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            image = Image.open("barbershop.jpg")
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.login_window, image=photo)
        bg_label.image = photo
        bg_label.pack()

    def crear_interfaz(self):
        # Etiquetas
        ttk.Label(self.root, text="Cortes Disponibles:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.root, text="Clientes Registrados:").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(self.root, text="Reservas:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        ttk.Label(self.root, text="Ventas Totales:").grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Listas
        self.cortes_listbox = tk.Listbox(self.root, width=25, height=15)
        self.cortes_listbox.grid(row=1, column=0, padx=5, pady=5)

        self.clientes_listbox = tk.Listbox(self.root, width=25, height=15)
        self.clientes_listbox.grid(row=1, column=1, padx=5, pady=5)

        self.reservas_listbox = tk.Listbox(self.root, width=40, height=15)
        self.reservas_listbox.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

        # Ventas
        self.ventas_label = ttk.Label(self.root, text="$0")
        self.ventas_label.grid(row=1, column=3, padx=5, pady=5)

        # Botones CRUD
        ttk.Button(self.root, text="Agregar Corte", command=self.agregar_corte).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Button(self.root, text="Listar Cortes", command=self.listar_cortes).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Button(self.root, text="Eliminar Corte", command=self.eliminar_corte).grid(row=2, column=0, padx=5, pady=5)

        ttk.Button(self.root, text="Agregar Cliente", command=self.agregar_cliente).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Button(self.root, text="Listar Clientes", command=self.listar_clientes).grid(row=2, column=1, padx=5, pady=5, sticky="e")
        ttk.Button(self.root, text="Eliminar Cliente", command=self.eliminar_cliente).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.root, text="Hacer Reserva", command=self.hacer_reserva).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.root, text="Listar Reservas", command=self.listar_reservas).grid(row=2, column=2, padx=5, pady=5, sticky="e")
        ttk.Button(self.root, text="Eliminar Reserva", command=self.eliminar_reserva).grid(row=2, column=2, padx=5, pady=5)

        ttk.Button(self.root, text="Registrar Venta", command=self.registrar_venta).grid(row=2, column=3, padx=5, pady=5)

    # Métodos CRUD para cortes
    def agregar_corte(self):
        corte = simpledialog.askstring("Agregar Corte", "Ingrese el nombre del corte:")
        if corte:
            self.cortes_listbox.insert(tk.END, corte)
            self.cortes_disponibles.append(corte)

    def listar_cortes(self):
        cortes = "\n".join(self.cortes_disponibles)
        messagebox.showinfo("Cortes Disponibles", cortes)

    def eliminar_corte(self):
        index = self.cortes_listbox.curselection()
        if index:
            self.cortes_listbox.delete(index)
            del self.cortes_disponibles[index[0]]

    # Métodos CRUD para clientes
    def agregar_cliente(self):
        cliente = simpledialog.askstring("Agregar Cliente", "Ingrese el nombre del cliente:")
        if cliente:
            self.clientes_listbox.insert(tk.END, cliente)
            self.clientes.append(cliente)

    def listar_clientes(self):
        clientes = "\n".join(self.clientes)
        messagebox.showinfo("Clientes Registrados", clientes)

    def eliminar_cliente(self):
        index = self.clientes_listbox.curselection()
        if index:
            self.clientes_listbox.delete(index)
            del self.clientes[index[0]]

    # Métodos CRUD para reservas
    def hacer_reserva(self):
        cliente = self.clientes_listbox.get(tk.ACTIVE)
        corte = self.cortes_listbox.get(tk.ACTIVE)
        fecha = simpledialog.askstring("Hacer Reserva", f"Ingrese la fecha para la reserva de '{cliente}' con el corte '{corte}':")
        if fecha:
            self.reservas_listbox.insert(tk.END, f"{cliente} - {corte} - {fecha}")
            self.reservas.append({'cliente': cliente, 'corte': corte, 'fecha': fecha})

    def listar_reservas(self):
        reservas_info = ""
        for reserva in self.reservas:
            reservas_info += f"Cliente: {reserva['cliente']}, Corte: {reserva['corte']}, Fecha: {reserva['fecha']}\n"
        messagebox.showinfo("Reservas", reservas_info)

    def eliminar_reserva(self):
        index = self.reservas_listbox.curselection()
        if index:
            self.reservas_listbox.delete(index)
            del self.reservas[index[0]]

    # Método para registrar ventas
    def registrar_venta(self):
        monto = simpledialog.askinteger("Registrar Venta", "Ingrese el monto de la venta:")
        if monto:
            self.ventas += monto
            self.ventas_label.config(text=f"${self.ventas}")

def main():
    root = tk.Tk()
    app = BarberiaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
