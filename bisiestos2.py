print("\nPrograma creado en Python\n"
    +"que recibe dos valores numericos\n"
    +"que representan dos años\n" 
    +"y crea una lista que muestra los años bisiestos entre los dos años.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  25-02-2022\n"
    +"---\n")

# método que lee los años entre los cuales se hara la comprobación de cuales son bisiestos y cuales no
def leeAnhos():
    
    primer_anho = 0
    segundo_anho = 0

    while True:
        try: 
            primer_anho = int(input('Ingrese el primer año: '))
            if primer_anho > 0:
                break
            else:
                print('Error: el dato ingresado debe ser mayor a cero')
                continue
        except:
            print('Error: el dato ingresado no es correcto')
            continue

    while True:
        try:
            segundo_anho = int(input('Ingrese el segundo año: '))
            if segundo_anho > 0:
                break
            else:
                print('Error: el dato ingresado debe ser mayor a cero')
                continue
        except:
            print('Error: el dato ingresado no es correcto')
            continue

    if segundo_anho < primer_anho:
        aux = segundo_anho
        segundo_anho = primer_anho
        primer_anho = aux

    return (primer_anho, segundo_anho)

# método que almacena en una lista los años que son bisiestos y luego los imprime en un mensaje
def listaBisiesto(anhos):
    inicio = anhos[0]
    fin = anhos[1]

    anhos_bisiestos = []

    while inicio <= fin:
        aux = esBisiesto(inicio)
        if aux != None:
            anhos_bisiestos.append(aux)
        inicio += 1

    print()
    print(anhos_bisiestos) 

# método que comprueba si un año es bisiesto o no
def esBisiesto(anho):
    if anho % 4 == 0:
        if anho % 100 == 0:
            if anho % 400 == 0:
                return anho
        else:
            return anho

if __name__ == '__main__': 
    try:
        while True:
            listaBisiesto(leeAnhos())
            input(f'\nSi desea realizar una nueva encuesta presione ENTER, en caso contrario precione Ctrl+C\n')
    except KeyboardInterrupt as e:
        print(f'\nHasta luego!\n')
        exit()