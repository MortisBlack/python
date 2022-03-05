# se importa el paquete math para poder usar el valor de pi
import math

print("\nPrograma creado en Python\n"
    +"que recibe un valor numerico\n"
    +"que representa el radio de una esfera\n" 
    +"y encuentra su área y volumen.\n"
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

# variable que contiene el dato numerico que representa el radio de la esfera
radio = 0

while flag_exit == False:
    while flag_number == False:
        print("Ingrese el valor del radio de la esfera:")

        radio = input("> ")
        
        if radio.lower() == "c":
            flag_exit = True
            flag_number = True
        else:
            try:
                radio = float(radio)
                flag_number = True
            except:
                print("\033[91m\nError: el dato ingresado tiene que ser numerico\n\033[0m")
    else:
        if flag_exit == False:
            area = 4 *math.pi * (radio ** 2)
            volumen = (4/3) * math.pi * (radio ** 3)

            resultado = f'\nEl área de la esfera es: {area:.6f}' \
                        f'\nEl volumen de la esfera es: {volumen:.6f}' \
                        f'\n' \
                        f'\n---' \
                        f'\n'

            print(resultado)

            flag_number = False
else:
    print("\nHasta luego!\n")
    
