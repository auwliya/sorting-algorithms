import numberrandomizer
import time

#grabs two numbers if number 1 is larger than number 2, it swaps their position.
#it keeps running through the list until it is sorted.
def swapnumbers(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            list[index], list[index + 1] = list[index + 1], list[index]

#checks whether the list is sorted or not
#if it isn't sorted it returns False
def ordercheck(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True      

#while ordercheck returns flase, it keeps swapping the numbers.
def bubblesort(list):
    while ordercheck(list) == False:
        swapnumbers(list)

#imports the numberrandomizer
#bubble sort can handle bigger lists
list = numberrandomizer.randomizelist(1000)

time_start = time.perf_counter()
bubblesort(list)
time_end = time.perf_counter()

print(f"List: {list}, sorted in {time_end - time_start} seconds")