for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} -> clave: Mk')
    elif num % 3 == 0:
        print(f'{num} -> clave: 3M')
    elif num % 5 == 0:
        print(f'{num} -> clave: 5M')
    else:
        print(num)
