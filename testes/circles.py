
"""
ia analisar a imagem a procura de circulos e mostar a distancia que este circulo estara do centro da imagem,
quando chegasse ´proximo do centro ele contaria por quanto tempo este objeto permaneceu parado, e se fosse pouco tempo 
siguinifacria que este objeto esta em movimento, e é apenas um, contando um objeto procurado pelo usuario e printaria no terminal

"""

from SimpleCV import Camera,Display,Color
import time
import numpy as np


cam = Camera(camera_index = 0)
disp = Display()
num = 0
tempo = []

while disp.isNotDone():
	img = cam.getImage().flipHorizontal()
	circle = img.findCircle()
	blobs = img.findBlobs()
	b = blobs[-1]
	if b.isCircle(.2):
		img.drawCircle((b.centroid()),b.radius(),Color.BLUE,3) 		#print "here" + str(num)
		x=b.distanceFrom()
		if  x<50:
			tempo.append(time.time())
			diff =tempo[-1] - tempo[0]
			if diff > 1.5 :
				num +=1
				tempo = []
				 num 
				continue	
	

	
	
	img.show()
