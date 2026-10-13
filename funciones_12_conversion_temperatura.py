# Algoritmo Celsius → Fahrenheit:
# Recibir grados Celsius
# Aplicar fórmula: F = C * 9/5 + 32
# Devolver F

# Algoritmo Fahrenheit → Celsius:
# Recibir grados Fahrenheit
# Aplicar fórmula: C = (F - 32) * 5/9
# Devolver C
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
