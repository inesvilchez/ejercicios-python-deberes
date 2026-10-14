'''
Algoritmo: Calculadora segura
ENTRADAS: texto_a, texto_b, operacion
SALIDA: resultado

bloque de desarrollo
INTENTAR:
    num_a = convertir_a_decimal(texto_a)
    num_b = convertir_a_decimal(texto_b)
    
    SI operacion == "suma":
        resultado = num_a + num_b
    SINO SI operacion == "division":
        resultado = num_a / num_b
    FIN SI
    
CAPTURAR ValueError:
    resultado = "Error: valor no numérico"
CAPTURAR ZeroDivisionError:
    resultado = "Error: división entre cero"
FIN INTENTAR
DEVOLVER: resultado
'''
def invertir_diccionario(diccionario):
    """Devuelve un diccionario con claves y valores invertidos."""
    invertido = {}

    for clave, valor in diccionario.items():
        invertido[valor] = clave

    return invertido
print(invertir_diccionario({"a": 1, "b": 2, "c": 3}))  

print(invertir_diccionario({"x": "hola", "y": "adios"}))  

print(invertir_diccionario({10: "uno", 20: "dos"}))  
