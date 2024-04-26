import tkinter as tk
from tkinter import messagebox

# Función para el botón
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Has hecho clic en el botón!")

# Crear ventana
ventana = tk.Tk()
ventana.title("Aplicación con Widgets")

# Etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, soy franco!")
etiqueta.pack()

# Botón
boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack()

# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Cuadro de texto
cuadro_texto = tk.Text(ventana)
cuadro_texto.pack()

# Checkbutton
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(ventana, text="Aceptar los términos y condiciones", variable=checkbutton_var)
checkbutton.pack()

# Radiobutton
radio_var = tk.StringVar()
radio_var.set("Opción 1")
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=radio_var, value="Opción 1")
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=radio_var, value="Opción 2")
radio1.pack()
radio2.pack()

# Lista desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3"]
lista_desplegable = tk.OptionMenu(ventana, radio_var, *opciones)
lista_desplegable.pack()

# Ejecutar la ventana
ventana.mainloop()

 


