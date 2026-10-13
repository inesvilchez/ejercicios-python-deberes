# Algoritmo:
# Si a es mayor que b y mayor que c → devolver a
# Si b es mayor que a y mayor que c → devolver b
# Si no → devolver c
#
# Nota: si hay empates, devolver cualquiera de los mayores
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
