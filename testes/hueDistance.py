from SimpleCV import Camera,Display,Color
cam = Camera()
disp = Display()

"""
Usado como o connceito base para o projeto final,
este programa pega uma imagem na camera, desta imagem ele 'distancia' as cores da imagem pela cor passada como prametro, ou seja se eu passo a cor preta
como parametro, toda a imagem ficara branca, menos os objetos pretos da imagem, resaltando assim a cor procurada,
depois subtraio esta imagem que resalta cor pela imagem colorida normal da camera, resultando assim em uma imagem qual completam,ente preta, meno a cor procurada, que sera a unica cooisa colorida na imagem

"""

while disp.isNotDone():
	img=cam.getImage().flipHorizontal()
	imgHue=img.colorDistance(Color.GREEN)#.hueDistance(Color.GREEN)
	teste = img - imgHue
	blobs=teste.findBlobs()
	'''if blobs[-1].isCircle(.25):
		blobs[-1].draw(width=-1,color= Color.BLUE)
		teste.dl().text(str(blobs[-1].meanColor()),(30,30),color=Color.RED)
		print "FODA-SE"
		'''
	teste.show()