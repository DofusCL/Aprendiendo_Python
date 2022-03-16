from random import shuffle

def shuffle_list(gamelist):
    shuffle(gamelist)
    return gamelist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Escoge un Numero 0, 1 o 2: ")
    return int(guess)


def check_guess(mixed_list, usr_guess):
    if mixed_list[usr_guess] == 'O':
        print("Has Adivinado")
    else:
        print("Error! No has adivinado")
        print(mixed_list)


# iniciamos la lista
mylist = [' ', 'O', ' ']

# revolvemos el contenido
mixed_list = shuffle_list(mylist)

# preguntamos al usuario dónde está la bolita
usr_guess = player_guess()

# chequeamos el resultado del usuario
check_guess(mixed_list, usr_guess)
