from operations import *
from Functions.utils import *
from history import * 


opciones = ["Suma", "Resta", "Multiplicación", "División"]

def Perform_operation():
    
    a = Ask_Number("Ingrese el primer número: ")
    b = Ask_Number("Ingrese el segundo número: ")
    
    Show_Menu(opciones, title="Operaciones disponibles")
    opcion = Ask_Option("Ingrese el número de la operación que desea realizar: ", opciones)

    if opcion == 1:
        resultado = Sum(a, b)
        simbolo = "+"
    elif opcion == 2:
        resultado = Resta(a, b)
        simbolo = "-"
    elif opcion == 3:
        resultado = Multiplicacion(a, b)
        simbolo = "*"
    elif opcion == 4:
        try:
            resultado = Division(a, b)
            simbolo = "/"
        except ValueError as e:
            print(e)
            return
        
    operation_str = f"{a} {simbolo} {b} = {resultado}"
    Add_Operation(operation_str)
    print("El resultado de la operación es:", resultado)

#main
def main():
    #Asignamos una lista con las opciones del menú
    menuOptions = ["Realizar Operacion", "Ver historial", "Borrar historial", "Salir"]
    
    while True:
        Show_Menu(menuOptions,"Menu disponible")
        opcion = Ask_Option("Ingrese el número de la acción que desea realizar: ", menuOptions)
        
        if opcion ==  1:
            Perform_operation()
        elif opcion == 2:
            Show_History()
        elif opcion == 3:
            Delete_History()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
    

if __name__ == "__main__":
    main()
