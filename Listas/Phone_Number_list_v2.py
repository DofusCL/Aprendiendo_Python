def create_phone_number(mylist):
    n = ''.join(map(str, mylist))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])


mylist = list(range(0, 10))
r = create_phone_number(mylist)
print(r)
