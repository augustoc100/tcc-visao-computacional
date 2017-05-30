"""
Tutorial pego na internet ensinando a pegar movimentação na imagem, trakeando movimento

"""


# coding: utf-8
from SimpleCV import Camera,Display,Color
import time
import numpy as np

scaler = 1

cam = Camera(camera_index = 0)
disp = Display()
last = cam.getImage().scale(scaler)
sz = last.width/10

while disp.isNotDone():
	img = cam.getImage().scale(scaler)
	motion = img.findMotion(last,sz,method='HS')
	motion.draw(color=Color.BLUE,width=1)


	
	

	
	
	img.show()
