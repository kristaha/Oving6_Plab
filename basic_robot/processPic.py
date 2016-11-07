# klasse for å ta og prosessere bile

from camera import Camera
import imager2 as IMR

class ProcessPic:

    def __init__(self):
        self.cam = Camera()
        self.im = IMR.Imager("bilder/test2.png")
        self.s = 1

    def takePic(self):
        return IMR.Imager(image=self.cam.update().scale(self.s, self.s))

    def process(self):
        self.im = self.takePic()
        x, y = range(self.im.xmax), range(self.im.ymax)
        redCounter = 0
        for i in y:
            for j in x:
                pix = self.im.get_pixel(j, i)  # HAR BRUK BLÅ OG IKKE GRØNN!!!
                if pix[0] > 200 and pix[1] < 110:
                    redCounter += 1
        if redCounter >= 300:
            return 1000
        return 0

#test = ProcessPic()
#print(test.process())