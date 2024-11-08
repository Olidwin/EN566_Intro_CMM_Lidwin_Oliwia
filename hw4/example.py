import random


#between 0 and 1

num = 0
for i in range(0,10000):
    coorx = random.random()
    coory = random.random()
    if ((coorx * coorx) + (coory*coory)) < 1.0:
        num = num + 1
        
print(4*num/10000)