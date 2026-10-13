# Algoritmo:
# Recibir una lista con posibles duplicados
# Convertir la lista a un conjunto (set) para eliminar duplicados
# Convertir el conjunto de nuevo a lista
# Devolver la lista sin duplicados
def eliminar_duplicados(lista):
    """Devuelve una lista sin elementos duplicados."""
    sin_duplicados = list(set(lista))
    return sin_duplicados
print(eliminar_duplicados([1, 2, 2, 3, 3, 3]))   
print(eliminar_duplicados(["a", "b", "a"]))       
print(eliminar_duplicados([10, 10, 10, 10]))      
