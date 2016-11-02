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
        #self.im = self.takePic()
        x, y = range(self.im.xmax), range(self.im.ymax)
        counter = 0
        for i in x:
            for j in y:
                pix = self.im.get_pixel(i,j)
                print(pix)


#test = ProcessPic()
#test.process()