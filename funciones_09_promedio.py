'''
Algoritmo: Promedio de una lista de números
ENTRADAS: numeros
SALIDA: promedio

bloque de desarrollo
suma_total = suma(numeros)
cantidad = longitud(numeros)
promedio = suma_total / cantidad
DEVOLVER: promedio
'''
def calcular_promedio(numeros):
    """Calcula la media aritmética de una lista de números."""
    suma = 0

    for numero in numeros:
        suma += numero

    promedio = suma / len(numeros)
    return promedio
print(calcular_promedio([4, 8, 6])) 
print(calcular_promedio([10, 20]))   
print(calcular_promedio([1]))        
