# klasse for å ta og prosessere bile

from camera import Camera
import imager2 as IMR

class ProcessPic:

    def __init__(self):
        self.cam = Camera()
        #self.im = IMR.Imager("bilder/test2.png")
        self.s = 1

    def takePic(self):
        im = IMR.Imager(image=self.cam.update()).scale(self.s, self.s)
        #im.dump_image("/root/Oving6_Plab/basic_robot/bilder/bilde.png")
        return im


    def redShift(self, im):
        x, y = range(im.xmax), range(im.ymax)
        for i in y:
            for j in x:
                pix = im.get_pixel(j, i)
                if (pix[1] < 100) and (pix[2] < 100):
                    im.set_pixel(j, i, (255,0,0))
                else:
                    im.set_pixel(j, i, (0,0,255))
        return im

    def process(self):
        im = self.takePic()
        #nyIm = self.redShift(im)
        x, y = range(im.xmax), range(im.ymax)
        redCounter = 0
        for i in y:
            for j in x:
                pix = im.get_pixel(j, i)
                if pix[0] > 200 and (pix[1] < 80) and (pix[2] < 80):
                    redCounter += 1
        print(redCounter)
        if redCounter > 400:
            return 1000
        return 1

#test = ProcessPic()
#print(test.process())