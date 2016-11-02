# Klasse for å følge linje

from reflectance_sensors import ReflectanceSensors

class FollowLine:

    def __init__(self):
        self.reflectanseSensor = ReflectanceSensors()
        self.values = self.getValueList()
        self. values = self.isOnLine()

    def getValueList(self):
        self.reflectanseSensor.reset()
        self.reflectanseSensor.update()
        return self.reflectanseSensor.get_value()

    def isOnLine(self):
        nowValue = self.getValueList()
        offLineList = [0,1,4,5]
        for i in range(len(self.values)):
            if i in offLineList and nowValue[i] < 0.2:
                return [(1000-(nowValue[i]*1000)),i]
        return [0,10]

    def getPriValues(self):
        return self.isOnLine()

    # I arbitary klassen bruker jeg bare retur vediene til isOnLine() som prioriteringsverdier
    # Da blir det priverdier mellom 0-1000












