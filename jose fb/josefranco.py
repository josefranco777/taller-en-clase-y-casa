import tkinter as tk

# Función para el botón de ingresar
def ingresar():
    # Aquí puedes colocar la lógica para verificar el usuario y contraseña
    usuario = usuario_entry.get()
    clave = clave_entry.get()
    print("Usuario:", usuario)
    print("Contraseña:", clave)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("800x500")  # Tamaño de la ventana principal

# Crear los dos frames
frame_izquierda = tk.Frame(ventana, width=200, height=400, bg="white")
frame_izquierda.pack(side="left", fill="both", expand=True)

frame_derecha = tk.Frame(ventana, width=200, height=400, bg="lightgray")
frame_derecha.pack(side="right", fill="both", expand=True)

# Agregar el logo en el frame de la izquierda
logo_label = tk.Label(frame_izquierda, text="Logo", font=("CALIBRI", 16), bg="white")
logo_label.pack(pady=200)

# Agregar los elementos en el frame de la derecha
titulo_label = tk.Label(frame_derecha, text="Inicio de Sesión", font=("Arial", 18))
titulo_label.pack(pady=20)

usuario_label = tk.Label(frame_derecha, text="Usuario:", font=("Arial", 12))
usuario_label.pack()

usuario_entry = tk.Entry(frame_derecha, font=("Arial", 12))
usuario_entry.pack()

clave_label = tk.Label(frame_derecha, text="Contraseña:", font=("Arial", 12))
clave_label.pack()

clave_entry = tk.Entry(frame_derecha, show="*", font=("Arial", 12))  # El parámetro show="*" oculta los caracteres de la contraseña
clave_entry.pack()

boton_ingresar = tk.Button(frame_derecha, text="Ingresar", command=ingresar, font=("Arial", 12))
boton_ingresar.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()
