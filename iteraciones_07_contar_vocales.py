'''
Algoritmo: Contar vocales de una palabra
ENTRADAS: palabra
SALIDA: contador

bloque de desarrollo
contador = 0
palabra_minusculas = convertir_a_minusculas(palabra)
PARA CADA letra EN palabra_minusculas:
    SI letra == "a" O letra == "e" O letra == "i" O letra == "o" O letra == "u":
        contador = contador + 1
    FIN SI
FIN PARA
DEVOLVER: contador
'''
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
