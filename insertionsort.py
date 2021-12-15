import numberrandomizer
import time

def insertionsort(list):
    for index in range(1, len(list)):
        currentValue = list[index]
        currentPosition = index

        while currentPosition > 0 and list[currentPosition - 1] > currentValue:
            list[currentPosition] = list[currentPosition - 1]
            currentPosition = currentPosition - 1

        list[currentPosition] = currentValue

list = numberrandomizer.randomizelist(1000)

time_start = time.perf_counter()
insertionsort(list)
time_end = time.perf_counter()

print(f"List: {list}, sorted in {time_end - time_start} seconds")