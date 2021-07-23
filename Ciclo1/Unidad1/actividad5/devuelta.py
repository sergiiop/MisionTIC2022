SALDO = 10000

valor_compra = int(input('Ingrese el valor de la compra: '))

if SALDO >= valor_compra:
    SALDO -= valor_compra
    print(f'Su devuelta es ${SALDO}')
else:
    print('Saldo insuficiente')
