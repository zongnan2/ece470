import params
import smart_velocity_finder
import numpy as np
import time

class Ball:

    def __init__(self, mode = 'simulation'):

        self.base_x = params.ball_base_x
        self.base_y = params.ball_base_y
        self.base_z = params.ball_base_z
        self.radius = params.ball_radius

        self.y = self.base_y
        self.vy = 0
        self.gy = params.gravity

        self.mode = mode
        self.last_shot = 0

        self.time_steps = np.array([ time.time()])
        self.y_history = np.array([ self.vy ])


        pass

    def shoot(self):

        if self.mode == 'simulation':
            self.vy = params.ball_v0

        if self.mode == 'real':

            #not yet connected or built
            #send shooting signal to the module
            pass

        self.last_shot = time.time()

    def move(self):

        ct = time.time()
        self.time_steps = np.append(self.time_steps, ct)
        dt = self.time_steps[-1] - self.time_steps[-2]

        if self.mode == 'simulation':
            y = self.y + self.vy*dt + 0.5*self.gy*dt**2

        if self.mode == 'real':
            y = self.get_ball_height()

        if y < 0:
            y = 0

        self.y_history = np.append(self.y_history, y)
        self.y = y

        if y > 0:
            self.update()

        else:
            self.vy = 0

    def update(self):

        n = self.steps_since_shot()
        if n >= 2:
            self.vy = smart_velocity_finder.find_velocity( self.time_steps[-(n):], self.y_history[-(n):], self.gy )

    def steps_since_shot(self):

        #gets the relevant time history

        relevant_time = self.time_steps[ self.time_steps > self.last_shot ]
        return min(len(relevant_time), params.max_velocity_hist )



    def get_ball_height():

        ##from sensor
        return 1



print ()
