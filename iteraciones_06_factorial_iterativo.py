'''
Algoritmo: Factorial iterativo
ENTRADAS: n
SALIDA: resultado

bloque de desarrollo
resultado = 1
contador = 1
MIENTRAS contador <= n:
    resultado = resultado * contador
    contador = contador + 1
FIN MIENTRAS
DEVOLVER: resultado
'''
def factorial_iterativo(n):
    """Calcula n! usando un bucle (versión iterativa)."""
    resultado = 1

    for numero in range(1, n + 1):
        resultado *= numero

    return resultado
print(factorial_iterativo(5)) 
print(factorial_iterativo(0)) 
print(factorial_iterativo(7)) 
