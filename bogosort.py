import random
import numberrandomizer
import time

#shuffles the list
def shufflelist(list):
    for index in range(len(list)):
        shuffle = random.randint(index,len(list) - 1)
        temp = list[index]
        list[index] = list[shuffle]
        list[shuffle] = temp

#grabs 2 numbers, if number 1 is larger than number 2, returns false
#if the entire list is sorted it returns true
def ordercheck(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True      

#shuffles the list until it is sorted
def bogosort(list):
    while ordercheck(list) == False:
        shufflelist(list)

#imports the numberrandomizer
#with bogo sort it is not reccomended to use large lists
list = numberrandomizer.randomizelist(10)

#starts counting the time, and stops when the list is sorted
time_start = time.perf_counter()
bogosort(list)
time_end = time.perf_counter()

#prints the sorted list and the time it took to sort it
print(f"List: {list}, sorted in {time_end - time_start} seconds")