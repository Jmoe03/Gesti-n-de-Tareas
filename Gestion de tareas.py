import Funciones 

#Bucle Principal 
while True: 

    # Menu de Opciones 
    print("\n***** --- Gestíon de Tareas Yatuté --- *****\n")
    print("1. Agregar Tarea")
    print("2. Ver Tarea")
    print("3. Marcar Tarea Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    print("\n")
    #Entrada Usuario
    opcion = input("Introduce una Opción: ")

    print("\n")
    #Menu 1
    match opcion:
     
         case "1":
          Funciones.Agregar_tareas(Funciones.tareas)
       
         case "2":
          Funciones.Ver_tareas(Funciones.tareas)
         
         case "3":
          Funciones.Marcar_tareas_Completada(Funciones.tareas)
      
         case "4":
          Funciones.Eliminar_tareas(Funciones.tareas)
      
         case "5":
           print("Gracias, Saliendo del Programa...")
           break

         case __doc__:
            print("Opción Inválida")


