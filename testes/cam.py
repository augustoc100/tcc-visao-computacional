


from SimpleCV import Camera, Display, Color,DrawingLayer
cam = Camera()
img = cam.getImage()
disp = Display((1000,1000))

normalDisplay = True
while disp.isNotDone():
	img = cam.getImage()
	dl = DrawingLayer((img.width, img.height))

	myString1 = "( "+str(disp.mouseRawX) + " " + str(disp.mouseRawY)+" )"
	#print(myString1)
	#print(img.width)
	#print( (display.mouseX,display.mouseY))
	if disp.mouseLeft:
		propriedades = cam.getAllProperties()
		print(propriedades)

	img.dl().ezViewText(myString1,(30,30))
	inicio = (0,img.height/2)
	fim = (img.width,img.height/2)
	dl.line(inicio,fim,Color.RED,width = 3, antialias = True, alpha = -1)
	img.addDrawingLayer(dl)

	img.show()

"""
	time.sleep(0.01)
	dist = img.colorDistance(Color.BLACK).dilate(10)
	segmented = dist.stretch(200,255)
	blobs = segmented.findBlobs()
	mouse = disp.mousex
	print(mouse)
	if disp.mouseLeft:
		normalDisplay = not(normalDisplay)

	if normalDisplay:
		img.show()
	else:
		segmented.show()

"""