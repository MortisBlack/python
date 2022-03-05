import math

print("\nPrograma creado en Python\n"
    +"que recibe diferentes valores numericos\n"
    +"que representan a los estudiantes y sus calificaciones\n" 
    +"y calcula la calificación promedio y la desviación estándar de las calificaciones.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  13-02-2022\n"
    +"---")


# flag_exit   = sirve para indicar cuando el usuario indica que quiere dejar de ejecutar el programa
flag_exit = False

# variable que contiene el dato que representa a la cantidad de alumnos
estudiantes = 0

# lista para almacenar las calificaciones de los alumnos
calificaciones = []

# variable auxiliar para indicar la salida del programa
aux = 0

def comprobar(numero):
    """Comprueba que el valor ingresado sea numerico
    
    Si el valor ingresado no es numerico muestra un mensaje de error y vuelve a pedir el valor

    Parametros
    ----------
    numero : valor que sera comprobado
    """
    try:
        float(numero)
        return numero
    except ValueError:
        print('\033[91mError: el dato ingresado es incorrecto\033[0m')
        return comprobar(input())        

def calcularMedia(valores):
    """Calcula la media de los valores ingresados
    
    Parametros
    ----------
    valores : lista que contiene las calificaciones de los alumnos
    """

    cantidad = len(valores)
    sumatoria = 0

    aux = 0
    while aux < cantidad:
        sumatoria = sumatoria + float(valores[aux])
        aux = aux + 1

    return sumatoria / cantidad
    
def calcularDesviacion(valores, media):
    """Calcula la desviación estnadar de los valores ingresados
    
    Parametros
    ----------
    valores : lista que contiene las calificaciones de los alumnos
    media : valor de la media calculada de las calificaciones de los alumnos
    """

    cantidad = len(valores)
    sumatoria = 0

    aux = 0
    while aux < cantidad:
        valores[aux] = pow((float(valores[aux]) - media), 2)
        aux = aux + 1

    aux = 0
    while aux < cantidad:
        sumatoria = sumatoria + float(valores[aux])
        aux = aux + 1

    return math.sqrt(sumatoria / cantidad)

while flag_exit == False:
    print('Indique la cantidad de estudiantes en el salon:')
    estudiantes = comprobar(input())

    aux = 0
    while aux < int(estudiantes):
        print(f'Indique la calificación del estudiante numero {aux + 1}:')
        calificaciones.append(comprobar(input()))
        aux = aux + 1

    media = calcularMedia(calificaciones)

    desviacion = calcularDesviacion(calificaciones, media)

    print(f'\nLa calificación promedio es {media:.2f}')

    print(f'\nLa desviación estandar es {desviacion:.2f}')

    print(f'\n¿Desea continuar?\n(\'c\' para salir, cualquier tecla para continuar)')
    aux = input()
    flag_exit = True if aux.lower() == 'c' else False
else:
    print("\nHasta luego!\n")