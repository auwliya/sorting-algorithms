from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random
import time

VALUE_MAX = 1000
VALUE_MIN = 1
SAMPLE_SIZE = 1000

data = [i for i in range(1, SAMPLE_SIZE + 1)]
random.shuffle(data)

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
        yield list
    return list

# NOTE: De uitkomst van Yield stoppen we nu steeds in
generator = selectionsort(data)
# NOTE: Dit geeft ons een 'figuur' met 'assen' waar we onze balkjes in kunnen plaatsen
fig, ax = plt.subplots()
# NOTE: Dit geeft ons balken, over de x-as telt het het aantal elementen over de y as komen de waardes uit de lijst
rects = ax.bar(range(len(data)), data)
# NOTE: Dit gebruiken we om een teller bij te houden die we in de visualisatie kunnen tonen
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]
# NOTE: Deze functie gaan we gebruiken om stapsgewijs te animeren

def animate(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))
# NOTE: We geven ons figuur mee, verwijzen naar de animatiefunctie, als argumenten moeten de balken en de teller mee, de 'yield'-waarde van de sort functie zijn de stappen/frames van de sortering, interval staat hoog zodat het goed te volgen is, 1 keer animeren is voldoende
anim = FuncAnimation(
    fig,
    func=animate,
    fargs=(rects, iteration),
    frames=generator,
    interval=200,
    repeat=False,
)
# NOTE: we tonen ons figuur, je kan ook de animatie opslaan met anim.save()
plt.show()