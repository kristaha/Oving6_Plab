from basic_robot.motors import Motors
from basic_robot.ultrasonic import Ultrasonic


class Crash_sensor():

    def __init__(self):

        self.k = 0


    def calculate(self):

        u_sensor = Ultrasonic()

        motors = Motors()

        motors.forward(.2, 3)

        u_sensor.update()
        distance = u_sensor.get_value()

        if distance < 3:

            motors.stop()







    #Ultraviolet og 