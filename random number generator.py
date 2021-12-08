from random import seed
from random import shuffle
# seed random number generator
seed(1)
# list from 0 to 99 (100 numbers)
list = [i for i in range(100)]
# randomly shuffle the list
shuffle(list)
print(list)