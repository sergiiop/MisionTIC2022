from os import system
import time
import math

#lista que contiene las opciones del menu
menu_option = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana',
               'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo']

#menu
menu = f"""
    Bienvenido
    1 - {menu_option[0]} 
    2 - {menu_option[1]}
    3 - {menu_option[2]}
    4 - {menu_option[3]}
    5 - {menu_option[4]}
    6 - Elegir opción de menú favorita
    7 - Cerrar sesión.
    """

location = []
recorrido = []
cod = '51604'
pwd = '40615'

# matriz de las coordenadas inicializadas vacias
my_coordinates = [
    [],
    [],
    [],
]

#Declaracion e inicialización de la matriz de la ubicación de cuatro zonas wifi con su respectivo promedio de usuarios
zonas_wifi = [
    [-3.777, -70.302, 91],
    [-4.134, -69.983, 233],
    [-4.006, -70.132, 149],
    [-3.846, -70.222, 211],
]

#funcion para ordenar la matriz tomando como referencia la posicion 1
def myFunc(e):
    return e[0] 

#funcion para ordenar la matriz tomando como referencia la posicion 1
def myFunc2(e):
    return e[2]


def import_file(informacion):
    try:
        archivo=open('archivoescritura.txt','w')
        archivo.write(str(informacion))
    except IOError:
        print('Error con el fichero')
        time.sleep(1)
        print('Exportando...')
        exit()
    except FileNotFoundError:
        print('Error con el fichero')
        time.sleep(1)
        print('Exportando...')
        exit()
    except:
        print('Error con el fichero')
        time.sleep(1)
        print('Exportando...')
        exit()
#funcion para calcular la distancia
#Recibe un array, la ubicación actual
def myDist(my_locate):
    #ordenamos las zonas wifi por cantidad de usuarios conectados de menor a mayor
    zonas_wifi.sort(key=myFunc2)
    #inicializamos una lista
    distances = []
    # formula para encontrar la distancia entre dos coordenadas
    R = 6372.795477598
    rad = math.pi/180
    #necesitamos calcular dos distancias diferentes, por lo que hacemos un loop que hara el calculo, para la latitud 1 y longitud 1, utilizamos los valores que tiene el array my_locate, para la latitud 2 y longitud 2, utilizamos los dos primeros arrays de la matriz zonas_wifi y de estos arrays los dos primeros valores
    for i in range(2):
        lat1 = my_locate[0]
        lat2 = zonas_wifi[i][0]
        dlat = lat2 - lat1
        dlon = zonas_wifi[i][1] - my_locate[1]
        a = (math.sin(rad*dlat/2))**2 + math.cos(rad*lat1) * math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
        distancia = 2*R*math.asin(math.sqrt(a))
        #agregamos las distancias a la lista
        distances.append(distancia)
    print(distances)
    return distances

# funcion para sacar el promedio
def coordenate_prom(my_coordinates):
    pass

#función que efectua la actualizacion de las coordenadas dependiendo del indice
def updated_coordenate(my_coordinates, idx):
    print(f'Coordenada a actualizar # {idx+1}')
    #eliminamos las coordenadas actuales segun el indice
    for i in range(2):
        my_coordinates[idx].pop()
    
    #solicitamos que se agreguen las nuevas coordenadas
    for i in range(2):
        coordinates = float(input('Ingrese la nueva coordenada: '))
        if (coordinates >= -4.227 and coordinates <= -3.002 and i == 0) or (i == 1 and coordinates >= -70.365 and coordinates <= -69.714):
            my_coordinates[idx].append(coordinates)
        else:
            print('Error coordenada')
            exit()
    print(f'Ah sido actualizada la Coordenada # {idx+1}')
    return my_coordinates


#funcion para hacer la actualizacion de coordenadas
def update_coordenate(my_coordinates):
    #mostramos las coordenadas actuales 
    for i in range(0, len(my_coordinates)):
        print(f'coordenada [latitud,longitud] {i+1} : {my_coordinates[i]}')
    print(f'La coordenada 1 es la que esta más al sur')  # AQUI
    coor_promedio = coordenate_prom(my_coordinates) # variable que recibe el promedio
    print(f'Coordenada promedio de todos los puntos {coor_promedio} ')
    print(f'Presione 1,2 o 3 para actualizar la respectiva coordenada')
    print(f'presione 0 para regresar al menu')
    update_coor = int(input(': '))
    #dependiendo de cual opcion eloja la funcion update_coordenate, actualizará la coordenada
    #esta funcion recibe la matriz donde estan las coordenadas en el indice de la fila que sera la coordenada a actualizar
    if update_coor == 1:
        my_coordinates = updated_coordenate(my_coordinates, 0)
        return my_coordinates
    elif update_coor == 2:
        my_coordinates = updated_coordenate(my_coordinates, 1)
        return my_coordinates
    elif update_coor == 3:
        my_coordinates = updated_coordenate(my_coordinates, 2)
        return my_coordinates
    elif update_coor == 0:
        (menu,my_coordinates)
    else:
        print('Error actualización')
        exit()


#funcion para verificar el capcha
def captcha(cod):
    # 51604
    first_term = int(cod[2:])  # primer termino => 610
    second_term = (((5+1) - 6) * 1)  # = 1
    result_capt = first_term + second_term
    captcha_received = int(input((f'{first_term} + {second_term} = ')))
    #validacion si el resultada del capcha es igual al que el usuario esta ingresando
    if result_capt == captcha_received:
        return True
    else:
        return False


#validacion para el cambio favorito del menu
#al final retorna verdadero o falso con eso se hace posteriormente la validacion
def validation():
    print('Confirmación')
    first_option = int(input('Primera adivinanza: '))
    if first_option == 0:
        second_option = int(input('Segunda adivinanza: '))
        if second_option == 4:
            return True
        else:
            print('Error')
            return False
    else:
        print('Error')
        return False


#funcion para hacer el cambio de menu
#esta funcion recibe como paremetro la opcion del menu que se quiere elegir como favorito y la lista que contiene las opciones del menu
def choose_favorite(menu_option, option_fav):
    #guardamos temporalmente la opcion que se eligio
    option_new_fav = menu_option[option_fav-1]
    #eliminamos esa opion de la lista
    menu_option.remove(option_new_fav)
    #la insertamos en la posicion inicial
    menu_option.insert(0, option_new_fav)
    #declaramos un nuevo menu con la posicon actualizada
    new_menu = f"""
    Bienvenido
    1 - {menu_option[0]} 
    2 - {menu_option[1]}
    3 - {menu_option[2]}
    4 - {menu_option[3]}
    5 - {menu_option[4]}
    6 - Elegir opción de menú favorita
    7 - Cerrar sesión.
    """
    return new_menu


#funcion para cambiar de contraseña
#recibe como parametro la contraseña actual
def change_password(password):
    validation_password = input('Ingrese la contraseña actual: ')
    #validacion de la contraseña actual
    if validation_password == password:
        new__password = input('Ingrese la contraseña nueva: ')
        return new__password
    else:
        print('Error')


#función para el manejo de las coordenadas
#recibe como parametro las coordenadas actuales
def coordinates(my_coordinates):
    #inicializamos una nueva matriz que sera la temporal
    new_coordinates = [
        [],
        [],
        [],
    ]
    
    try:
        #validamos si las coordenadas estan vacias o llenas
        if my_coordinates == [[], [], []]:
            #si estan vacias las llenamos
            for i in range(len(my_coordinates)):
                for j in range(2):
                    coordinates = float(input('Ingrese la coordenada: '))
                    #controlamos los limites establecidos
                    if (coordinates >= -4.227 and coordinates <= -3.002 and j == 0) or (j == 1 and coordinates >= -70.365 and coordinates <= -69.714):
                        new_coordinates[i].append(coordinates)
                    else:
                        print("Error coordenada")
                        exit()
            #hacemos la asignacion de las coordenadas temporales a las coordenadas actuales
            my_coordinates = new_coordinates
            #ordenamos las coordenadas de menor a mayor
            my_coordinates.sort(key=myFunc)
            #retornamos las nuevas coordenadas
            return my_coordinates
        else:
            #si no esta vacia la matriz preguntamos si quiere actualizar
            current = update_coordenate(my_coordinates)
            return current
    except:
        my_coordinates = my_coordinates
        print('Error')

#funcion para dar las indicaciones y el tiempo en llegar al lugar
#recibe dos parametros, las distancias y las coordenadas
def indications(distances, my_coordinates):
    #inicializamos Y y X que se le asignaran luego el sentido
    y = ''
    x = ''
    recorrido = []
    print('Zonas wifi cercanas con menos usuarios')
    #mostramos las coordenadas
    for i in range(2):
        print(
            f'La zona wifi {i+1}: ubicada en {zonas_wifi[i][0:2]} a {distances[i]} km, tiene en promedio {zonas_wifi[i][2]} usuarios')
    option = int(input('Elija 1 o 2 para recibir indicaciones de llegada: '))
    #dependiendo de la opcion que elija se mostrara una direccion u otra
    if option == 1:
        if zonas_wifi[0][0] >= my_coordinates[0]:
            y = 'norte'
        elif zonas_wifi[0][1] >= my_coordinates[1]:
            x = 'oriente'
        elif zonas_wifi[0][0] <= my_coordinates[0]:
            y = 'sur'
        elif zonas_wifi[0][1] <= my_coordinates[1]:
            x = 'occidente'
        #calculo del tiempo
        tiempo = distances[0] / 0.00333
        recorrido.append(distances)
        recorrido.append('moto')
        recorrido.append(tiempo)
        print(f'Para llegar a la zona wifi, dirigirse primero a {x} y luego hacia el {y}')
        print(f'El tiempo promedio en moto es: {tiempo}')
        return recorrido
    elif option == 2:
        if zonas_wifi[1][0] >= my_coordinates[0]:
            y = 'norte'
        elif zonas_wifi[1][1] >= my_coordinates[1]:
            x = 'oriente'
        elif zonas_wifi[1][0] <= my_coordinates[0]:
            y = 'sur'
        elif zonas_wifi[1][1] <= my_coordinates[1]:
            x = 'occidente'
        tiempo = distances[1] / 0.01944
        recorrido.append(distances)
        recorrido.append('bici')
        recorrido.append(tiempo)
        print(
            f'Para llegar a la zona wifi, dirigirse primero a {x} y luego hacia el {y}')
        print(f'El tiempo promedio en bici es: {tiempo}')
        return recorrido
    else:
        print('Error zona wifi')
        exit()

#Funcion para localizar los wifi más cercanos dependiendo a la ubicación
def locate_wifi(my_coordinates):
    #mostramos las ubicaciones más frecuentes
    for i in range(0, len(my_coordinates)):
        print(f'coordenada [latitud,longitud] {i+1} : {my_coordinates[i]}')
    #Solicitamos la ubicacion actual
    locate = int(input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: '))
    #dependiendo de la ubicación se le manda un array a la funcion para calcular la distancia
    if locate == 1:
        #si la ubicacion es la primera, se envia la coordenada que esta en la primera posición de la matriz 
        distances = myDist(my_coordinates[0])
        recorrido = indications(distances, my_coordinates[0])
        option = int(input('Presione 0 para salir'))
        if option == 0:
            sesion_init(menu, my_coordinates, pwd,
                        my_coordinates[0], zonas_wifi[0], recorrido)
    elif locate == 2:
        distances = myDist(my_coordinates[1])
        recorrido = indications(distances, my_coordinates[1])
        option = int(input('Presione 0 para salir'))
        if option == 0:
            sesion_init(menu, my_coordinates, pwd,
                        my_coordinates[1], zonas_wifi[0], recorrido)
    elif locate == 3:
        distances = myDist(my_coordinates[2]) 
        recorrido = indications(distances, my_coordinates[2])
        option = int(input('Presione 0 para salir'))
        if option == 0:
            sesion_init(menu, my_coordinates, pwd,
                        my_coordinates[2],zonas_wifi[0], recorrido)
    else:
        print('Error ubicación')
        exit()


def save_location(actual, zona_wifi_1, recorrido):
    informacion = {
      'actual': actual,
      'zona_wifi_1': zona_wifi_1,
      'recorrido': recorrido,
    }
    print(informacion)
    option = int(input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal'))
    if option == 1:
        print('Exportando archivo')
        import_file(informacion)
        exit()
    if option == 0:
        return False


def leer_archivo(archivo):
    try:
        archivo = open(archivo).readline()
        archivo=archivo.split(';')
        
        list_temp = []
        
        for x in range(0,4):
            list_temp.append([])
            tmp = archivo[x].split(',')
            for y in range(0,3):
                list_temp[x].append(tmp[y])
        
        for x in range(len(list_temp)):
            for y in range(0,len(list_temp[x])):
                list_temp[x][y] = float(list_temp[x][y])
                if y==2:
                    list_temp[x][y] = int(list_temp[x][y])
        option = int(input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal '))
        if option == 0:
          sesion_init(menu, my_coordinates, pwd,my_coordinates[2], zonas_wifi[0], recorrido)
          return list_temp
    except FileNotFoundError:
        print('Error con la creacion del fichero')
        return [[-4.10112000, -69.94058000, 192],
                [- 4.12018100, -69.94746000, 137],
                [- 3.84656400, -70.22285000, 211],
                [- 4.13488700, -69.98357000, 233]
                ]
    except ValueError:
        print('Dato Invalido')
        return [[-4.10112000, -69.94058000, 192],
                [- 4.12018100, -69.94746000, 137],
                [- 3.84656400, -70.22285000, 211],
                [- 4.13488700, -69.98357000, 233]
                ]
    except:
        print('Error.')
        return [[-4.10112000, -69.94058000, 192],
                [- 4.12018100, -69.94746000, 137],
                [- 3.84656400, -70.22285000, 211],
                [- 4.13488700, -69.98357000, 233]
                ]
#funcion que contiene la sesion iniciada
def sesion_init(menu, my_coordinates, pwd, location,zona_wifi,recorrido):
    #contador para el control de intentos
    contador = 1
    while contador < 4:
        print(location)
        print(menu)
        option = int(input('Elija una opción: '))
        #opcion para elegir favorito
        if option == 6:
            option_fav = int(input('Elija una opción: '))
            #dependiendo de la opcion que elija el usuario, hara una validacion, llamará a la función que realiza el cambio y al final al menu se le aplican los cambios
            if option_fav == 1:
                is_valid = validation()
                if is_valid:
                    system("cls")
                    menu = menu
            elif option_fav == 2:
                is_valid = validation()
                if is_valid:
                    system("cls")
                    new_option = choose_favorite(
                        menu_option, option_fav)
                    menu = new_option
            elif option_fav == 3:
                is_valid = validation()
                if is_valid:
                    system("cls")
                    new_option = choose_favorite(
                        menu_option, option_fav)
                    menu = new_option
            elif option_fav == 4:
                is_valid = validation()
                if is_valid:
                    system("cls")
                    new_option = choose_favorite(
                        menu_option, option_fav)
                    menu = new_option
            elif option_fav == 5:
                is_valid = validation()
                if is_valid:
                    system("cls")
                    new_option = choose_favorite(
                        menu_option, option_fav)
                    menu = new_option
            else:
                print('Error')
                break
        #opcion para cambiar la contraseña
        elif option == 1:
            print('Usted ha elegido la opción 1')
            #variable que contiene la nueva contraseña retornada por la funcion cambiar_contraseña
            # a esta funcion se le pasa como parametro la contraseña actual
            new_password = change_password(pwd)
            #validacion de que se hizo el cambio de contraseña exitoso
            if new_password:
                pwd = new_password
            else:
                print('Error')
                break
        #opcion para ingresar o actualizar coordenadas
        elif option == 2:
            print('Usted ha elegido la opción 2')
            # variable temporal que almacena las coordenadas que retorne la funcion coordenadas
            # esta funcion recibe como parametros las coordenadas actuales
            current = coordinates(my_coordinates)
            # la variable que contiene las coordenadas actuales seran actualizadas por lo que contenga la temporal
            my_coordinates = current
            #si la funcion retorna False es porque ocurrio un error
            if not current:
                break
        #opcion para localizar zonas wifi
        elif option == 3:
            # si las coordenadas no estan vacias procede al llamado de la funcion localizar_wifi
            #esta funcion recibe como parametros las coordenadas
            if not my_coordinates == [[], [], []]:
                locate = locate_wifi(my_coordinates)
                location = locate
                return location
            else:
            #si las coordenadas estan vacias, error
                print('Error sin registro de coordenadas')
                break
        elif option == 4:
            if not location == []:
                savetmp = save_location(location,zona_wifi, recorrido)
                zonas_wifi = savetmp
                if savetmp:
                  input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ')
                else:
                    next
            else:
                print('Error de alistamiento')
                break
        elif option == 5:
            leer_archivo('archivolectura.txt')
            break
        elif option == 7:
            print('Hasta pronto')
            break
        else:
            print('Error')
            contador += 1


# inicio del codigo
def run():
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
    username = input('Ingrese su usuario: ')
    
    # validacion de sesion
    if cod == username:
        password = input('Ingrese su contraseña: ')
        if password == pwd:
            result_capt = captcha(cod)
            if result_capt:
                sesion_init(menu, my_coordinates,pwd, location,zonas_wifi[0],recorrido)
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')


if __name__ == '__main__':
    run()
