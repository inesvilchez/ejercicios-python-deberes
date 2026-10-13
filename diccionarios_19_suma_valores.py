# Algoritmo:
# Recibir un diccionario con valores numéricos
# Crear suma = 0
# Recorrer cada valor del diccionario:
#     añadir el valor a suma
# Devolver suma
def sumar_valores(diccionario):
    """Suma todos los valores numéricos de un diccionario."""
    suma = 0

    for valor in diccionario.values():
        suma += valor

    return suma
print(sumar_valores({"a": 3, "b": 5, "c": 2}))  
print(sumar_valores({"x": 10, "y": 20}))        
print(sumar_valores({"uno": 1}))               
