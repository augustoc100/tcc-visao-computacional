# coding: utf-8
from SimpleCV import Camera,Display,Color
import time
import numpy as np



cam = Camera(camera_index = 0)
disp = Display()
while disp.isNotDone():
	img= cam.getImage().flipHorizontal()
	blobs = img.findBlobs()

	areaAvg = np.mean(blobs.area())
	areaStd = np.std(blobs.area())
	teste = blobs.filter(blobs.area() < areaAvg+2.5*areaStd  )





"""
Ela deveria pegar a cor em RGB enviada como parametro no metodo sortColorDistance,
 procurar alguma coisa com essa cor na imagem e pintar este objeto de rosa (HOTPINK)

"""
	b = blobs[-1]
	#if b.isCircle(0.2):
	#	b.draw(width=-1,color = Color.RED)
	teste = teste.sortColorDistance(color = Color.BLUE)
	if teste:
		dists = teste[0:4].distanceFrom((img.width,0))

		#print teste
		#teste[0:1].draw(width = -1,color=Color.BLUE)
		location = np.where(dists==np.min(dists))[0][0]
		#print location
		#teste[location].crop().show()

		#teste[dists].crop().show()
		teste[location].draw(width=-1,color=Color.HOTPINK)

	


	
	

	
	
	img.show()
