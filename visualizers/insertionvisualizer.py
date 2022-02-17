from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random

VALUE_MAX = 1000
VALUE_MIN = 1
SAMPLE_SIZE = 100

# Dit is de visualizer van de Insertion Sort

# NOTE: Ik heb jullie functie herschreven met een List Comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
# data = [random.randrange(VALUE_MIN, VALUE_MAX, 1) for i in range(SAMPLE_SIZE)]
# NOTE: Als alternatief zou je ook een lijst van maken met oplopende nummers en die door elkaar zetten

data = [i for i in range(1, SAMPLE_SIZE + 1)]
random.shuffle(data)

def insertionsort(list):
    for index in range(1, len(list)):
        currentValue = list[index]
        currentPosition = index - 1

        while currentPosition >= 0 and currentValue < list[currentPosition]:
            list[currentPosition + 1] = list[currentPosition]
            currentPosition -= 1

        list[currentPosition + 1] = currentValue
        yield list
    return list

# NOTE: De uitkomst van Yield stoppen we nu steeds in
generator = insertionsort(data)
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