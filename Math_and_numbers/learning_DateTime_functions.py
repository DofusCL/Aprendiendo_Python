import datetime

mytime = datetime.time(2, 20, 1, 43)
print(mytime)

print(mytime.minute)
print(mytime.hour)
print(mytime.microsecond)

print(type(mytime))


today = datetime.date.today() # european
print(today)
""" today.year
today.month
today.year
today.ctime
 """
# Date and Time
from datetime import datetime
mynewdt = datetime(2021, 10, 3, 14,20,13)
print(mynewdt)

# arithmetic datetime object
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
# we can check the difference in numbers of days
result = date1 - date2
print(result)
print(type(result))

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
result2 = datetime1 - datetime2
print(result2)
print(result2.seconds)
print(result2.total_seconds())
