def captcha(cod):
    # 51610
    first_term = int(cod[2:])  # 610
    second_term = (((5+1) - 6) * 1)  # = 1
    result_capt = first_term + second_term
    captcha_received = int(input((f'{first_term} + {second_term} = ')))
    if result_capt == captcha_received:
        return True
    else:
        return False


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
                print('Sesión iniciada')
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')


if __name__ == '__main__':
    run()
