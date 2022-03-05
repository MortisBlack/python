import math

print("\nPrograma creado en Python\n"
    +"que recibe una letra (P o S) y un valor numerico\n"
    +"los cuales representa el tipo de mosaico para la letra\n"
    +"y los metros cuadrados de un piso\n" 
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  05-02-2022\n"
    +"---\n"
    +"(Para salir ingrese la letra \"c\" en cualquier momento)\n"
    +"---")

# variable usada para controlar si el programa continua o termina
flag_exit = False

# variable para determinar el tipo de mosaico
tipo = ''

# variable que contiene la superficie a calcular
metros = 0

# variable para almacenar el monto a pagar segun las cajas calculadas
resultado = 0

# cajas que se van a comprar
cajas = 0

# precio de la caja del mosaico de primera
PRECIO_P = 150

# precio de la caja del mosaico de segunda
PRECIO_S = 125

'''
Función que comprueba el tipo de mosaico que se va a comprar
P = mosaico de primera
S = mosaico de segunda
'''
def camino(letra):
    if letra == 'c':
        global flag_exit
        flag_exit = True
    elif letra.lower() == 'p' or letra.lower() == 's':
        global tipo
        tipo = letra
    else:
        print('\033[91mError: el dato ingresado es incorrecto\033[0m')
        camino(input())


'''
Función que comprueba que el valor ingresado para el piso sea numerico
'''
def superficie(numero):
    if numero == 'c':
        global flag_exit
        flag_exit = True
    elif numero.isnumeric():
        global metros
        metros = numero
    else:
        print('\033[91mError: el dato ingresado es incorrecto\033[0m')
        superficie(input())


'''
Función que hace el calculo de las cajas necesarias y monto a pagar
'''
def calculo():
    global tipo, metros, PRECIO_P, PRECIO_S, resultado, cajas

    # Si es mosaico de primera
    if tipo.lower() == 'p':
        # Se redondea hacia arriba para poder cubrir el area total
        cajas = math.ceil(float(metros) / 0.9)
        resultado = cajas * PRECIO_P
    
    # Si es mosaico de segunda
    if tipo.lower() == 's':
        # Se redondea hacia arriba para poder cubrir el area total
        cajas = math.ceil(float(metros) / 0.85)
        resultado = cajas * PRECIO_S


while flag_exit == False:
    print(f'\nIngrese el tipo de mosaico (una letra):'
        f'\n - P = mosaico de primra'
        f'\n - S = mosaico de segunda')
    camino(input())

    if flag_exit == False:
        print(f'\nIngrese la superficie del piso:')
        superficie(input())

        if flag_exit == False:
            calculo()

            # variable usada para poder imprimir el tipo de mosaico en el mensaje
            palabra = 'primera' if tipo.lower() == 'p' else 'segunda' 

            print(f'\nEl total de cajas necesarias para cubrir el area de {metros}m2 es de {cajas} cajas.'+
            f'\nAl ser mosaico de {palabra} el monto a pagar es de ${resultado:.2f}\n')

else:
    print('\nHasta luego!')
