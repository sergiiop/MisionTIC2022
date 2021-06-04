menu = """
Bienvenido A nuestra calculadora 🖩
1 - Suma
2 - Resta
3 - Multiplicacion
4 - División
5 - Potencia
Elige la operación a realizar: """

opcion = int(input(menu))

if opcion == 5: #Si es potencia entra a este condicional
    num = int(input('Ingrese el numero a potenciar: '))
    resultado = num ** 2
    print(resultado)
else: # Si no valida el resto de operaciones
    num_1 = int(input('Ingrese el primer numero: '))
    num_2 = int(input('Ingrese el segundo numero: '))
    if opcion == 1: # Valida la resta
        suma = num_1 + num_2
        print(f'el resultado de la suma es = {suma}')
    elif opcion == 2: # Valida la resta
        resta = num_1 - num_2
        print(f'el resultado de la resta es = {resta}')
    elif opcion == 3: #Valida la Multiplicación
        multi = num_1 * num_2
        print(f'el resultado de la multiplicacion es = {multi}')
    elif opcion == 4: # Valida la división
        if num_2 != 0: #Valida que el denominador sea diferente de 0
            div = num_1 / num_2
            print(f'el resultado de la División es = {div}')
        else:
            print('La division no es valida')
    else:
        print('Ingrese una operacion valida')
