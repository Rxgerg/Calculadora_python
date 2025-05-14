from operations import *
from Functions.utils import *
from history import * 


opciones = ["Suma", "Resta", "Multiplicación", "División", "Potencia", "Raíz cuadrada", "Módulo", "Factorial"]

def Perform_operation():
    operation_str = None
    
    Show_Menu(opciones, title="Operaciones disponibles")
    opcion = Ask_Option("Ingrese el número de la operación que desea realizar: ", opciones)
    
    #Operaciones que necesitan dos números.
    if opcion in [1,2,3,4,5,7]:
        a = Ask_Number("Ingrese el primer número: ")
        b = Ask_Number("Ingrese el segundo número: ")

    if opcion == 1:
        resultado = Sum(a, b)
        simbolo = "+"
        operation_str = f"{a} {simbolo} {b} = {resultado}"
    elif opcion == 2:
        resultado = Substract(a, b)
        simbolo = "-"
        operation_str = f"{a} {simbolo} {b} = {resultado}"
    elif opcion == 3:
        resultado = Multiply(a, b)
        simbolo = "*"
        operation_str = f"{a} {simbolo} {b} = {resultado}"
    elif opcion == 4:
        try:
            resultado = Divide(a, b)
            simbolo = "/"
            operation_str = f"{a} {simbolo} {b} = {resultado}"
        except ValueError as e:
            print(e)
            operation_str = None
            return
    elif opcion == 5:
        resultado = Power(a,b)
        simbolo = "^"
        operation_str = f"{a} {simbolo} {b} = {resultado}"
    elif opcion == 6:
        a = Ask_Number("Ingrese el número para la raíz cuadrada: ")
        try:
            resultado = Square_root(a)
            operation_str = f"√{a} = {resultado}"
        except ValueError as e:
            print(e)
            operation_str = None
            return
    elif opcion == 7:
        resultado = Modulo(a,b)
        simbolo = "%"
        operation_str = f"{a} {simbolo} {b} = {resultado}"
    elif opcion == 8:
        n = Ask_Number("Ingrese un número entero no negativo para el factorial: ")
        try:
            resultado = Factorial(n)
            operation_str = f"{int(n)}! = {resultado}"
        except ValueError as e:
            print(e)
            return
    else:
        print("Operación no válida.")
        return
       
    if operation_str is not None:
        Add_Operation(operation_str)
        print("El resultado de la operación es:", resultado)
    else: 
        print("No se pudo registrar la operación en el historial.")

#main
def main():
    #Asignamos una lista con las opciones del menú
    menuOptions = ["Realizar Operacion", "Ver historial", "Borrar historial", "Guardar historial", "Salir"]
    
    while True:
        Show_Menu(menuOptions,"Menu disponible")
        opcion = Ask_Option("Ingrese el número de la acción que desea realizar: ", menuOptions)
        
        if opcion ==  1:
            Perform_operation()
        elif opcion == 2:
            Show_History()
        elif opcion == 3:
            Clear_History()
        elif opcion == 4:
            Save_History()
        elif opcion == 5:
            print("¡Hasta luego!")
            break
    

if __name__ == "__main__":
    main()
