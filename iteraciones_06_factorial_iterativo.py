# Algoritmo:
# Si n es 0 → devolver 1 (porque 0! = 1)
# Crear una variable resultado = 1
# Recorrer los números desde 1 hasta n
#     multiplicar resultado por cada número
# Al final devolver resultado
def factorial_iterativo(n):
    """Calcula n! usando un bucle (versión iterativa)."""
    resultado = 1

    for numero in range(1, n + 1):
        resultado *= numero

    return resultado
print(factorial_iterativo(5)) 
print(factorial_iterativo(0)) 
print(factorial_iterativo(7)) 
