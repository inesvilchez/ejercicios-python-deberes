# Algoritmo:
# Si n es 0 → devolver 1 (caso base)
# Si n es mayor que 0:
#     devolver n * factorial_recursivo(n - 1)
# La función se llama a sí misma hasta llegar a 0
def factorial_recursivo(n):
    """Calcula n! llamándose a sí misma (versión recursiva)."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
print(factorial_recursivo(5))
print(factorial_recursivo(0)) 
print(factorial_recursivo(7))  
