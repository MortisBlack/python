print("\nPrograma creado en Python\n"
    +"que recibe un valor numerico\n"
    +"que representa un monto de dinero a sacar de un cajero\n" 
    +"el cual tiene que ser multiplo de 50.\n"
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

# variable que representa el dinero que va a ser retirado del cajero
dinero = 0

# grupo de variables que representan los billetes entregados por el cajero al usuario
billete_mil         = 0
billete_quinientos  = 0
billete_cien        = 0
billete_cincuenta   = 0

while flag_exit == False:
    while flag_number == False:
        print("Ingrese el valor a retirar:")

        dinero = input("> ")
        
        if dinero.lower() == "c":
            flag_exit = True
            flag_number = True
        else:
            try:
                dinero = float(dinero)

                if dinero % 50 != 0:
                    print("\033[91m\nError: el dato ingresado debe ser multiplo de 50\n\033[0m")
                else:
                    flag_number = True
            except:
                print("\033[91m\nError: el dato ingresado tiene que ser numerico\n\033[0m")
    else:
        if flag_exit == False:

            while dinero > 0:
                if dinero % 1000 == 0:
                    dinero -= 1000
                    billete_mil += 1
                elif dinero % 500 == 0:
                    dinero -= 500
                    billete_quinientos += 1
                elif dinero % 100 == 0:
                    dinero -= 100
                    billete_cien += 1
                elif dinero % 50 == 0:
                    dinero -= 50
                    billete_cincuenta += 1

            resultado = f'\nLos billetes entregados fueron:' \
                        f'\nBilletes de 1000:   {billete_mil}' \
                        f'\nBilletes de 500:    {billete_quinientos}' \
                        f'\nBilletes de 100:    {billete_cien}' \
                        f'\nBilletes de 50:     {billete_cincuenta}\n'

            print(resultado)

            flag_number = False
else:
    print("\nHasta luego!\n")