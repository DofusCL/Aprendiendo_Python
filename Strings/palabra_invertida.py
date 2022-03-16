def master_yoda(word):
    # Genero una Nueva Lista con el método Split de mi palabra
    new_word = word.split()
    # Regreso un nuevo String unido por espacios con le método join, pero de forma inversa
    return new_word
    # return '.'.join(new_word[::-1])


the_word = input('Ingrese una Frase para separar: ')
r = master_yoda(the_word)
print(r)
