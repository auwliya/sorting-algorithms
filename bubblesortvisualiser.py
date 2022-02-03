import random
import pygame

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("bubblesort visualiser")

arr_clr =[(0, 204, 102)]*151
clr_ind = 0
clr =[(0, 204, 102), (255, 0, 0),
(0, 0, 153), (255, 102, 0)]

run = True

width = 900
length = 600

def randomizelist(x):
	sortlist = []
	for _ in range(x):
		sortlist.append(random.randint(0,x))
	return sortlist

sortlist = randomizelist(100)

def draw():
	element_width =(width-150)//150
	boundry_arr = 900 / 150
	boundry_grp = 550 / 100
	pygame.draw.line(screen, (0, 0, 0),
					(0, 95), (900, 95), 6)
	for i in range(1, 100):
		pygame.draw.line(screen,
						(224, 224, 224),
						(0, boundry_grp * i + 100),
						(900, boundry_grp * i + 100), 1)
	
	# Drawing the array values as lines
	for i in range(1, 100):
		pygame.draw.line(screen, arr_clr[i],\
			(boundry_arr * i-3, 100),\
			(boundry_arr * i-3, sortlist[i]*boundry_grp + 100),\
			element_width)

while run:
	# background
	screen.fill((255, 255, 255))
	# Event handler stores all event
	for event in pygame.event.get():
		# If we click Close button in window
		if event.type == pygame.QUIT:
			run = False
	draw()
	pygame.display.update()

print(f"{sortlist}")