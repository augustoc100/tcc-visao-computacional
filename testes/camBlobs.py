# coding: utf-8


"""
Primeiro prototipo da aplicação em SimpleCV
ele captura a imagem, depois procura os cantos da imagem chamado de blobs, 
depois eu pego o maior conjunto de cantos que se tornam algum objeto e deste objeto pergunto se é um circulo,
ou um retangulo, se for um dos dois peço para o simplcv desenhar um objeto envolvedo e pintando,
o objeto original, depois peço para ele me dar a cor em rgb deste obejto e printo no terminal
"""
from SimpleCV import Camera,Display,Color
import time
numero_da_cam = 0
reconhecimento = .2
cam = Camera(camera_index = numero_da_cam)
disp = Display()
cont = 0
while disp.isNotDone():
	img =cam.getImage().dilate(1).flipHorizontal()#.colorDistance(Color.BLACK)
	blobs = img.findBlobs()
	b = blobs[-1]
	if b.isCircle(reconhecimento):
		x= b.meanColor()
		print "cor "+ str(x)
		img.dl().text("circulo",(b.centroid()),Color.BLUE)
		img.drawCircle((b.centroid()),b.radius(),Color.BLUE,5)
	if b.isRectangle(reconhecimento - 0.1):
		img.dl().text("retangulo",(b.x*0.30 , b.y*0.30),Color.RED)

		img.dl().rectangle((b.x/2 , b.y/2),(b.x,b.y),color = Color.RED, width=2)
	

	img.show()
