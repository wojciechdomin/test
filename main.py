import math


class Polygon:
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


def main():
	p1 = Polygon([(0.0,0.0),(0.0,1.0),(1.0,1.0),(1.0,0.0)],(5.0,4.0),0)
	p2 = Polygon([(0.0,0.0),(0.0,2.0),(1.0,2.0),(1.0,0.0)],(3.0,2.0),0)
	print(get_polygon_coordinates(p1))
	p1.angle = math.pi*0.5
	print(get_polygon_coordinates(p1))

main()