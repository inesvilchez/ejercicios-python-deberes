# Algoritmo:
# Recibir una lista de números
# Crear una variable mayor = primer elemento
# Recorrer cada número de la lista:
#     Si el número es mayor que 'mayor':
#         actualizar 'mayor'
# Al final devolver 'mayor'
def mayor_en_lista(numeros):
    """Devuelve el número mayor dentro de una lista."""
    mayor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor
print(mayor_en_lista([3, 8, 2, 10, 5]))  
print(mayor_en_lista([1]))              
print(mayor_en_lista([-5, -2, -9]))      
