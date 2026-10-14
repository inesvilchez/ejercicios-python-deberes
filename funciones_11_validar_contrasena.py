'''
Algoritmo: Validar contraseña
ENTRADAS: contrasena, longitud_minima
SALIDA: es_valida

bloque de desarrollo
SI longitud(contrasena) >= longitud_minima:
    es_valida = True
SINO:
    es_valida = False
FIN SI
DEVOLVER: es_valida
'''
def validar_contrasena(contrasena, longitud_minima=8):
    """Comprueba si una contraseña alcanza la longitud mínima exigida."""
    if len(contrasena) >= longitud_minima:
        return True
    else:
        return False
print(validar_contrasena("abc123"))      
print(validar_contrasena("abc123", 5))    
print(validar_contrasena("superclave"))  
