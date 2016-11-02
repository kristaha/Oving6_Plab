from FollowLine import FollowLine
from crash_sensor import Crash_sensor


class Arbitrary:

    def __init__(self):

        self.crash_sensor = Crash_sensor()
        self.follow_line = FollowLine()



    def priority_sensor(self):

        pri_value_crash = self.crash_sensor.getPriValues()
        pri_value_follow = self.follow_line.isOnLine()

        value_list = [pri_value_crash[0], pri_value_follow[0]]
        sens_list = [self.crash_sensor, self.follow_line]
        highest_value = max(value_list)

        if highest_value == 0:
            return None

        for i in range(len(value_list)):

            if value_list[i] == highest_value:

                return sens_list[i]
















