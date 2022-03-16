def the_twenty(x, y):
    suma = x + y
    return suma == 20 or x == 20 or y == 20


a = int(input('Escriba un Número: '))
b = int(input('Escriba un Número: '))

r = the_twenty(a, b)
if r:
    print('Uno de los números, o la Suma, coinciden con 20')
else:
    print('Ni la Suma ni los Números son 20')
