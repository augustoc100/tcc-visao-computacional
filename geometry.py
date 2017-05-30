from SimpleCV import Color
import time
class Geometry():


	def __draw(self,b,img,lbs,cor):
		x,y = b.centroid()
		lb_certo,lb_errado = lbs

		red,green,_ = b.meanColor()


		num_certo_after =int(lb_certo.text)
		num_errado_after =int(lb_errado.text)

		b.draw(width =- 1, color=(255,255,255))
		img.drawText("detectado!!",x,y, color=cor, fontsize = 60)


		dists = b.distanceFrom()
		# distancia do centro
		if dists <= 40:

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
	
		print dists




	def __findBlobs(self, img):
		return img.findBlobs()[-1]



	def ehCirculo(self, img,cor,lbs):
		b = self.__findBlobs(img)

		if b.isCircle(.25):
			print "circle detected"
			self.__draw(b,img,lbs,cor)








	def ehRetangulo(self,img,cor,lbs):
		b = self.__findBlobs(img)
		
		if b.isRectangle(.1):

			print "RECTANGLE DETECTED!!!"
			self.__draw(b,img,lbs,cor)




			#img.dl().text(str(b.meanColor()),(30,30), Color.GREEN)
			#self.__getColor(img)

	#def __getColor(self,img):

	#	x=img.hueDistance(Color.GREEN)#(255,192,203))
		