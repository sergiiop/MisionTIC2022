from os import system

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

def myFunc(e):
    return e[0] 


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
            print('Usted ha elegido la opción 3')
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
