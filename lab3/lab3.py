from graph import *
import math 


def background():
	penColor(0, 255, 255)
	brushColor('PaleTurquoise')
	rectangle(0,0, 500,300)
	brushColor('ForestGreen')
	rectangle(0,300, 500,600)
background()
penColor(0,0,0)


def house(x, y, z):
	'''
	 z - difference
	'''
	brushColor('MediumOrchid')
	rectangle(x,y, x+z*4, y+z*3)
	brushColor('Plum')
	polygon([(x,y), (x+z*2,y-z*2), (x+z*4, y)])
	brushColor('Thistle')
	rectangle(x+z*1.5,y+z, x+z*2.5,y+z*2)

house(50, 250, 50)


def cloud(x, y, radius, z):
	penColor('Gray')
	brushColor('White')
	for i in range(4):
		circle(x,y,radius)
		x += z*3
	for i in range(2):
		circle(x-z*6,y-z*2,radius)
		x -= z*3
cloud(230,120,30,10)


def wood(x, y, radius, z):
	penSize(20)
	penColor('Black')
	moveTo(x,y+z*2)
	lineTo(x,y+z*6)
	penSize(1)
	brushColor('DarkGreen')
	for i in range(2):
		circle(x,y,radius)
		circle(x-z,y+z,radius)
		circle(x+z,y+z,radius)
		y+=40
		z-=5
wood(430,200,30,30)



def sun(x, y, r, rs):			
	brushColor('PaleGoldenrod')
	polygon([(x + r*math.cos(0.5), y + r*math.sin(0.5)),
	(x + rs*math.cos(0.75), y + rs*math.sin(0.75)),
	(x + r*math.cos(1), y + r*math.sin(1)),
	(x + rs*math.cos(1.25), y + rs*math.sin(1.25)),
	(x + r*math.cos(1.5), y + r*math.sin(1.5)),
	(x + rs*math.cos(1.75), y + rs*math.sin(1.75)),
	(x + r*math.cos(2), y + r*math.sin(2)),
	(x + rs*math.cos(2.25), y + rs*math.sin(2.25)),
	(x + r*math.cos(2.5), y + r*math.sin(2.5)),
	(x + rs*math.cos(2.75), y + rs*math.sin(2.75)),
	(x + r*math.cos(3), y + r*math.sin(3)),
	(x + rs*math.cos(3.25), y + rs*math.sin(3.25)),
	(x + r*math.cos(3.5), y + r*math.sin(3.5)),
	(x + rs*math.cos(3.75), y + rs*math.sin(3.75)),
	(x + r*math.cos(4), y + r*math.sin(4)),
	(x + rs*math.cos(4.25), y + rs*math.sin(4.25)),
	(x + r*math.cos(4.5), y + r*math.sin(4.5)),
	(x + rs*math.cos(4.75), y + rs*math.sin(4.75)),
	(x + r*math.cos(5), y + r*math.sin(5)),
	(x + rs*math.cos(5.25), y + rs*math.sin(5.25)),
	(x + r*math.cos(5.5), y + r*math.sin(5.5)),
	(x + rs*math.cos(5.75), y + rs*math.sin(5.75)),
	(x + r*math.cos(6), y + r*math.sin(6)),
	(x + rs*math.cos(6.25), y + rs*math.sin(6.25)),
	(x + r*math.cos(6.5), y + r*math.sin(6.5)),
	(x + rs*math.cos(6.75), y + rs*math.sin(6.75)),
	(x + r*math.cos(0.5), y + r*math.sin(0.5))
	])
sun(450, 50, 30, 35)


run()
