# Algoritmo:
# Recibir una lista y un elemento a buscar
# Crear contador = 0
# Recorrer cada elemento de la lista:
#     Si el elemento es igual al buscado:
#         sumar 1 al contador
# Devolver contador
def contar_elemento(lista, elemento):
    """Cuenta cuántas veces aparece un elemento en una lista."""
    contador = 0

    for item in lista:
        if item == elemento:
            contador += 1

    return contador
print(contar_elemento([1, 2, 3, 2, 2], 2))  
print(contar_elemento(["a", "b", "a"], "a")) 
print(contar_elemento([10, 20, 30], 5))     
