print("\nPrograma creado en Python\n"
    +"que recibe dos valores numericos\n"
    +"que representan dos años\n" 
    +"y crea una lista que muestra los años bisiestos entre los dos años.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  13-02-2022\n"
    +"---\n"
    +"(Para salir ingrese la letra \"c\")\n"
    +"---")


# flag_exit   = sirve para indicar cuando el usuario indica que quiere dejar de ejecutar el programa
flag_exit = False

# variable que contiene el dato numerico que representa el año del principio
anho_01 = 0

# variable que contiene el dato numerico que representa el año del final
anho_02 = 0

# variable auxiliar para acomodar los años ingresados de menor a mayor
aux = 0

def comprobar(numero):
    """Comprueba que el valor ingresado sea numerico
    
    Si el valor ingresado no es numerico muestra un mensaje de error y vuelve a pedir el valor

    Tambien sirve para salir del programa si el usuario ingresa la letra 'c'

    Parametros
    ----------
    numero : valor que sera comprobado
    """
    global flag_exit
    if numero.lower() == "c":
        flag_exit = True
    elif  numero.isnumeric():
        return numero
    else:
        print('\033[91mError: el dato ingresado es incorrecto\033[0m')
        return comprobar(input())

def bisiestos(numero):
    """Función que recibe un valor y comprueba que sea un año bisiesto
    
    Parametros
    ----------
    numero : valor que sera comprobado
    """

    if int(numero) % 4 == 0 :
                if int(numero) % 100 == 0:
                    if int(numero) % 400 == 0:
                        print(f'- {numero}')
                else:
                    print(f'- {numero}')

while flag_exit == False:
    print('\nIngrese el primer año:')
    anho_01 = comprobar(input())

    if flag_exit == False:
        print('Ingrese el segundo año:')
        anho_02 = comprobar(input())

    if flag_exit == False:
        if int(anho_01) > int(anho_02):
            aux = anho_02
            anho_02 = anho_01
            anho_01 = aux

        print(f'\nLos años bisiestos entre {anho_01} y {anho_02} son:')

        while int(anho_01) <= int(anho_02):
            bisiestos(anho_01)
            anho_01 = int(anho_01) + 1
        
        print(f'\n¿Desea continuar?\n(\'c\' para salir, cualquier tecla para continuar)')
        aux = input()
        flag_exit = True if aux.lower() == 'c' else False

else:
    print("\nHasta luego!\n")