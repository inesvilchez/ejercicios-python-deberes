'''
Algoritmo: Analizar frase
ENTRADAS: frase
SALIDA: frase_mayusculas, cantidad_palabras

bloque de desarrollo
frase_mayusculas = convertir_a_mayusculas(frase)
palabras = separar_por_espacios(frase)
cantidad_palabras = longitud(palabras)
DEVOLVER: frase_mayusculas, cantidad_palabras
'''
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    frase_mayus = frase.upper()
    palabras = frase.split()
    cantidad = len(palabras)
    return frase_mayus, cantidad
print(analizar_frase("hola que tal"))      
print(analizar_frase("esto es una prueba")) 
print(analizar_frase("python"))             
