import os.path


FILE_PATH = "history.txt"
history_list = []

#Guardar la operación en la memoria
def Add_Operation(operacion):
    history_list.append(operacion)
    
#Mostrar el historial guardado en memoria
def Show_History():
    if not history_list:
        print("No hay operaciones en el historial.")
    else:
        print("\n--- Historial de Operaciones ---")
        for op in history_list:
            print(op)
        
#Borrar historial de memoria
def Clear_History():
    history_list.clear()
    print("Historial borrado.")
    
#Carga el historial si existe.
def Load_History():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Limpiar saltos de línea y cargar en lista
            global history_list
            history_list = [line.strip() for line in lines]

#Guarda el historial
def Save_History():
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            for operacion in history_list:
                file.write(operacion + "\n")
            print(f"Se ha guardado correctamente ", {FILE_PATH})
    except Exception as e:
        print(f"Ocurrió un error: {e}")