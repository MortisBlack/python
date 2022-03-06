import maclaurin as mac

def leeRangoTerminos():
    while True:
            try:
                nMin = int(input('Ingrese el vlaor de nMin para el cálculo de la función: '))
                break
            except Exception as e:
                print('Error: el dato ingresado no es numerico')
                continue
    
    while True:
            try:
                nMax = int(input('Ingrese el vlaor de nMax para el cálculo de la función: '))
                break
            except Exception as e:
                print('Error: el dato ingresado no es numerico')
                continue

    while True:
            try:
                incN = int(input('Ingrese el vlaor de incN para el cálculo de la función: '))
                break
            except Exception as e:
                print('Error: el dato ingresado no es numerico')
                continue
    
    return (nMin, nMax, incN)

if __name__ == '__main__':
    funcion = ""
    x = 0

    while True:

        while True:
            funcion = input('Ingrese la función a tabular (s = seno, e = exponencial): ')
            if funcion.lower() == 's' or funcion.lower() == 'e':
                break
            else:
                print('Error: dato ingresado incorrecto')
                continue
        
        while True:
            try:
                x = float(input('Ingrese el vlaor de X para el cálculo de la función: '))
                break
            except Exception as e:
                print('Error: el dato ingresado no es numerico')
                continue

        terminos = leeRangoTerminos()

        if funcion == 's':
            formula = 'seno(x, n)'
        else:
            formula = 'exp(x, n)'

        print(f'Tabla de        X                Nmin     Nmax     incX')
        print(f'{formula}  {x:12.6f}  {terminos[0]:8d}{terminos[1]:10d}{terminos[2]:10d}')
        print('Resultados:')
        aux = terminos[0]
        for valor in mac.tabulaFuncion(funcion, x, terminos[0], terminos[1], terminos[2]):

            print(f'n = {aux}: {valor:.4f}')
            aux += terminos[2]
        print()
        
        salida = input('¿Desea repetir el cálculo? (s = si, n = no): ')
        if salida.lower() == 's':
            print()
            continue
        else:
            break
    
    print(f'\n¡Hasta luego!\n')
