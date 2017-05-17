

class CtrlFirst():
	
	def __init__(self):
		

		from camera import CameraApp
		from geometry import Geometry
		self.cam = CameraApp()
		self.gem = Geometry()
#		self.certo=0
#		self.errado=0

	def iniciar(self,escolhas,lbs):
		lb_certo,lb_errado = lbs
		params = self.__parameters(escolhas) 
		print lb_certo

		self.cam.inicia(params,lb_certo.text)
		

	def __parameters(self, escolhas):
		
		cor = {
			"green2":(0,75,0),
			"orange":(237,84,18),
			"green":(0,128,0),
			"red": (100,2,3),
			"redTeste":(34,0,1),
			"greenTeste":(0,32,0),
			"red2":(84,18,0),
			"darkred": (107,1,0)
		}
		geometry , color = "",""
		if escolhas["forma"] == "circulo":
			geometry = self.gem.ehCirculo 
		else:
			geometry = self.gem.ehRetangulo

		if escolhas["cor"] == "verde":
			color = cor["green"]
		else:
			color = cor["red"]

		return geometry,color
'''
		print "start"
		self.cam.iniciar()


	def parar(self):
		self.cam.parar()

'''



'''

	def openCamera(self):
		from SimpleCV import Camera, Display, Color

		cam= Camera()
		disp = Display()
		while disp.isNotDone():
			img = cam.getImage()
			if disp.mouseLeft:
				img.drawCircle((10,10),10,Color.RED,5)

			img.show()
'''