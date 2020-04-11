import time
import numpy as np
###All dimensions in meters

g = -9.81

max_velocity_hist = 20

#BALL
ball_radius = 4
ball_v0 = 10

#for simulation only

###For Transformation Matrix

L1 = 1 #meter
L2 = .8
L3 = .2
L4 = .4

omega1 = np.array([ [1],[0],[0] ])
q1 = np.array([ [0],[0],[0] ])
rot_joint1 = True

omega2 = np.array([ [1],[0],[0] ])
q2 = np.array([ [0],[0],[L1]])
rot_joint2 = True

omega3 = np.array([ [1],[0],[0] ])
q3 = np.array([ [0],[0],[L1+L2]])
rot_joint3 = True

omega4 = np.array([ [0],[1],[0] ])
q4 = np.array([ [0],[0],[L1+L2+L3]])
rot_joint4 = True

omegas = [omega1, omega2, omega3, omega4]
qs_or_vs = [q1,q2,q3,q4]
rot_joints = [rot_joint1, rot_joint2, rot_joint3, rot_joint4]

Ms = [
np.array([
[1,0,0,0],
[0,1,0,0],
[0,0,1,L1],
[0,0,0,1]
]),

np.array([
[1,0,0,0],
[0,1,0,0],
[0,0,1,L1+L2],
[0,0,0,1]
]),

np.array([
[1,0,0,0],
[0,1,0,0],
[0,0,1,L1+L2+L3],
[0,0,0,1]
]),

np.array([
[1,0,0,0],
[0,0,1,0],
[0,-1,0,L1+L2+L3+L4],
[0,0,0,1]
])
]

M = Ms[-1]

#Pygame
length = 700
width = 500
pix_to_met = min(length, width) / 2 / (L1+L2+L3+L4)
background_color = (0,0,0)
joint_color = (255,255,255)
ball_color = (255,255,0)
joint_rad = 5
dt = 60
dt_sec = 1 / dt

colors = [ (120,120,120), (120,120,120), (120,120,120), (0,0,255) ]
joint_colors = [ (255,0,0),(255,0,0),(255,0,0),(255,0,0), (255,0,0)]







############## Start Time
start_time = time.time()
