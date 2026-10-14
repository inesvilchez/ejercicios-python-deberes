'''
Algoritmo: División segura
ENTRADAS: a, b
SALIDA: resultado

bloque de desarrollo
INTENTAR:
    resultado = a / b
CAPTURAR ZeroDivisionError:
    resultado = "Error: división entre cero"
FIN INTENTAR
DEVOLVER: resultado
'''
def contar_elemento(lista, elemento):
    """Cuenta cuántas veces aparece un elemento en una lista."""
    contador = 0

    for item in lista:
        if item == elemento:
            contador += 1

    return contador
print(contar_elemento([1, 2, 3, 2, 2], 2))  
print(contar_elemento(["a", "b", "a"], "a")) 
print(contar_elemento([10, 20, 30], 5))     
