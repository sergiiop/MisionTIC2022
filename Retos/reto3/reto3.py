from os import system


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
    new__password = input('Ingrese la contraseña nueva: ')
    if new__password == password:
        return False
    else:
        validation_password = input('Ingrese la contraseña actual: ')
        if validation_password == password:
            return new__password


def coordinates():
    my_coordinates = [
        [-4.227, -70.365],
        [-4.227, -70.365],
        [-4.227, -70.365],
    ]

    new_coordinates = [
        [],
        [],
        [],
    ]

    print(len(my_coordinates))  # 3
    print(my_coordinates)
    try:
        if my_coordinates == [[], [], []]:
            print('Vacia')
            for i in range(len(my_coordinates)):
                for j in range(2):
                    coordinates = float(input('Ingrese la coordenada: '))
                    print(j)
                    if (coordinates >= -4.227 and coordinates <= -3.002 and j == 0) or (j == 1 and coordinates >= -70.365 and coordinates <= -69.714):
                        print('entre :D')
                        new_coordinates[i].append(coordinates)
                    else:
                        print("Error coordenada")
                        exit()
            my_coordinates = new_coordinates
        else:
            print('no vacia')
            for i in range(0, len(my_coordinates)):
                print(f'coordenada [latitud,longitud] {i+1} : {my_coordinates[i]}')
    except:
        my_coordinates = my_coordinates
        print('Error')


def run():
    contador = 1
    cod = '51604'
    pwd = '40615'
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
    username = input('Ingrese su usuario: ')

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

    if cod == username:
        password = input('Ingrese su contraseña: ')
        if password == pwd:
            result_capt = captcha(cod)
            if result_capt:
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
                        coordinates()
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
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')


if __name__ == '__main__':
    coordinates()
