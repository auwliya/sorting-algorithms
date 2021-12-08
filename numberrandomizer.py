import random

def randomizelist(x):
    list = []
    for _ in range(x):
        list.append(random.randint(0,x))
    return list



