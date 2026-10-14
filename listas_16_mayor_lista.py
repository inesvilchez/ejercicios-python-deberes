'''
Algoritmo: Invertir cadena de texto
ENTRADAS: texto
SALIDA: texto_invertido

bloque de desarrollo
SI longitud(texto) <= 1:
    texto_invertido = texto
SINO:
    texto_invertido = invertir_texto(resto_del_texto) + primera_letra(texto)
FIN SI
DEVOLVER: texto_invertido
'''
def mayor_en_lista(numeros):
    """Devuelve el número mayor dentro de una lista."""
    mayor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor
print(mayor_en_lista([3, 8, 2, 10, 5]))  
print(mayor_en_lista([1]))              
print(mayor_en_lista([-5, -2, -9]))      
