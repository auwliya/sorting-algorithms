import numberrandomizer
import time

#The code searches through the list of numbers. It starts with the smallest number and compares all numbers after that with the smallest one.
#If there is one smaller, it compares all next numbers with that one. When it has found the smallest number and compared all numbers in the list,
#it switches the smallest number to the first position in the list. The next smallest number goes next to this first smallest number and so on.
#It loops until the list is sorted.
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

#The list gets set to the randomized amount of numbers.
list = numberrandomizer.randomizelist(10000)

#Runs the script and uses a timer to time how long it takes the selectionsort to run.
time_start = time.perf_counter()
selectionsort(list)
time_end = time.perf_counter()

#Prints the list and time so you can see the sorted list and how long it took.
print(f"List: {list}, sorted in {time_end - time_start} seconds")