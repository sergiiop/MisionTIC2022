import math

def run():
    print('Calculo de Hipotenusa')
    first_cat = int(input('Ingrese el primer cateto: '))
    second_cat = int(input('Ingrese el segundo cateto: '))
    print(first_cat*first_cat)
    print(second_cat * second_cat)
    hipotenusa = math.sqrt((first_cat*first_cat) + (second_cat*second_cat))
    print(f'el resultado de la hipotenusa, de los catetos {first_cat} y {second_cat} es {hipotenusa}')


if __name__ == "__main__":
    run()
