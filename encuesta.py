from turtle import Turtle


print("\n\x1b[0;36mPrograma creado en Python\n"
    +"que recibe diferentes valores numericos\n"
    +"que representan a los estudiantes y diferentes datos de cada uno \n" 
    +"y realiza unos calculos para desplegar una encuesta.\n"
    +"---\n"
    +"Programa creado por:  Jesús Urrego\n"
    +"                 ID:  00000216768\n"
    +"  Fecha de creación:  20-02-2022\n"
    +"---\033[0m")

def encuesta():

    # ciclo que se ejecuta para realizar una nueva encuesta
    while True:
        # datos generales       
        total_alumnos = 0

        # sexos
        hombres = 0
        mujeres = 0

        # edades
        hombres_edad = 0
        mujeres_edad = 0

        # Lugar de residencia
        hombres_local = 0
        mujeres_local = 0

        hombres_foraneos = 0
        mujeres_foraneas = 0

        # Tipo de vivienda de los foraneos
        hombres_casa_asistencia = 0
        mujeres_casa_asistencia = 0

        hombres_compartir_casa = 0
        mujeres_compartir_casa = 0

        hombres_vivir_solo = 0
        mujeres_vivir_solo = 0

        print(f'\n\x1b[0;33m(Ingrese edad 0 para acabar con la toma de datos para la encuesta)\033[0m')

        # ciclo que se ejecuta registrar los datos de la encuesta
        while True:
            print()

            # ciclo que verifica una edad ingresada correcta
            while True:
                try:
                    edad = int(input(f'Ingrese la edad del alumno: '))
                    if edad < 0:
                        print('\033[91mError: el dato ingresado debe ser positivo\033[0m')
                        continue

                    break
                except:
                    print('\033[91mError: el dato ingresado debe ser numerico\033[0m')
                    continue
            
            # si la edad es igual a 0, se termina de recolectar datos y se imprimen los resultados
            if edad == 0:
                break

            total_alumnos += 1

            # ciclo que verifica un sexo seleccionado correcto
            while True:
                sexo = input('Ingrese el sexo del alumno (M = Masculino, F = Femenino): ').lower()
                if sexo == 'm' or sexo == 'f':
                    if sexo == 'm':
                        hombres += 1
                        hombres_edad += edad
                    else:
                        mujeres_edad += edad
                        mujeres += 1

                    break
                else:
                    print('\033[91mError: el dato ingresado no es correcto\033[0m')
                    continue
            
            # ciclo que verifica un origen del alumno seleccionado correcto
            while True:
                origen = input('Ingrese el origen del alumno (L = Local, F = Foráneo): ').lower()
                if origen == 'l' or origen == 'f':

                    # si el alumno que se esta registrando es foraneo
                    if origen == 'f':

                        # suma +1 en foraneo en hombre o mujer segun sea el caso
                        if sexo == 'm':
                            hombres_foraneos += 1
                        else:
                            mujeres_foraneas += 1

                        # ciclo que verifica un tipo de vivienda seleccionada correcta
                        while True:
                            print('Ingrese el tipo de vivienda deseada por del alumno')
                            tipo_vivienda = input('(A = Casa de asistencia, C = Compartir casa, S = Vivir solo): ').lower()
                            if tipo_vivienda == 'a' or tipo_vivienda == 'c' or tipo_vivienda == 's':

                                # suma +1 en el tipo de vivienda en hombre o mujer segun sea el caso
                                if sexo == 'm':
                                    if tipo_vivienda == 'a':
                                        hombres_casa_asistencia += 1
                                    elif tipo_vivienda == 'c':
                                        hombres_compartir_casa += 1
                                    else:
                                        hombres_vivir_solo += 1
                                else:
                                    if tipo_vivienda == 'a':
                                        mujeres_casa_asistencia += 1
                                    elif tipo_vivienda == 'c':
                                        mujeres_compartir_casa += 1
                                    else:
                                        mujeres_vivir_solo += 1                      
                                break
                            else:
                                print('\033[91mError: el dato ingresado no es correcto\033[0m')
                                continue
                    else:

                        # suma +1 en local en hombre o mujer segun sea el caso
                        if sexo == 'm':
                            hombres_local += 1
                        else:
                            mujeres_local += 1
                    break
                else:
                    print('\033[91mError: el dato ingresado no es correcto\033[0m')
                    continue

               
        print(f'\nResultados de la encuesta:\n'
                 +f'- Total de alumnos encuestados: {total_alumnos:2}\n'
                 +f'- Hombres: {hombres:25}\n'
                 +f'- Mujeres: {mujeres:25}\n'
                 +f'- Edad promedio de los hombres: {hombres_edad/hombres:5.2f}\n'
                 +f'- Edad promedio de las mujeres: {mujeres_edad/mujeres:5.2f}\n'
                 +f'- Porcentaje de hombres foráneos: {(hombres_foraneos/hombres) * 100:5.2f} %\n'
                 +f'- Porcentaje de mujeres foráneas: {(mujeres_foraneas/mujeres) * 100:5.2f} %\n'
                 +f'- Porcentaje de alumnos que desean vivir en casa de asistencia: {((hombres_casa_asistencia + mujeres_casa_asistencia) / total_alumnos) * 100:5.2f} %\n'
                 +f'- Porcentaje de alumnos mujeres que desean compartir casa: {(mujeres_compartir_casa/mujeres) * 100:5.2f} %\n'
                 +f'- Porcentaje de alumnos hombres que desean vivir solos: {(hombres_vivir_solo/hombres) * 100:5.2f} %') 

        input(f'\n\x1b[0;33mSi desea realizar una nueva encuesta presione ENTER, en caso contrario precione Ctrl+C\033[0m\n')

if __name__ == '__main__': 
    try:
        encuesta()
    except KeyboardInterrupt as e:
        print(f'\nHasta luego!\n')
        exit()
