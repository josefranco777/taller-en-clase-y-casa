
# Crear un diccionario vacío llamado perro
perro = {}

# Añadir nombre, color, raza, patas y edad al diccionario perro
perro["nombre"] = "jose"
perro["color"] = "Marrón"
perro["raza"] = "Labrador"
perro["patas"] = 4
perro["edad"] = 3

# Crear un diccionario de estudiante y añadir información
estudiante = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "sexo": "Masculino",
    "edad": 20,
    "estado civil": "Soltero",
    "habilidades": ["Programación", "Inglés"],
    "país": "México",
    "ciudad": "Ciudad de México",
    "dirección": "Calle Principal #123"
}

# Obtener la longitud del diccionario del estudiante
longitud = len(estudiante)
print("Longitud del diccionario de estudiante:", longitud)

# Obtener el valor de las habilidades y comprobar el tipo de datos
habilidades = estudiante["habilidades"]
print("Habilidades:", habilidades)
print("Tipo de datos de las habilidades:", type(habilidades))

# Modificar los valores de las habilidades añadiendo una o dos habilidades
estudiante["habilidades"].extend(["Comunicación", "Organización"])

# Obtener las claves del diccionario como una lista
claves = list(estudiante.keys())
print("Claves del diccionario de estudiante:", claves)

# Obtener los valores del diccionario como una lista
valores = list(estudiante.values())
print("Valores del diccionario de estudiante:", valores)

# Cambiar el diccionario a una lista de tuplas utilizando el método items()
lista_tuplas = list(estudiante.items())
print("Diccionario convertido a lista de tuplas:")
for item in lista_tuplas:
    print(item)

# Eliminar uno de los elementos del diccionario
del estudiante["edad"]

# Borrar uno de los diccionarios
del estudiante
