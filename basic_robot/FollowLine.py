# Klasse for å følge linje

from reflectance_sensors import ReflectanceSensors

class FollowLine:

    def __init__(self):
        self.reflectanseSensor = ReflectanceSensors()
        self.values = self.getValueList()

    def getValueList(self):
        self.reflectanseSensor.reset()
        self.reflectanseSensor.update()
        return self.reflectanseSensor.get_Value()

    def isOnLine(self):
        nowValue = self.getValueList()
        offLineList = [0,1,4,5]
        for i in range(len(self.values)):
            if i in offLineList and nowValue[i] > 500:
                return [nowValue[i],i]
        return [0,10]

    # I arbitary klassen bruker jeg bare retur vediene til isOnLine() som prioriteringsverdier
    # Da blir det priverdier mellom 0-1000
    











