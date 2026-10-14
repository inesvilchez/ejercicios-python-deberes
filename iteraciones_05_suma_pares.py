'''
Algoritmo: Suma de pares entre 1 y n
ENTRADAS: n
SALIDA: suma

bloque de desarrollo
contador = 1
suma = 0
MIENTRAS contador <= n:
    SI contador % 2 == 0:
        suma = suma + contador
    FIN SI
    contador = contador + 1
FIN MIENTRAS
DEVOLVER: suma
'''
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
