import tkinter as tk
from tkinter import messagebox
#jose franco 
def registrar():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    edad = edad_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    sexo = sexo_var.get()
    ciudad = ciudad_listbox.get(tk.ACTIVE)

    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showinfo("Información Registrada", mensaje)

ventana = tk.Tk()
ventana.geometry("400x500")
ventana.title("Formulario de Registro")

tk.Label(ventana, text="Nombre:").grid(row=0, column=1)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=2)

tk.Label(ventana, text="Apellido:").grid(row=1, column=1)
apellido_entry = tk.Entry(ventana)
apellido_entry.grid(row=1, column=2)

tk.Label(ventana, text="Edad:").grid(row=2, column=1)
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=2, column=2)

tk.Label(ventana, text="Dirección:").grid(row=3, column=1)
direccion_entry = tk.Entry(ventana)
direccion_entry.grid(row=3, column=2)

tk.Label(ventana, text="Teléfono:").grid(row=4, column=1)
telefono_entry = tk.Entry(ventana)
telefono_entry.grid(row=4, column=2)

tk.Label(ventana, text="Sexo:").grid(row=5, column=1)
sexo_var = tk.StringVar()
tk.Radiobutton(ventana, text="Masculino", variable=sexo_var, value="Masculino").grid(row=5, column=2)
tk.Radiobutton(ventana, text="Femenino", variable=sexo_var, value="Femenino").grid(row=5, column=3)

tk.Label(ventana, text="Ciudad:").grid(row=6, column=1)
ciudad_listbox = tk.Listbox(ventana, selectmode=tk.SINGLE)
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
for ciudad in ciudades:
    ciudad_listbox.insert(tk.END, ciudad)
ciudad_listbox.grid(row=6, column=2)

tk.Button(ventana, text="Registrar", command=registrar).grid(row=7, column=2, columnspan=2)

ventana.mainloop()
