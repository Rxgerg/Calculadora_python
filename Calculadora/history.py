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
def Delete_History():
    history_list.clear()
    print("Historial borrado.")