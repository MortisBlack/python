print("\nPrograma creado en Python\n"
    +"que lee un valor numerico\n"
    +"que representa la venta de un vendedor\n"
    +"y calcula su respectiva comisión\n" 
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  05-02-2022\n"
    +"---\n"
    +"(Para salir ingrese la letra \"c\" en cualquier momento)\n"
    +"---")

# variable usada para controlar si el programa continua o termina
flag_exit = False

# variable usada para almacenar la venta del vendedor
venta = 0

# variable para almancear el monto de la comisión correspondiente
comision = 0

# variable para almancear el porcentaje de la comisión correspondiente e imprimirlo en el mensaje del resultado
porcentaje = 0

'''
Función que comprueba que el valor ingresado de la venta sea numerico
'''
def comprobar(dinero):
    if dinero == 'c':
        global flag_exit
        flag_exit = True
    elif dinero.isnumeric() and float(dinero) >= 0:
        global venta
        venta = dinero
    else:
        print('\033[91mError: el dato ingresado es incorrecto\033[0m')
        comprobar(input())


'''
Función que calcula la comisión a pagar al vendedor
'''
def calcular(dinero):
    global comision, porcentaje
    
    if float(dinero) < 1000:
        comision = 0
        porcentaje = 0
    elif float(dinero) >= 1000 and float(dinero) <= 4999.99:
        comision = float(dinero) * 0.025
        porcentaje = 2.5
    elif float(dinero) >= 5000 and float(dinero) <= 9999.99:
        comision = float(dinero) * 0.05
        porcentaje = 5
    elif float(dinero) >= 10000 and float(dinero) <= 49999.99:
        comision = float(dinero) * 0.075
        porcentaje = 7.5
    elif float(dinero) >= 50000:
        comision = float(dinero) * 0.1
        porcentaje = 10


while flag_exit == False:
    print(f'Ingrese la cantidad de la venta total del vendedor:')
    comprobar(input())
    if flag_exit == False:
        calcular(venta)

        total = float(venta) + float(comision)
        print(f'Se ha calculado la comisión del vendedor.\n'
        f'Cómo la venta fue de ${float(venta):.2f}, la comisión del vendedor es del {float(porcentaje)}%\n'
        f'\n'
        f'Venta:    ${float(venta):.2f}\n'
        f'Comisión: ${float(comision):.2f}\n'
        f'--------------------------\n'
        f'Total:    ${total:.2f}\n')


else:
    print('\nHasta luego!')
