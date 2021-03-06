from crash_sensor import Crash_sensor

__author__ = 'keithd'

from time import sleep
import random
import imager2 as IMR
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from FollowLine import FollowLine
from processPic import ProcessPic


## BE SURE TO RUN THESE DEMOS ON THE FLOOR or to have plenty of people guarding
## #  the edges of a table if it is run there.

# This just moves the robot around in a fixed dance pattern.  It uses no sensors.

##kommenter
def dancer():
    ZumoButton().wait_for_press()
    m = Motors()

    m.forward(.2,3)
    m.backward(.2,3)
    m.right(.5,3)
    m.left(.5,3)
    m.backward(.3,2.5)
    m.set_value([.5,.1],10)
    m.set_value([-.5,-.1],10)


def crashTest():
    ZumoButton().wait_for_press()

    sensor = Crash_sensor()

    motor = Motors()

    counter = 0
    f_value = sensor.calculateFront()
    ir_command = sensor.calculateSides()

    while True:

        counter += 1
        if counter >= 5:

            f_value = sensor.calculateFront()
            ir_command = sensor.calculateSides()
            counter = 0

        if ir_command == "LEFT":

            motor.left(0.5, 0.1)

        elif ir_command == "RIGHT":
            motor.right(0.5, 0.1)
        elif ir_command == "BACKWARD":
            motor.backward(0.3, 0.5)
        else:
            motor.forward(0.3, 0.01)

        if f_value == 1000:
            motor.stop()
            break







# This tests the UV (distance) sensors.  The robot moves forward to within 10 cm of the nearest obstacle.  It
# then does a little dancing before backing up to approximately 50 cm from the nearest obstacle.

def explorer(dist=10):
    ZumoButton().wait_for_press()
    m = Motors(); u = Ultrasonic()
    while u.update() > dist:
        m.forward(.2,0.2)
    m.backward(.1,.5)
    m.left(.5,3)
    m.right(.5,3.5)
    sleep(2)
    while u.update() < dist*5:
        m.backward(.2,0.2)
    m.left(.75,5)



def random_step(motors,speed=0.25,duration=1):
    dir = random.choice(['forward','backward','left','right'])
    eval('Motors.'+ dir)(motors,speed,duration)

# This moves around randomly until it gets to a dark spot on the floor (detected with the infrared belly sensors).
# It then rotates around, snapping pictures as it goes.  It then pastes all the pictures together into a
# panoramo view, many of which may be created per "vacation".

def tourist(steps=25,shots=5,speed=.25):
    ZumoButton().wait_for_press()
    rs = ReflectanceSensors(); m = Motors(); c = Camera()
    for i in range(steps):
        random_step(m,speed=speed,duration=0.5)
        vals = rs.update()
        if sum(vals) < 1:  # very dark area
            im = shoot_panorama(c,m,shots)
            im.dump_image('vacation_pic'+str(i)+'.jpeg')

def shoot_panorama(shots=5):
    camera = Camera()
    motors = Motors()
    s = 1
    im = IMR.Imager(image=camera.update()).scale(s,s)
    rotation_time = 3/shots  # At a speed of 0.5(of max), it takes about 3 seconds to rotate 360 degrees
    for i in range(shots-1):
        motors.right(0.5, rotation_time)
        im = im.concat_horiz(IMR.Imager(image=camera.update()))
    im.dump_image("/root/Oving6_Plab/basic_robot/bilder/test.png")
    return im

def followTest():
    ZumoButton().wait_for_press()
    m = Motors()
    follow = FollowLine()
    time = 0
    while(time < 100):
        values = follow.isOnLine()
        if values[0] == 0:
            m.forward(0.2, 0.2)
        elif values[1] == 0 or values[1]==1:
            m.left(0.2,0.3)
        else:
            m.right(0.2,0.3)
        time += 1

def cameraTest():
    camera = Camera()
    s = 1
    im = IMR.Imager(image=camera.update()).scale(s,s)
    im.dump_image("/root/Oving6_Plab/basic_robot/bilder/test2.png")


#dancer()
#crashTest()
#followTest()
#explorer()
#tourist()
#cameraTest()
#test = ProcessPic()
#test.process()
