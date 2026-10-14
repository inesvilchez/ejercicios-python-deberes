'''
Algoritmo: Suma recursiva de una lista
ENTRADAS: numeros
SALIDA: suma

bloque de desarrollo
SI longitud(numeros) == 0:
    suma = 0
SINO:
    suma = primer_elemento(numeros) + suma_lista(resto_de_numeros)
FIN SI
DEVOLVER: suma
'''
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
