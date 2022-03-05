import sympy as sp

print("Programa creado por:  Jesús Urrego\n"
     +"                 ID:  00000216768\n"
     +"  Fecha de creación:  25-02-2022\n"
    +"---\n")

def menu():
    asf = 0

def leeDatosIntegración():
    '''
    xi = 0
    xf = 0
    n = 0

    while True:
        try:
            xi = float(input('Ingrese el límite inferior: '))
            break
        except:
            print('Error: el dato ingresado no es correcto')
            continue

    while True:
        try:
            xf = float(input('Ingrese el límite superior: '))
            break
        except:
            print('Error: el dato ingresado no es correcto')
            continue
    
    while True:
        try:
            n = float(input('Ingrese el numero de rectángulos: '))
            break
        except:
            print('Error: el dato ingresado no es correcto')
            continue'''
    x = sp.Symbol('x')
    y=3*x
    print(sp.integrate(y,(x,5,7)))

    # return (xi, fi, n)


if __name__ == '__main__':
    leeDatosIntegración()
    print(f'\nHasta luego!\n')
