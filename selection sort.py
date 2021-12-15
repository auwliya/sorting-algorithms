import numberrandomizer
import time

def selectionsort(list):
    for i in range(len(list)):
        smallest=list[i]
        to_switch=i
        for n in range(i,len(list)):
            if list[n]<smallest:
                smallest=list[n]
                to_switch=n

        list[to_switch]=list[i]
        list[i]=smallest      

    return list

list = numberrandomizer.randomizelist(1000)

time_start = time.perf_counter()
selectionsort(list)
time_end = time.perf_counter()

print(f"List: {list}, sorted in {time_end - time_start} seconds")