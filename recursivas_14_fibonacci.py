# Algoritmo:
# Si n es 0 → devolver 0
# Si n es 1 → devolver 1
# Si n es mayor:
#     devolver fibonacci(n-1) + fibonacci(n-2)
# La función se llama a sí misma hasta llegar a los casos base
def fibonacci(n):
    """Devuelve el número Fibonacci en la posición n."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(0)) 
print(fibonacci(1))  
print(fibonacci(5))   
print(fibonacci(10))
