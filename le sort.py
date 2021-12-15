import random
import numberrandomizer
import time

#le sort was a mistake made during an attempt to make the bubble sort
#the list accidentally turned every number into the previous one, and after a change it only printed "le sort"
#in this file it was remade as a joke, but it actually works as a le sort

def swapnumbers(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            temp = list[index + 1]
            list[index] = list[index + 1]
            list[index] = temp
        
        elif list[index] < list[index + 1]:
            temp = list[index + 1]
            list[index] = list[index + 1]
            list[index] = temp            

def ordercheck(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True      

def bubblesort(list):
    while ordercheck(list) == False:
        swapnumbers(list)

list = numberrandomizer.randomizelist(1000)

time_start = time.perf_counter()
bubblesort(list)
time_end = time.perf_counter()

print(f"List: {list}, sorted in {time_end - time_start} seconds")