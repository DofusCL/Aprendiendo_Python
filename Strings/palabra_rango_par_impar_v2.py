def even_words(word):
    for word in st.split():
        if len(word) % 2 == 0:
            print(word + ': su Largo es par')


st = input('Ingrese una frase: ')
even_words(st)
