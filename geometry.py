class Geometry():



	def ehCirculo(self, img,cor,lb):
		b = self.__findBlobs(img)


		if b.isCircle(.25):
			self.__draw(b,lb)
		

	def ehRetangulo(self,img,cor,lb):
		
		b = self.__findBlobs(img)
		
		if b.isRectangle(.1):

			print "RECTANGLE DETECTED!!!"
			self.__draw(b,lb)

	
	def __findBlobs(self, img):
		blobs = img.findBlobs()

		return blobs[-1]


	def __draw(self, b,lb):

		num_after = int(lb)
		
		b.draw(width =- 1, color=(255,255,255))
		dists = b.distanceFrom()
		color = b.meanColor()
		#print color == cor
		if dists <= 40:
			lb = str(num_after +1)
		print dists
