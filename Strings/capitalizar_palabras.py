def capitalizar(word):
    if len(word) > 3:
        # Desde el principio hasta el 4to espacio y del 4to espacio al final
        return word[:3].capitalize() + word[3:].capitalize()
    else:
        return None


the_word = input('Ingrese una palabra: ')
r = capitalizar(the_word)
if r is None:
    print('La palabra debe contener 4 o más letras')
else:
    print(r)
