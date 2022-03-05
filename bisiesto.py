print("\nPrograma creado en Python\n"
    +"que recibe un valor numerico\n"
    +"que representa un año\n" 
    +"y y comprueba si es bisiesto.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  05-02-2022\n"
    +"---\n"
    +"(Para salir ingrese la letra \"c\")\n"
    +"---\n")

    
'''
Variables usadas como compuertas logicas del programa
flag_exit   = sirve para indicar cuando el usuario indica que quiere dejar de ejecutar el programa
fla_number  = sirve para determinar que el dato ingresado es numerico
'''
flag_exit = False
flag_number = False

# variable que contiene el dato numerico que representa el año a comprobar
anho = 0

while flag_exit == False:
    while flag_number == False:
        print("Ingrese el año a comprobar:")

        anho = input("> ")
        
        if anho.lower() == "c":
            flag_exit = True
            flag_number = True
        else:
            try:
                anho = int(anho)
                flag_number = True
            except:
                print("\033[91m\nError: el dato ingresado tiene que ser numerico sin decimales\n\033[0m")
    else:
        if flag_exit == False:
            if anho % 4 == 0 :
                if anho % 100 == 0:
                    if anho % 400 == 0:
                        print(f"\nEl año {anho} es bisiesto.")
                    else:
                        print(f"\nEl año {anho} no es bisiesto.")
                else:
                    print(f"\nEl año {anho} es bisiesto.")
            else:
                print(f"\nEl año {anho} no es bisiesto.")

            resultado = f'\n---' \
                        f'\n'

            print(resultado)

            flag_number = False
else:
    print("\nHasta luego!\n")
    