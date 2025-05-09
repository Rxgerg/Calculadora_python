
#Validar que estén metiendo un numero.
def Is_Number(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

#Pedir numero y validar si es tipo float
def Ask_Number(mensaje):
    while True:
        entrada = input(mensaje)
        if Is_Number(entrada):
            return float(entrada)
        print("Por favor, ingrese un número válido.")

#Desplegar un menú
def Show_Menu(opciones, title):
    print(f"\n--- {title} ---")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}) {opcion}")


#Seleccionar una opción númerica
def Ask_Option(mensaje, opciones):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= len(opciones):
                return opcion
            print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
