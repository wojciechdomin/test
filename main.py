import math
import pygame


class Polygon: 
	#wypukły!!!!
	def __init__(self,vertices, position, angle):
		self.vertices = vertices
		self.position = position
		self.angle = angle



def get_polygon_coordinates(polygon):
	#działa ok, ale nieestetyczne
	pos_x = polygon.position[0]
	pos_y = polygon.position[1]
	angle = -polygon.angle
	polygon_coordinates = [(pos_x + x[0]*math.cos(angle) - x[1]*math.sin(angle) , pos_y + x[0]*math.sin(angle) + x[1]*math.cos(angle)) for x in polygon.vertices]
	return polygon_coordinates

def check_intersection(polygon1, polygon2):
	#some bulshit
	print("Nie zaimplementowano check_intersection")

#def draw_frame():
	

	# Set up the display
	
	

	# Colors
	

	# Display update

def scale(vertices, x_min, x_max, y_min, y_max, screen_width, screen_height):
	return [( (x - x_min) / (x_max - x_min) * screen_width, (y - y_min) / (y_max - y_min) * screen_height ) for x, y in vertices]

	


def main():
	p1 = Polygon([(0.0,0.0),(0.0,1.0),(1.0,1.0),(1.0,0.0)],[5.0,4.0],0)
	p2 = Polygon([(0.0,0.0),(0.0,2.0),(1.0,2.0),(1.0,0.0)],[3.0,2.0],0)
	print(get_polygon_coordinates(p1))
	
	print(get_polygon_coordinates(p1))

	# Inicjalizacja Pygame
	pygame.init()

	# Ustawienia okna
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Gra')

	# Kolory
	WHITE = (255, 255, 255)

	# Główna pętla gry
	running = True
	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False  # Zatrzymaj grę, jeśli użytkownik zamknie okno
		#Begin Logic	
		p1.angle += 0.05
		p1.position[0] += math.sin(p1.angle)*0.1
		p1.position[1] += math.cos(p1.angle)*0.1
		#End Logic
		screen.fill(WHITE)
		pygame.draw.polygon(screen, (0, 255, 0), scale(get_polygon_coordinates(p1),-10,10,-10,10,600,600))
		pygame.draw.polygon(screen, (28, 25, 255), scale(get_polygon_coordinates(p2),-10,10,-10,10,600,600))

		pygame.display.flip()
		pygame.time.Clock().tick(60)  # 60 FPS


	pygame.quit()



main()
