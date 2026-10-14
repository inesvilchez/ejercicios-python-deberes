'''
Algoritmo: Convertir a entero
ENTRADAS: texto
SALIDA: resultado

bloque de desarrollo
INTENTAR:
    resultado = convertir_a_entero(texto)
CAPTURAR ValueError:
    resultado = "Error: no es un número"
FIN INTENTAR
DEVOLVER: resultado
'''
def eliminar_duplicados(lista):
    """Devuelve una lista sin elementos duplicados."""
    sin_duplicados = list(set(lista))
    return sin_duplicados
print(eliminar_duplicados([1, 2, 2, 3, 3, 3]))   
print(eliminar_duplicados(["a", "b", "a"]))       
print(eliminar_duplicados([10, 10, 10, 10]))      
