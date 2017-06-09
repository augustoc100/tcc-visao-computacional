from SimpleCV import Color, DrawingLayer
from time import sleep
class Geometry():
	def __draw_suport(self,img,b,lbs):
			dl = DrawingLayer((img.width, img.height))
			

			x,y = b.centroid()
			lb_certo,lb_errado = lbs




			b.draw(width =- 1, color=(255,255,255))
			img.drawText("detectado!!",x,y, color=Color.BLACK, fontsize = 60)

			dl.line((0,img.height/2),(img.width,img.height/2),Color.RED,width = 1, antialias = True, alpha = -1)
			dl.line((img.width/2,0 ),(img.width/2,img.height),Color.RED,width = 1, antialias = True, alpha = -1)

			return int(lb_certo.text),int(lb_errado.text),dl


	def __draw(self,b,img,lbs,cor):
		lb_certo,lb_errado = lbs
		red,green,_ = b.meanColor()

		num_certo_after,num_errado_after,dl = self.__draw_suport(img,b,lbs)
		dists = b.distanceFrom()
		# distancia do centro
		if dists <= 30:
			sleep(1)
			#testa se a cor que eu quero e que eh detectada sao vermelha
			if red > 50 and cor[0] > 50 or green >30 and cor[1] > 30 :

				lb_certo.text = str(num_certo_after+1)
			# Aprovados
				img.drawText(lb_certo.text,510,100, color=(0,255,0), fontsize = 100)		

			else:
				lb_errado.text = str(num_errado_after+1)

				#Reprovados 
				img.drawText(lb_errado.text,510,300, color=(250,0,0), fontsize = 100)

			print "menor"
			
		img.addDrawingLayer(dl)





	




	def __findBlobs(self, img):
		return img.findBlobs()[-1]



	def ehCirculo(self, img,cor,lbs):
		b = self.__findBlobs(img)

		if b.isCircle(.25):
			self.__draw(b,img,lbs,cor)








	def ehRetangulo(self,img,cor,lbs):
		b = self.__findBlobs(img)
		
		if b.isRectangle(.1):

			self.__draw(b,img,lbs,cor)



