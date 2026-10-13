# Algoritmo:
# Convertir la palabra a minúsculas
# Crear contador = 0
# Para cada letra en la palabra:
#     Si la letra está en "aeiou":
#         sumar 1 al contador
# Devolver contador
def contar_vocales(palabra):
    """Cuenta las vocales de una palabra, sin distinguir mayúsculas."""
    palabra = palabra.lower()
    contador = 0

    for letra in palabra:
        if letra in "aeiou":
            contador += 1

    return contador
print(contar_vocales("Programacion")) 
print(contar_vocales("xyz"))         
print(contar_vocales("Hola"))       
