'''
Algoritmo: Categoría de envío según el peso
ENTRADAS: peso_kg
SALIDA: categoria

bloque de desarrollo
SI peso_kg <= 1:
    categoria = "Sobre"
SINO SI peso_kg <= 5:
    categoria = "Paquete pequeño"
SINO SI peso_kg <= 20:
    categoria = "Paquete grande"
SINO:
    categoria = "Voluminoso"
FIN SI
DEVOLVER: categoria
'''
def categoria_envio(peso_kg):
    """Clasifica un envío según su peso en kilos."""
    if peso_kg <= 1:
        return "Sobre"
    elif peso_kg <= 5:
        return "Paquete pequeño"
    elif peso_kg <= 20:
        return "Paquete grande"
    else:
        return "Voluminoso"
print(categoria_envio(0.5))
print(categoria_envio(15))  
print(categoria_envio(30)) 
