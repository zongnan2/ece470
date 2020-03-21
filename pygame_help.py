import pygame
import math
import numpy as np
import params

def get_screen(length, width):
    '''Returns the screen with length and width'''
    return pygame.display.set_mode((length, width))

def flip_screen():
    '''Updates the screen'''
    pygame.display.flip()

def fill_screen(screen, color):
    screen.fill(color)

def draw_circle(screen, color, coords, radius):
    x = int(coords[0])
    y = int(coords[1])
    pygame.draw.circle(screen, color, [x,y], int(radius))

def draw_line(screen, color, start, end, width = 5):
    pygame.draw.line(screen, color, start, end, width)

#def draw_rect(screen, color, coords):
def deg_to_rad(deg):
    return math.pi * deg / 180

def rad_to_deg(rad):
    return rad * 180 / math.pi


def angle_from_1_to_2(x1,y1,x2,y2):

    dy = y2 - y1
    dx = x2 - x1
    theta = math.atan2(dy,dx)
    return theta

def polar_to_cart(r, radians):

    x = r * math.cos(radians)
    y = r * math.sin(radians)
    return x, y

def world_coord_to_pixel_coord(coords):

    T = np.array([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 1]
    ])

    coords_arr = np.array([ coords[0], coords[1], 0 ,0]) * params.pix_to_met
    new_coords = np.matmul(T, coords_arr)
    coords = [ new_coords[0] + params.length/2, new_coords[1] + params.width/2]

    return coords

def draw_robot(screen, joints_coords):

    fill_screen(screen, params.background_color )

    for i in range(1, len(joints_coords)):

        start = world_coord_to_pixel_coord( joints_coords[i-1])
        end = world_coord_to_pixel_coord( joints_coords[i])

        draw_line(screen, params.colors[i-1], start, end)

    for i in range(len(joints_coords)):
        draw_circle(screen, params.joint_colors[i], world_coord_to_pixel_coord(joints_coords[i]), params.joint_rad)



    flip_screen()
