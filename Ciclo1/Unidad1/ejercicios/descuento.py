def run():
    print('Calcular 15% de decuescuento')
    valor = int(input('Ingrese el valor de la compra: '))
    descuento = valor * 0.15
    valor_total = valor + descuento
    print(
        f'El 15% de {valor} es {descuento}\n El valor total a pagar es {valor_total}')


if __name__ == "__main__":
    run()
