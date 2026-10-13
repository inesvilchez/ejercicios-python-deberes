# Algoritmo:
# Para cada número desde 1 hasta 10:
#     calcular resultado = numero * i
#     imprimir "numero x i = resultado"
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
tabla_multiplicar(3)
tabla_multiplicar(7)
