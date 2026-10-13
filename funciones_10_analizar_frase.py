# Algoritmo:
# Convertir la frase a mayúsculas
# Separar la frase en palabras usando split()
# Contar cuántas palabras hay
# Devolver la frase en mayúsculas y el número de palabras
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    frase_mayus = frase.upper()
    palabras = frase.split()
    cantidad = len(palabras)
    return frase_mayus, cantidad
print(analizar_frase("hola que tal"))      
print(analizar_frase("esto es una prueba")) 
print(analizar_frase("python"))             
