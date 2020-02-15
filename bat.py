import numpy as np

class Bat:

    def __init__(self, mode = 'simulation'):

        self.base_x = params.bat_base_x
        self.base_y = params.bat_base_y
        self.base_z = params.bat_base_z

        self.theta = 0
        self.length = params.bat_length

        self.bat_height = params.bat_base_height


    def change_theta(self, new_theta):

        self.theta = new_theta

        #send signal to robot

    def swing_bat(self):

        self.change_theta(0)
        n = 10

        for i in range(n):
            angle = (i / n)*(2 * np.pi)
            self.change_theta(angle)
