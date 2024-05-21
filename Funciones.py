# Lista de Tareas a Realizar
tareas = ["Tarea 1", "Tarea 2", "Tarea 3"]
#funciones del programa
def agregar_tareas(lista):
    # Entrada de tarea
    tareas =input("Introducta la tarea:   ")

    # Añadir la tarea al final de la lista
    lista.append(tareas)

    #informe de tarea añadida
    print("\n Tarea Añadida a Lista Tareas Pendientes. \n")

    #Imprimir tarea añadida
    print(f"La tarea agregada es: {tareas}.")

    #Informar del número de tareas
    print (f"La tarea se almacenó en la posición: {len(lista)}\n")

def Ver_tareas(lista):
    # Condicional para evaluar  algo en la lista
     if lista:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")

    #Si la lista esta vacia avisa
     else:
        print("No Hay Tareas Pendientes")
    #Mensaje fin de lista
     print("--- Fin de Listado de Tarea ---")

def Marcar_tareas_Completada(lista):
    # Ver Tareas
     Ver_tareas(lista)

    #Entrada para que el usuario introduzca la tarea
     completada = int(input("\nIntoducir el Número de Tarea a Marcar como Completada:  "))

    #condicional para marcar tarea completada
     if completada > 0 and completada <= len(lista):
        #condicional para evaluar si l atarea estaba completada

        #si la tarea ya esta completa
        if "(completada)"  in lista[completada -1]:
            print(" La tarea ya estaba Marcada como completada. ")
        #en cambio, si no esta.
        else:
         lista[completada-1] = "(completada)" + lista[completada-1]
         print("Se marco la tarea como completada: ")
    # Avisar si la opción es invalida
     else: 
         print("Opción Inválida.")
          
def Eliminar_tareas(lista):
    
      #Si la lista contiene algo
    if lista:
        
        # funcion de ver tareas
        Ver_tareas(lista)
        # Entrada para que le usuario introduzca una tarea
        tarea = int(input("Introducir número de tarea a eliminar: "))

        # Opcion inválida si la tarea no se encuentra en el rango de la lista
        if tarea <=0 or tarea > len(lista):
            print("Opción Inválida.") 
        # Si la tarea es válida se elimina la tarea
        else:
            del lista[tarea -1]
            print("Se eliminó la tarea")
     # Si la lista esta vacia se avisa de ello
    else: 
        print(" No Hay Tareas")

