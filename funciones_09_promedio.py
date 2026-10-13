# Algoritmo:
# Recibir una lista de números
# Sumar todos los elementos
# Dividir la suma entre la cantidad de elementos
# Devolver el resultado
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
