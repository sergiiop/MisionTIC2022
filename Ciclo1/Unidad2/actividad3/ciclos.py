from datetime import datetime
from os import system


def greet():
    system("cls")
    print('Opción para saludar dependiendo de la hora')
    now = datetime.now()
    nombre = input('Ingrese su nombre: ')
    if(now.hour >= 4 and now.hour <= 12):
        print(f"Buenos Dias {nombre}, son las", now.hour)
    elif(now.hour >= 13 and now.hour <= 18):
        print(f"Buenos Tardes{nombre}, son las ", now.hour)
    else:
        print(f"Buenos Noches {nombre}, son las ", now.hour)


def is_even():
    system("cls")
    print('Opción para saber si un numero es par  o impar')
    number = float(input('Ingrese el numero: '))
    if number % 2 == 0:
        print(f'el numero {number} es par')
    else:
        print(f'el numero {number} es impar')


def average():
    system("cls")
    print('Opción para saber el promedio de 5 numeros')
    my_Array = []
    suma = 0
    
    for i in range(5):
        input_number = float(input('Ingrese un numero: '))
        my_Array.append(input_number)
    
    for j in my_Array:
        suma += j
    
    average = suma / (i+1)
    print(f'''
          El promedio de los numeros: {my_Array[0]}, {my_Array[1]}, {my_Array[2]}, {my_Array[3]}, {my_Array[4]} 
          es = {average}
          ''')


def module():
    system("cls")
    first_number = float(input('Ingrese el primer numero: '))
    second_number = float(input('Ingrese el segundo numero: '))
    if second_number != 0:
        module = first_number % second_number
        print(f'El modulo entre los numeros {first_number} y {second_number} es = {module}')
    else:
        print('Error, El segundo numero no puede ser 0')


def percentage():
    system("cls")
    number = float(input('Ingrese el numero a sacar porcentaje: '))
    porcentage = float(input('Ingrese el porcentaje que desea: '))
    total_procentage = (number * (porcentage / 100))
    print(f'El {porcentage}% de {number} es = {total_procentage}')


def potency():
    system("cls")
    number = float(input('Ingrese el numero a sacar potencia: '))
    potency = number ** 2
    print(f'La potencia de {number} es = {potency}')


def es_primo():
    system("cls")
    contador = 0
    print('Opción para si un numero es primo o no')
    number = int(input('Ingrese el numero para saber si es primo: '))
    
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1
    
    if contador == 0:
        print(f'el numero {number} es primo')
    else:
        print(f'el numbero {number} no es primo')


def run():
    menu = f"""
    Bienvenido
    1 - Saludar
    2 - Es par
    3 - Promedio
    4 - Módulo
    5 - Porcentaje
    6 - Potencia
    7 - Es primo
    0 - Salir.
    Elija una opción a realizar
    """
    
    intentos = 3
    
    while intentos != 0:
        sentinel = int(input(menu))
        if sentinel == 1:
            greet()
        elif sentinel == 2:
            is_even()
        elif sentinel == 3:
            average()
        elif sentinel == 4:
            module()
        elif sentinel == 5:
            percentage()
        elif sentinel == 6:
            potency()
        elif sentinel == 7:
            es_primo()
        elif sentinel == 0:
            print('Saliendo del programa...')
            exit()
        else:
            system("cls")
            intentos -= 1
            print(f'Opción incorrecta, te quedan {intentos} intentos')
            if intentos == 0:
                print('Saliendo del programa...')


if __name__ == "__main__":
    run()
