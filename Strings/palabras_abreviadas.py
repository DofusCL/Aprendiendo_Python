def abrev_name(name):
    lista = [word[0] for word in name.split()]
    # return lista
    return '.'.join(lista).title()

name = 'Chaparrito GOnzales'
r = abrev_name(name)
print(r)
