# Algoritmo:
# Recibir un diccionario
# Crear un diccionario nuevo vacío
# Recorrer cada clave y valor del diccionario original:
#     en el nuevo diccionario, poner valor como clave y clave como valor
# Devolver el diccionario invertido
def invertir_diccionario(diccionario):
    """Devuelve un diccionario con claves y valores invertidos."""
    invertido = {}

    for clave, valor in diccionario.items():
        invertido[valor] = clave

    return invertido
print(invertir_diccionario({"a": 1, "b": 2, "c": 3}))  

print(invertir_diccionario({"x": "hola", "y": "adios"}))  

print(invertir_diccionario({10: "uno", 20: "dos"}))  
