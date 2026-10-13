# Algoritmo:
# Si la lista está vacía → devolver 0
# Si la lista tiene elementos:
#     devolver el primer elemento + suma_lista(resto de la lista)
# La función se llama a sí misma reduciendo la lista
def suma_lista(numeros):
    """Suma los elementos de una lista usando recursividad."""
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + suma_lista(numeros[1:])
print(suma_lista([1, 2, 3]))     
print(suma_lista([10, 5]))        
print(suma_lista([]))             
print(suma_lista([7, 3, 9, 1]))  
