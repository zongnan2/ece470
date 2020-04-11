import ball
import math
import pygame_help as ph

class Launcher:

    def __init__(self, screen, plane1 = 'Y', plane2 = 'Z'):

        self.x = 0
        self.y = 0
        self.z = 0

        self.tilt = 0
        self.d_tilt = .02

        self.v = 0.01

        self.p1 = plane1
        self.p2 = plane2
        self.planes = [plane1, plane2]

        self.coords = []
        for plane in self.planes:
            if plane == 'X':
                self.coords.append(self.x)
            if plane == 'Y':
                self.coords.append(self.y)
            if plane == 'Z':
                self.coords.append(self.z)

        self.length = 0.2
        self.color = (255, 120, 120)

        self.calc_end()

    def counter_clock(self):
        self.d_angle( -1*self.d_tilt)

    def clockwise(self):
        self.d_angle(self.d_tilt)

    def up(self):
        self.move(0, self.v)

    def down(self):
        self.move(0, -self.v)

    def left(self):
        self.move(-self.v ,0)

    def right(self):
        self.move(self.v ,0)

    def move(self, dp1, dp2):

        self.coords[0] += dp1
        self.coords[1] += dp2
        self.calc_end()

    def d_angle(self, dt):

        self.tilt += dt
        self.calc_end()

    def draw(self, screen):

        ph.draw_robot(screen, [self.coords, self.end_coords])

    def calc_end(self):

        self.end_coords = [ self.coords[0] + self.length * math.cos(self.tilt), self.coords[1] + self.length * math.sin(self.tilt) ]

    def shoot(self):

        new_ball = ball.Ball( self.coords.copy() , self.tilt )
        return new_ball
