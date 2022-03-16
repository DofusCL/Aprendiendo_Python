import math
import numpy as np
# help(math)

# Round The Numbers
value = 4.35
print(math.floor(value))

# Round to the top
print(math.ceil(value))

# look what happens with the Built in Function Round()
print(round(4.35))
# if you choose to round up or down  in python many times
# this applies the rule in the future so choose go odd or even
# as you go up and down
print(round(4.5))
print(round(5.5))

# number pi
print(math.pi)

from math import pi
print(pi)

print(math.inf)
print(math.nan)
print(math.e)
print(math.log(math.e))
print(math.sin(25))
print(math.degrees(pi/2))
print(math.radians(180))

# random module
import random

print("RanDOM")
# return some rand integer
test = random.randint(1,45000)
print(test)

# random item from list
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# grab multiples numbers
# Sample with Replacement
mychoise = random.choices(population=mylist, k=10)
print(mychoise)

# Sample Without Replacement
# Once a number is Chosen i would not get it a again
mychoise = random.sample(population=mylist, k=10)
print(mychoise)

# shuffle a list in place
# take in mind is permanently affected
newlist = mylist
random.shuffle(newlist)
print(newlist)

#uniform disfribution
uni = random.uniform(a=0,b=100)
print(uni)

# distribución Gausiana (Gauss distribution)
gauss = random.gauss(mu = 0, sigma = 1)
print(gauss)

# NUMPY
