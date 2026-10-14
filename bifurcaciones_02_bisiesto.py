'''
Algoritmo: Año bisiesto
ENTRADAS: anio
SALIDA: es_bisiesto

bloque de desarrollo
SI (anio % 4 == 0 Y anio % 100 != 0) O (anio % 400 == 0):
    es_bisiesto = True
SINO:
    es_bisiesto = False
FIN SI
DEVOLVER: es_bisiesto
'''
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
