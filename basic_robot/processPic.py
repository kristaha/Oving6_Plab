# klasse for å ta og prosessere bile

from camera import Camera
import imager2 as IMR

class ProcessPic:

    def __init__(self):
        self.cam = Camera()
        self.im = None  # IMR.Imager("bilder/test2.png")
        self.s = 1

    def takePic(self):
        return IMR.Imager(image=self.cam.update().scale(self.s, self.s))

    def process(self):
        self.im = self.takePic()
        x, y = range(self.im.xmax), range(self.im.ymax)
        redCounter = 0
        blueCounter = 0
        for i in x:
            for j in y:
                pix = self.im.get_pixel(i,j) # HAR BRUK BLÅ OG IKKE GRØNN!!!
                if (pix[1] < 100) and (pix[2] < 100):
                    redCounter += 1
                elif (pix[0] < 100) and (pix[1] < 100):
                    blueCounter += 1
        if redCounter > 400:
            return 1000
        elif blueCounter > 400:
            return 0
        else:
            self.process()