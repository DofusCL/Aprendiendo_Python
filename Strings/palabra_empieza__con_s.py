def palabra(word):
   wrd = 0
   for word in the_word.split():
       if word[0].lower() == 's':
           wrd += 1
           print(word)
   if wrd == 0:
           print('No hay palabras con "s" que mostrar')


the_word = input('Ingrese una palabra o frase que empìece con "s" : ')
palabra(the_word)
