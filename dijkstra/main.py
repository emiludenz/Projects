class Node:
	def __init__(self):
		self.id = ""
		self.connected = []
		self.x = 0
		self.y = 0
		self.coordinates = [self.x,self.y]


class Edge:
	def __init__(self):
		self.connects = []
		self.w = 0
		self.direction = []
		self.x = 0
		self.y = 0
		self.coordinates = [self.x,self.y]


"""
Make a game of the Dijkstra algorithm
"""
import pygame
from pygame.locals import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((250,250))
	pygame.display.set_caption("Dijkstra Game")

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()


if __name__ == '__main__':
	main()