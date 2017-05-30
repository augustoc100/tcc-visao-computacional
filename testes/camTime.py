# coding: UTF-8


"""
este ia tirar uma foto de meio em meio segundo depois subtrair uma imagem 
da outra e mostrando a diferença, para saber se tinha algum objeto novo aparecendo na imagem

"""
from SimpleCV import Camera,Display,Color
import time
numero_da_cam = 0
reconhecimento = -0.2
cam = Camera(camera_index = numero_da_cam)
disp = Display()
cont = 0
while disp.isNotDone():
	img = cam.getImage().colorDistance(Color.BLACK)
	img2 = cam.getImage()
	#time.sleep(0.5)
	#img2 = cam.getImage()
	#imgT = img2 - img
	#print "sleep"
	

	
	img.show()
	img2.show()

