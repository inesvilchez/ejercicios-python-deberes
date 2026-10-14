'''
Algoritmo: El mayor de tres números
ENTRADAS: a, b, c
SALIDA: mayor

bloque de desarrollo
SI a >= b Y a >= c:
    mayor = a
SINO SI b >= a Y b >= c:
    mayor = b
SINO:
    mayor = c
FIN SI
DEVOLVER: mayor
'''
def mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números sin usar max()."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(mayor_de_tres(4, 9, 2))  
print(mayor_de_tres(7, 7, 3))  
print(mayor_de_tres(10, 1, 10)) 
