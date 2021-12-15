import random
import numberrandomizer

list = numberrandomizer.randomizelist(100)

def ordercheck(list):
    for index in range(len(list) - 1):
        if list[index] > list(index + 1):
            return False
    return True

def selectionsort(list):
    for index in range(len(list) - 1):
        smallest=list[index]
        switch=index
        for item in range(index, len(list)):
            if list[item] < smallest:
                smallest = list[item]
                switch = item
        return list

while ordercheck(list) == False:
    selectionsort(list)

print(list)