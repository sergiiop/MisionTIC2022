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


# choose_favorite(menu_option):
#    pass


def run():
    contador = 1
    cod = '51604'
    pwd = '40615'
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
    username = input('Ingrese su usuario: ')

    menu_option = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana', 'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo']
    
    menu = f"""
    Bienvenido
    1 - Cambiar contraseña 
    2 - Ingresar coordenadas actuales
    3 - Ubicar zona wifi más cercana
    4 - Guardar archivo con ubicación cercana
    5 - Actualizar registros de zonas wifi desde archivo
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
                            if is_valid :
                                system("cls")
                                menu = menu
                        elif option_fav == 2:
                            is_valid = validation()
                            if is_valid:
                                system("cls")
                                menu = """
                                Bienvenido
                                1 - Ingresar coordenadas actuales
                                2 - Cambiar contraseña
                                3 - Ubicar zona wifi más cercana
                                4 - Guardar archivo con ubicación cercana
                                5 - Actualizar registros de zonas wifi desde archivo
                                6 - Elegir opción de menú favorita
                                7 - Cerrar sesión.
                                """
                        elif option_fav == 3:
                            is_valid = validation()
                            if is_valid:
                                system("cls")
                                menu = """
                                Bienvenido
                                1 - Ubicar zona wifi más cercana
                                2 - Cambiar contraseña
                                3 - Ingresar coordenadas actuales
                                4 - Guardar archivo con ubicación cercana
                                5 - Actualizar registros de zonas wifi desde archivo
                                6 - Elegir opción de menú favorita
                                7 - Cerrar sesión.
                                """
                        elif option_fav == 4:
                            is_valid = validation()
                            if is_valid:
                                system("cls")
                                menu = """
                                Bienvenido
                                1 - Guardar archivo con ubicación cercana 
                                2 - Cambiar contraseña
                                3 - Ingresar coordenadas actuales
                                4 - Ubicar zona wifi más cercana
                                5 - Actualizar registros de zonas wifi desde archivo
                                6 - Elegir opción de menú favorita
                                7 - Cerrar sesión.
                                """
                        elif option_fav == 5:
                            is_valid = validation()
                            if is_valid:
                                system("cls")
                                menu = """
                                Bienvenido
                                1 - Actualizar registros de zonas wifi desde archivo 
                                2 - Cambiar contraseña
                                3 - Ingresar coordenadas actuales
                                4 - Ubicar zona wifi más cercana
                                5 - Guardar archivo con ubicación cercana
                                6 - Elegir opción de menú favorita
                                7 - Cerrar sesión. 
                                """
                        else:
                            print('Error')
                            break
                    elif option == 1:
                        print('Usted ha elegido la opción 1')
                        break
                    elif option == 2:
                        print('Usted ha elegido la opción 2')
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
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')


if __name__ == '__main__':
    run()
