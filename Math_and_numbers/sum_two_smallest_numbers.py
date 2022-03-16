def sum_two_smallest_numbers(mylist):
    new_list = sorted(mylist)
    return sum(new_list[:2])
    # return sum(sorted(mylist)[:2])


mylist = [5,8,12,1,22]
r = sum_two_smallest_numbers(mylist)
print(r)
