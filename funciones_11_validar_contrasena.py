# Algoritmo:
# Recibir una contraseña y una longitud mínima (por defecto 8)
# Si la longitud de la contraseña es mayor o igual que la longitud mínima:
#     devolver True
# Si no:
#     devolver False
def validar_contrasena(contrasena, longitud_minima=8):
    """Comprueba si una contraseña alcanza la longitud mínima exigida."""
    if len(contrasena) >= longitud_minima:
        return True
    else:
        return False
print(validar_contrasena("abc123"))      
print(validar_contrasena("abc123", 5))    
print(validar_contrasena("superclave"))  
