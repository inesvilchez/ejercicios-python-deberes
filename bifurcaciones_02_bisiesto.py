# Algoritmo:
# Un año es bisiesto si:
# - Es divisible entre 4
# - Excepto si es divisible entre 100
# - A menos que también sea divisible entre 400
#
# Si cumple la regla → devolver True
# Si no → devolver False
def es_bisiesto(año):
    """Determina si un año es bisiesto."""
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False
print(es_bisiesto(2024)) 
print(es_bisiesto(1900))   
print(es_bisiesto(2000))  
