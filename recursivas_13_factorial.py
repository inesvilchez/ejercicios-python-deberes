'''
Algoritmo: Factorial recursivo
ENTRADAS: n
SALIDA: resultado

bloque de desarrollo
SI n == 0:
    resultado = 1
SINO:
    resultado = n * factorial_recursivo(n - 1)
FIN SI
DEVOLVER: resultado
'''
def factorial_recursivo(n):
    """Calcula n! llamándose a sí misma (versión recursiva)."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
print(factorial_recursivo(5))
print(factorial_recursivo(0)) 
print(factorial_recursivo(7))  
