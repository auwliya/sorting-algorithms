import random
import numberrandomizer

def shufflelist(list):
    for index in range(len(list)):
        shuffle = random.randint(index,len(list) - 1)
        temp = list[index]
        list[index] = list[shuffle]
        list[shuffle] = temp

def ordercheck(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True      

def bogosort(list):
    while ordercheck(list) == False:
        shufflelist(list)

list = numberrandomizer.randomizelist(10)
bogosort(list)

print(list)
