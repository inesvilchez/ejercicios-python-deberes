#Algoritmo: Signo de un número
#ENTRADAS: numero
#SALIDA: resultado

#bloque de desarrollo
#SI numero > 0:
#    resultado = "positivo"
#SINO SI numero < 0:
#    resultado = "negativo"
#SINO:
#    resultado = "cero"
#FIN SI
#DEVOLVER: resultado

def signo_numero(numero):
    """Devuelve si un número es positivo, negativo o cero."""
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
print(signo_numero(-5))
print(signo_numero(0))
print(signo_numero(7))