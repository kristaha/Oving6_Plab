from motors import Motors
from Arbitrary import Arbitrary
from types import *
from FollowLine import FollowLine
from crash_sensor import Crash_sensor
from zumo_button import ZumoButton

class MotorAction():

    def __init__(self):

        self.arbit = Arbitrary()
        self.value = None
        self.motorList = []

        self.motorList.append(Motors())

    def UpdateValue(self):
        self.value = self.arbit.priority_sensor()

    def getValue(self):
        return self.value

#Handlinger ved forskjellige pri_sensorer
    def crash(self, value):
        if value == 'FORRWARD':
            self.motorList[0].stop()
            self.motorList[0].backward(0.2,0.4)
        elif value == 'LEFT':
            self.crashLeft()
        else:
            self.crashRight()

    def crashLeft(self):
        self.motorList[0].stop()
        self.motorList[0].right(0.2,0.4)

    def crashRight(self):
        self.motorList[0].stop()
        self.motorList[0].left(0.2, 0.4)

    def followLine(self,indexOfSensor):

        if indexOfSensor == 0 or indexOfSensor ==1:
            self.motorList[0].left(0.2,0.3)
        else:
            self.motorList[0].right(0.2,0.3)

    def camera(self,value):

        if value ==1:
            self.motorList[0].stop()
        else:
            self.motorList[0].forward(0.6,0.2)

    def noPri(self):
        self.motorList[0].forward(0.2,0.3)

## Kjøre def
    def drive(self):

        ZumoButton().wait_for_press()
        time = 0
        while( time < 300):
            time += 1
            self.UpdateValue()
            value = self.getValue()

            if value == None:

                self.noPri()

            elif type(value) == FollowLine():

                self.followLine(value.getPriValues()[1])

            elif type(value) == Crash_sensor:

                self.crash(value.getPriValues()[1])
            else:
                self.camera(0)
            

run = MotorAction()
run.drive()









