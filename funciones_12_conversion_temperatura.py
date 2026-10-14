'''
Algoritmo: Celsius a Fahrenheit
ENTRADAS: celsius
SALIDA: fahrenheit

bloque de desarrollo
fahrenheit = (celsius * 9/5) + 32
DEVOLVER: fahrenheit
'''

'''
Algoritmo: Fahrenheit a Celsius
ENTRADAS: fahrenheit
SALIDA: celsius

bloque de desarrollo
celsius = (fahrenheit - 32) * 5/9
DEVOLVER: celsius
'''
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9
print(celsius_a_fahrenheit(0))  
print(fahrenheit_a_celsius(32))  
print(celsius_a_fahrenheit(25)) 
print(fahrenheit_a_celsius(77))    
