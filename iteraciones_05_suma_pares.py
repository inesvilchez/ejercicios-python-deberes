# Algoritmo:
# Crear una variable suma = 0
# Recorrer todos los números desde 1 hasta n
# Si el número es par (numero % 2 == 0)
#     añadirlo a suma
# Al final devolver suma
def suma_pares(n):
    """Suma los números pares entre 1 y n."""
    suma = 0
    for numero in range(1, n + 1):
        if numero % 2 == 0:
            suma += numero
    return suma
print(suma_pares(10)) 
print(suma_pares(1))  
print(suma_pares(8))  
