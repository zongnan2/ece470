import params
import smart_velocity_finder as svf
import numpy as np
import time
import pygame_help as ph
import math
import sys

class Ball:

    def __init__(self, coords, tilt):

        self.coords = coords

        self.v = 6
        self.tilt = tilt

        self.vp1 = self.v * math.cos(self.tilt)
        self.vp2 = self.v * math.sin(self.tilt)

        self.radius = 5
        self.color = params.ball_color

        self.v1s = []
        self.v2s = []
        self.x1s = []
        self.x2s = []

    def draw(self, screen):
        ph.draw_circle(screen, self.color, ph.world_coord_to_pixel_coord(self.coords), self.radius)

    def update(self):
        self.vp2 = self.vp2 + params.g * params.dt_sec
        self.coords[1] = self.coords[1] + self.vp2*params.dt_sec + .5*params.g*params.dt_sec**2
        self.coords[0] = self.coords[0] + self.vp1*params.dt_sec

        self.v1s = svf.add_to_front(self.vp1, self.v1s)
        self.v2s = svf.add_to_front(self.vp2, self.v2s)
        self.x1s = svf.add_to_front(self.coords[0], self.x1s)
        self.x2s = svf.add_to_front(self.coords[1], self.x2s)


        if len(self.x1s) > int(params.max_velocity_hist/4):
            self.find_time_pos_of_peak()
            return True

        return False

    def find_time_pos_of_peak(self):

        dv = self.v2s[-1] - self.v2s[0]
        dt = params.dt_sec * (len(self.v2s) - 1)

        v_per_s = dv / dt

        time_from_now = self.v2s[0] / v_per_s

        x_pos = self.x1s[0] + (self.v1s[0] * time_from_now)
        y_pos = self.x2s[0] + (self.v2s[0] * time_from_now + .5*params.g*time_from_now**2)

        self.x_peak = x_pos
        self.y_peak = y_pos
        self.t_peak = time_from_now + time.time()



print ()
