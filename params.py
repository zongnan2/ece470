import time
import numpy as np
###All dimensions in meters

gravity = -9.81

max_velocity_hist = 10

#BALL
ball_base_x = 0
ball_base_y = 0
ball_base_z = 0
ball_radius = .02

#for simulation only
ball_v0 = 10

#BAT
bat_base_x = .1
bat_base_y = 0
bat_base_z = 0

bat_base_height = .1
bat_length = .2

###For Transformation Matrix

L1 = 1 #meter
omega1 = np.array([ [1],[0],[0] ])
q1 = np.array([ [0],[0],[0] ])
rot_joint1 = True

L2 = .8
omega2 = np.array([ [1],[0],[0] ])
q2 = np.array([ [0],[0],[L1]])
rot_joint2 = True

L3 = .2
omega3 = np.array([ [1],[0],[0] ])
q3 = np.array([ [0],[0],[L1+L2]])
rot_joint3 = True

L4 = .4
omega4 = np.array([ [0],[0],[1] ])
q4 = np.array([ [0],[0],[L1+L2+L3]])
rot_joint4 = True

omegas = [omega1, omega2, omega3, omega4]
qs_or_vs = [q1,q2,q3,q4]
rot_joints = [rot_joint1, rot_joint2, rot_joint3, rot_joint4]

M = np.array([
[0,1,0,0],
[0,0,1,0],
[1,0,0, (L1+L2+L3+L4) ],
[0,0,0,1]
])

############## Start Time
start_time = time.time()
