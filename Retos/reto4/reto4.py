from os import system
import math

menu_option = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana',
               'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo']

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


def myFunc(e):
    return e[0] 


def myFunc2(e):
    return e[2]


#funcion para calcular la distancia
#Recibe un array, la ubicación actual
def myDist(my_locate):
    #ordenamos las zonas wifi por cantidad de usuarios conectados de menor a mayor
    zonas_wifi.sort(key=myFunc2)
    distances = []
    R = 6372.795477598
    rad = math.pi/180
    for i in range(2):
        lat1 = my_locate[0]
        lat2 = zonas_wifi[i][0]
        dlat = lat2 - lat1
        dlon = zonas_wifi[i][1] - my_locate[1]
        a = (math.sin(rad*dlat/2))**2 + math.cos(rad*lat1) * math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
        distancia = 2*R*math.asin(math.sqrt(a))
        distances.append(distancia)
    print(distances)
    return distances

# funcion para sacar el promedio
def coordenate_prom(my_coordinates):
    pass


def updated_coordenate(my_coordinates, idx):
    print(f'Coordenada a actualizar # {idx+1}')
    for i in range(2):
        my_coordinates[idx].pop()
    
    for i in range(2):
        coordinates = float(input('Ingrese la nueva coordenada: '))
        if (coordinates >= -4.227 and coordinates <= -3.002 and i == 0) or (i == 1 and coordinates >= -70.365 and coordinates <= -69.714):
            my_coordinates[idx].append(coordinates)
        else:
            print('Error coordenada')
            exit()
    print(f'Ah sido actualizada la Coordenada # {idx+1}')
    return my_coordinates


def update_coordenate(my_coordinates):
    for i in range(0, len(my_coordinates)):
        print(f'coordenada [latitud,longitud] {i+1} : {my_coordinates[i]}')
    print(f'La coordenada 1 es la que esta más al sur')  # AQUI
    coor_promedio = coordenate_prom(my_coordinates) # variable que recibe el promedio
    print(f'Coordenada promedio de todos los puntos {coor_promedio} ')
    print(f'Presione 1,2 o 3 para actualizar la respectiva coordenada')
    print(f'presione 0 para regresar al menu')
    update_coor = int(input(': '))
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
        sesion_init(menu,my_coordinates)
    else:
        print('Error actualización')
        exit()


def captcha(cod):
    # 51604
    first_term = int(cod[2:])  # 610
    second_term = (((5+1) - 6) * 1)  # = 1
    result_capt = first_term + second_term
    captcha_received = int(input((f'{first_term} + {second_term} = ')))
    if result_capt == captcha_received:
        return True
    else:
        return False


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


def choose_favorite(menu_option, option_fav):
    option_new_fav = menu_option[option_fav-1]
    menu_option.remove(option_new_fav)
    menu_option.insert(0, option_new_fav)
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


def change_password(password):
    validation_password = input('Ingrese la contraseña actual: ')
    if validation_password == password:
        new__password = input('Ingrese la contraseña nueva: ')
        return new__password
    else:
        print('Error')


def coordinates(my_coordinates):
    new_coordinates = [
        [],
        [],
        [],
    ]
    
    try:
        if my_coordinates == [[], [], []]:
            for i in range(len(my_coordinates)):
                for j in range(2):
                    coordinates = float(input('Ingrese la coordenada: '))
                    if (coordinates >= -4.227 and coordinates <= -3.002 and j == 0) or (j == 1 and coordinates >= -70.365 and coordinates <= -69.714):
                        new_coordinates[i].append(coordinates)
                    else:
                        print("Error coordenada")
                        exit()
            my_coordinates = new_coordinates
            my_coordinates.sort(key=myFunc)
            return my_coordinates
        else:
            current = update_coordenate(my_coordinates)
            return current
    except:
        my_coordinates = my_coordinates
        print('Error')


def indications(distances, my_coordinates):
    y = ''
    x = ''
    print('Zonas wifi cercanas con menos usuarios')
    for i in range(2):
        print(
            f'La zona wifi {i+1}: ubicada en {zonas_wifi[i][0:2]} a {distances[i]} km, tiene en promedio {zonas_wifi[i][2]} usuarios')
    option = int(input('Elija 1 o 2 para recibir indicaciones de llegada: '))
    if option == 1:
        if zonas_wifi[0][0] >= my_coordinates[0]:
            y = 'norte'
        elif zonas_wifi[0][1] >= my_coordinates[1]:
            x = 'oriente'
        elif zonas_wifi[0][0] <= my_coordinates[0]:
            y = 'sur'
        elif zonas_wifi[0][1] <= my_coordinates[1]:
            x = 'occidente'
        tiempo = distances[0] / 0.00333
        print(f'Para llegar a la zona wifi, dirigirse primero a {x} y luego hacia el {y}')
        print(f'El tiempo promedio en moto es: {tiempo}')
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
        print(
            f'Para llegar a la zona wifi, dirigirse primero a {x} y luego hacia el {y}')
        print(f'El tiempo promedio en bici es: {tiempo}')
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
        indications(distances, my_coordinates[0])
        input('Presione 0 para salir')
    elif locate == 2:
        distances = myDist(my_coordinates[1])
        indications(distances, my_coordinates[1])
        input('Presione 0 para salir')
    elif locate == 3:
        distances = myDist(my_coordinates[2]) 
        indications(distances, my_coordinates[2])
        input('Presione 0 para salir')
    else:
        print('Error ubicación')
        exit()


def sesion_init(menu, my_coordinates, pwd):
    contador = 1
    print('Sesión iniciada')
    while contador < 4:
        print(menu)
        option = int(input('Elija una opción: '))
        if option == 6:
            option_fav = int(input('Elija una opción: '))
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
        elif option == 1:
            print('Usted ha elegido la opción 1')
            new_password = change_password(pwd)
            if new_password:
                pwd = new_password
            else:
                print('Error')
                break
        elif option == 2:
            print('Usted ha elegido la opción 2')
            current = coordinates(my_coordinates)
            my_coordinates = current
            if not current:
                break
        elif option == 3:
            if not my_coordinates == [[], [], []]:
                locate_wifi(my_coordinates)
            else:
                print('Error sin registro de coordenadas')
                break
        elif option == 4:
            print('Usted ha elegido la opción 4')
            break
        elif option == 5:
            print('Usted ha elegido la opción 5')
            break
        elif option == 7:
            print('Hasta pronto')
            break
        else:
            print('Error')
            contador += 1


def run():
    cod = '51604'
    pwd = '40615'
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
    username = input('Ingrese su usuario: ')
    
    if cod == username:
        password = input('Ingrese su contraseña: ')
        if password == pwd:
            result_capt = captcha(cod)
            if result_capt:
                sesion_init(menu, my_coordinates,pwd)
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')


if __name__ == '__main__':
    run()
