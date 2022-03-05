import math

print("\nPrograma creado en Python\n"
    +"que recibe un valor numerico\n"
    +"que representan la velocidad inicial de un proyectil\n" 
    +"y calcula el ángulo al que debe dispararse para alcanzar su máxima distancia.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  13-02-2022\n"
    +"---")


# flag_exit   = sirve para indicar cuando el usuario indica que quiere dejar de ejecutar el programa
flag_exit = False

# variable que contiene la velocidad incial del proyectil
velocidad = 0

# variable auxiliar para indicar la salida del programa
aux = 0

# constante que contiene el valor que representa a la gravedad de la tierra
GRAVEDAD = 9.81

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

def calcularValores(velocidad):
    resultados = [0, 0]
    resultado = 0
    angulo = 0

    aux = 0

    print()

    for index in range(19):
        resultado = (2 * pow(float(velocidad), 2) * math.sin((angulo * math.pi)/180) * math.cos((angulo * math.pi)/180)) / GRAVEDAD
        
        
        if resultado > aux:
            aux = resultado
            resultados[0] = resultado
            resultados[1] = angulo
        
        print(f'En el ángulo {angulo:02d}°, el proyectil alcanzo  {resultado:.4f}m')
        angulo = angulo + 5

    return resultados

while flag_exit == False:
    print(f'\nIngrese la velocidad incial del proyectil:')
    valores = calcularValores(comprobar(input()))
    
    print(f'\nEn proyectil alcanzo la mayor distancia en el ángulo {valores[1]:02d}°')
    print(f'con un total de {valores[0]:.2f} metros recorridos.')

    print(f'\n¿Desea continuar?\n(\'c\' para salir, cualquier tecla para continuar)')
    aux = input()
    flag_exit = True if aux.lower() == 'c' else False
else:
    print("\nHasta luego!\n")