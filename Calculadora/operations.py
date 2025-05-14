import math

#Suma
def Sum(a, b):
    return a + b

#Resta
def Substract(a, b):
    return a - b

#Multiplicacion
def Multiply(a, b) :
    return a * b

#Division
def Divide(a, b):
    if b == 0:
        raise ValueError("Error: División entre cero no permitida.")
    return a / b

#Potencia
def Power(a,b):
    return a ** b

#Raíz cuadrada
def Square_root(a):
    if a < 0:
        raise ValueError("No se le puede sacar raíz cuadrada a números negativos.")
    return math.sqrt(a)

#Módulo
def Modulo(a,b):
    return a % b

#Factorial
def Factorial(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    return math.factorial(int(n))