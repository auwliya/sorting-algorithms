import numberrandomizer
import time

def swapnumbers(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            list[index], list[index + 1] = list[index + 1], list[index]

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