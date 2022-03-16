def tofarh(celsius):
    farh = float((9/5)*celsius + 32)
    print(f'{celsius} Celsius equivalen a {farh:2.2f} Fahrenheit')


grados = float(input('Ingrese los grados Celsius de su ubicación: '))
tofarh(grados)
