


from SimpleCV import Camera, Display,Color
from geometry import Geometry 

class CameraApp():




	def __getParams(self,geometria):

		if geometria.__name__ == "ehCirculo":
			return "E um circulo? "
		else:
			return "E um retangulo?"

	#def parar(self):
	#	self.disp.done = True

		

	def inicia(self, params,lb):
		geometria, cor = params

		cam = Camera(camera_index= 1 )
		disp = Display()

		while disp.isNotDone():
		#	x = int(lb.text)
		#	lb.text = str(x+1)
			img = cam.getImage().flipHorizontal()

			if disp.mouseLeft:
				print "stop"

				disp.done =True

			imgHue = img.colorDistance(cor)
			imgTeste = img - imgHue
			imgTeste.drawText(self.__getParams(geometria),30,30, color=cor, fontsize = 50)

			geometria(imgTeste,cor,lb)
			imgTeste.show()

	

'''
		


cam = CameraApp()
gem = Geometry()

cam.inicia((gem.ehRetangulo, Color.BLUE ), "0")

'''