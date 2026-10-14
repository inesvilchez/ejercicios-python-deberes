'''
Algoritmo: Tabla de multiplicar
ENTRADAS: numero
SALIDA: mostrar_pantalla

bloque de desarrollo
contador = 1
MIENTRAS contador <= 10:
    IMPRIMIR numero + " x " + contador + " = " + (numero * contador)
    contador = contador + 1
FIN MIENTRAS
'''
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
tabla_multiplicar(3)
tabla_multiplicar(7)
