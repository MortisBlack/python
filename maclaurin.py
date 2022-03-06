from math import factorial

print("Programa creado por:  Jesús Urrego\n"
     +"                 ID:  00000216768\n"
     +"  Fecha de creación:  05-03-2022\n"
    +"---\n")

def seno(x, n):
    sum = x
    aux = -1

    for i in range(3, n+1, +2):
        sum += aux * (pow(x, i) / factorial(i))
        aux *= -1

    return sum

def exp(x, n):
    sum = 1 + x

    for i in range(2, n+1):
        sum += (pow(x, i) / factorial(i))

    return sum

def tabulaFuncion(f, x, nMin, nMax, incN):
    valores = []
    
    if f.lower() == 's':
        for i in range(nMin, nMax+1, +incN):
            
            valores.append(seno(x, i))
    else:
        for i in range(nMin, nMax+1, +incN):
            valores.append(exp(x, i))
    
    return valores


if __name__ == '__main__':
    print(f'PRUEBAS\n')
    print('{0:15}{1:15}{2:15}{3:25}'.format('Función','x','n','Resultado'))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('seno(x,n)','0.785398','5',seno(0.785398,5)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('seno(x,n)','0.785398','10',seno(0.785398,10)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('seno(x,n)','1.570796','5',seno(1.570796,5)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('seno(x,n)','1.570796','10',seno(1.570796,10)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('exp(x,n)','1.0','5',exp(1.0,5)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('exp(x,n)','1.0','10',exp(1.0,10)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('exp(x,n)','-1.0','5',exp(-1.0,5)))
    print('{0:15}{1:15}{2:15}{3:8.6f}'.format('exp(x,n)','-1.0','10',exp(-1.0,10)))
    print()
    print('{0:15}{1:15}{2:15}{3:15}{4:15}'.format('Tabla de','X','Nmin','Nmax', 'incX'))
    print('{0:15}{1:15}{2:15}{3:15}{4:25}'.format('seno(x,n)','0.785398','5','10', '1'))
    print('Resultados:')
    aux = 5
    for valor in tabulaFuncion('s', 0.785398, 5, 10, 1):

        print(f'n = {aux}: {valor:.4f}')
        aux += 1
    print()

    print('{0:15}{1:15}{2:15}{3:15}{4:25}'.format('seno(x,n)','1.570796','5','15', '2'))
    print('Resultados:')
    aux = 5
    for valor in tabulaFuncion('s',1.570796, 5, 15, 2):

        print(f'n = {aux}: {valor:.4f}')
        aux += 2

    print('{0:15}{1:15}{2:15}{3:15}{4:25}'.format('exp(x,n)','1.0','5','10', '1'))
    print('Resultados:')
    aux = 5
    for valor in tabulaFuncion('e',1.0, 5, 10, 1):

        print(f'n = {aux}: {valor:.4f}')
        aux += 1
    print()

    print('{0:15}{1:15}{2:15}{3:15}{4:25}'.format('exp(x,n)','-1.0','5','15', '2'))
    print('Resultados:')
    aux = 5
    for valor in tabulaFuncion('e',1.0, 5, 10, 1):

        print(f'n = {aux}: {valor:.4f}')
        aux += 2
    print()
    