#Suma
def Sum(a, b):
    return a + b

#Resta
def Resta(a, b):
    return a - b

#Multiplicacion
def Multiplicacion(a, b) :
    return a * b

#Division
def Division(a, b):
    if b == 0:
        raise ValueError("Error: División entre cero no permitida.")
    return a / b
