print("\nPrograma creado en Python\n"
    +"que recibe un valor numerico\n"
    +"que representa una distancia en metros\n" 
    +"y regresa su equivalente en pies y pulgadas.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  29-01-2020\n"
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

# variable que contiene el dato numerico en metros que va a ser convertido
metros = 0

while flag_exit == False:
    while flag_number == False:
        print("Ingrese el valor en metros a convertir:")

        metros = input("> ")
        
        if metros.lower() == "c":
            flag_exit = True
            flag_number = True
        else:
            try:
                metros = float(metros)
                flag_number = True
            except:
                print("\033[91m\nError: el dato ingresado tiene que ser numerico\n\033[0m")
    else:
        if flag_exit == False:
            pies = metros * 3.2808
            pulgadas = metros * 39.3701

            resultado = f'\nEl valor ingresado en pies es: {pies:.4f}' \
                        f'\nEl valor ingresado en pulgadas es: {pulgadas:.4f}' \
                        f'\n' \
                        f'\n---' \
                        f'\n'

            print(resultado)

            flag_number = False
else:
    print("\nHasta luego!\n")
    
