def palabra(word):
    new_list = word.split()
    print('Palabras Ingresadas: %i' % (len(new_list)))
    if len(new_list) != 2:
        print('La lista debe contener 2 palabras')
        return None
    else:
        return new_list[0][0] == new_list[1][0]


# Pido al usuario un String
the_word = input('Ingrese una frase de 2 palabras: ')

# Ejecuto y regreso el resultado
r = palabra(the_word)
# valido que sólo imprima algo si el return es booleano
# Puedo reemplazar if (r == True) por su equivalente if r:  ya que estoy automáticamente apuntando a su Veracidad
if r is not None:
    if r:
        print('Empiezan con la misma letra')
    else:
        print('Empiezan con lertas diferentes')
