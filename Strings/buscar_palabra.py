def find_needle(mylist):
        return 'found the needle at position ' + str(mylist.index('needle'))


mylist = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
r = find_needle(mylist)
print(r)
