#! python3
#Jeffrey Gearhart CST-205-01 
#Median Value image blending 

from Pil import Image
from statistics import Median
filelist ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg']
im =[]
pictureWidth= im[0].width
pictureHeight= im[0].height
outputImage= Image.new('RGB'(pictureWidth, pictureHeight))
outputImagePixelAccess= outputImage.load()
for imagefile in filelist:
	im.append = Image.open()
for x in range(0,pictureWidth):
	for y in range(0,pictureHeight):
		for myImage in theImages:

			myRed, myGreen, myBlue = myImage.getpixel((x,y))

			redPixelList.append(myRed)
			greenPixelListapend(myGreen)
			bluePixelList.append(myBlue)
		medianRed= int(Median(redPixelList))
		medianGreen= int (Median(greenPixelList))
		medianBlue= int (Median(bluePixelList))
		outputImagePixelAccess[x,y]= (medianRed, medianGreen, medianBlue)
outputImage.save= finished.png