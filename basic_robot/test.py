# test for å gjøre om bilde til tre hovedfarger

from camera import Camera
import imager2 as IMR

class ProcessPic:

    def __init__(self):
        self.cam = Camera()
        self.im = IMR.Imager("bilder/test2.png")
        self.s = 1

    def takePic(self):
        return IMR.Imager(image=self.cam.update().scale(self.s, self.s))

    def redShift(self, im):
        x, y = range(im.xmax), range(im.ymax)
        for i in y:
            for j in x:
                pix = im.get_pixel(j, i)  # HAR BRUK BLÅ OG IKKE GRØNN!!!
                if (pix[1] < 100) and (pix[2] < 100):
                    im.set_pixel(j, i, (255,0,0))
                else:
                    im.set_pixel(j, i, (0,0,255))
                    counter = 0
        im.display()
        return im

    def process2(self):
        # self.im = self.takePic()
        nyIm = self.redShift(self.im)
        x, y = range(nyIm.xmax), range(nyIm.ymax)
        redCounter = 0
        for i in y:
            for j in x:
                pix = nyIm.get_pixel(j, i)  # HAR BRUK BLÅ OG IKKE GRØNN!!!
                print(pix)
                if pix[0] > 200 and pix[1] < 110:
                    redCounter += 1
        print(redCounter)
        if redCounter > 800:
            return 1000
        return 1

    def process3(self):
        # self.im = self.takePic()
        x, y = range(self.im.xmax), range(self.im.ymax)
        redCounter = 0
        blueCounter = 0
        oppeVenstreRød, nedeHøyreRød, oppeVenstreGrønn, nedeHøyreGrønn = None, None, None, None
        for i in y:
            for j in x:
                pix = self.im.get_pixel(j, i)  # HAR BRUK BLÅ OG IKKE GRØNN!!!
                if (pix[1] < 100) and (pix[2] < 100):
                    if redCounter == 0:
                        oppeVenstreRød = [j, i]
                        redCounter += 1
                    nedeHøyreRød = [j, i]
                elif (pix[0] < 100) and (pix[1] < 100):
                    if blueCounter == 0:
                        oppeVenstreGrønn = [j, i]
                        blueCounter += 1
                    nedeHøyreGrønn = [j, i]
        print(oppeVenstreRød, nedeHøyreRød, oppeVenstreGrønn, nedeHøyreGrønn)
        print(min([oppeVenstreRød[0], nedeHøyreRød[0]]) * min([oppeVenstreRød[1], nedeHøyreRød[1]]))
        print(min([oppeVenstreGrønn[0], nedeHøyreGrønn[0]]) * min([oppeVenstreGrønn[1], nedeHøyreGrønn[1]]))
        if redCounter > 400:
            return 1000
        elif blueCounter > 400:
            return 0
        else:
            pass  # self.process()


#test = ProcessPic()
#print(test.process2())

