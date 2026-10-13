# Algoritmo:
# Si numero > 0 devolver "positivo"
# Si numero < 0 devolver "negativo"
# Si numero == 0 devolver "cero"

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