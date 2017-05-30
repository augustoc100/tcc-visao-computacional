

class CtrlFirst():
	
	def __init__(self):
		from camera import CameraApp
		from geometry import Geometry
		self.cam = CameraApp()
		self.gem = Geometry()
		self.certo=0
		self.errado=0

	def iniciar(self,escolhas,lbs):
		params = self.__parameters(escolhas) 

		self.cam.inicia(params,lbs)
		

	def __parameters(self, escolhas):
		
		cor = {
			"green2":(0,75,0),
			"orange":(237,84,18),
			"green":(0,128,0),
			"red": (100,2,3),
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
