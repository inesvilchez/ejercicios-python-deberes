# Algoritmo:
# Si peso <= 1 → "Sobre"
# Si peso > 1 y <= 5 → "Paquete pequeño"
# Si peso > 5 y <= 20 → "Paquete grande"
# Si peso > 20 → "Voluminoso"
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
