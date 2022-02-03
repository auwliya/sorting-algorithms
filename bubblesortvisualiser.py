import random
import pygame
pygame.font.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("bubblesort visualiser")

run = True

width = 900
length = 600
line_color = [(89, 205, 144)]*151
color = [(89, 205, 144), (255, 0, 0), (0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)

def randomizelist():
	list_sort = []
	for _ in range(151):
		list_sort.append(random.randint(0,151))
	return list_sort

list_sort = randomizelist()

def draw():
	# Text should be rendered
	txt = fnt.render("PRESS 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0))
	# Position where text is placed
	screen.blit(txt, (10, 0))
	txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.", 1, (0, 0, 0))
	screen.blit(txt1, (10, 30))
	txt2 = fnt1.render("ALGORITHM USED: BUBBLE SORT", 1, (0, 0, 0))
	screen.blit(txt2, (550, 60))
	element_width =(width-150)//150
	boundry_arr = 900 / 150
	boundry_grp = 550 / 100
	pygame.draw.line(screen, (0, 0, 0),
					(0, 95), (900, 95), 6)
	for i in range(1, 151):
		pygame.draw.line(screen,
						(224, 224, 224),
						(0, boundry_grp * i + 100),
						(900, boundry_grp * i + 100), 1)
	
	# Drawing the array values as lines
	for i in range(1, 151):
		pygame.draw.line(screen, line_color[i],\
			(boundry_arr * i-3, 100),\
			(boundry_arr * i-3, list_sort[i]*boundry_grp + 100),\
			element_width)

while run:
	# background
	screen.fill((255, 255, 255))
	# Event handler stores all event
	for event in pygame.event.get():
		# If we click Close button in window
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				randomizelist()
	draw()
	pygame.display.update()