from irproximity_sensor import IRProximitySensor
from motors import Motors
from ultrasonic import Ultrasonic


class Crash_sensor():

    def __init__(self):

        self.pri_value = 0

        self.IR_command = ""

    def calculateFront(self):

        u_sensor = Ultrasonic()
        u_sensor.update()
        distance = u_sensor.get_value()
        if distance < 10:
            self.pri_value = 1000

        else:
            self.pri_value = 0

        return self.pri_value

    def calculateSides(self):

        ir_proxy_sensor = IRProximitySensor()
        ir_proxy_sensor.update()

        values = ir_proxy_sensor.get_value()

        if values[0] == values[1] == False or values[0] == values[1] == True and self.pri_value == 0:

            self.IR_command = "FORWARD"
        elif values[0] == values[1] == False or values[0] == values[1] == True and self.pri_value == 1000:
            self.IR_command = "BACKWARD"

        elif values[1] == True and values[0] == False:
            self.IR_command = "RIGHT"
            self.pri_value = 1000

        elif values[0] == True and values[1] == False:
            self.IR_command = "LEFT"
            self.pri_value = 1000

        return self.IR_command


    #def getPriValues(self):

#        return[self.calculateFront(), self.calculateSides()]

    def getPriValues(self):

        return[self.pri_value, self.calculateSides()]


