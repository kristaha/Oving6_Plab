from motors import Motors
from ultrasonic import Ultrasonic


class Crash_sensor():

    def __init__(self):

        self.k = 0


    def calculate(self):

        u_sensor = Ultrasonic()

        motors = Motors()



        while True:

            u_sensor.update()
            distance = u_sensor.get_value()
            if distance < 20:
                motors.stop()
                break
            motors.forward(.2, 3)













    #Ultraviolet og 