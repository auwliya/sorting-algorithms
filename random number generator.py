from random import seed
from random import shuffle
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(100)]
# randomly shuffle the sequence
shuffle(sequence)
print(sequence)