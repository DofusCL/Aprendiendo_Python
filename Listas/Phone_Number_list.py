def create_phone_number(mylist):

    code = ''.join(map(str, mylist[:3]))
    first = ''.join(map(str, mylist[3:6]))
    second = ''.join(map(str, mylist[6:]))

    return "(" + code + ") " + first + " - " + second

mylist = list(range(0, 10))
r = create_phone_number(mylist)
print(r)




