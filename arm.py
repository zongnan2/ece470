import numpy as np
import pygame_help as ph
import params
import get_transformation_matrix as gtm
import support_functions as sf

from modern_robotics import *

class Robot:

    def __init__(self, Ms, screw, show_screen = True):

        self.Ms = Ms.copy()
        self.M = Ms[-1].copy()
        self.screw = screw
        self.n = len(screw[0])
        self.thetas = np.zeros(self.n)

        self.get_trans_matrices()
        self.get_world_coords()

        self.show_screen = show_screen

        for i in self.Ts:
            print (i)

    def print_info(self):

        self.get_lengths_from_coords()

        for i in range(self.n):
            print ('L' + str(i+1) + '. ' + str(self.lengths[i]) )

        for i in range(self.n):
            print ('THETA' + str(i+1) + '. ' + str(self.thetas[i]) )



    def get_trans_matrices(self):

        self.Ts = np.zeros((self.n, 4, 4))

        for i in range(self.n):

            j = i+1

            theta_slice = self.thetas[:j]
            screw_slice = self.screw[:, :j]

            new_T = gtm.get_t(M = self.Ms[i], thetas = theta_slice, screw = screw_slice )

            self.Ts[i] = new_T

    def get_world_coords(self):

        self.coords = np.zeros((self.n, 3))

        for i in range(self.n):

            self.coords[i] = gtm.tool_vector_to_body_vector(self.Ts[i], [0,0,0])

    def get_lengths_from_coords(self):

        self.lengths = np.zeros(self.n)

        for i in range(self.n):

            if i == 0:
                start = [0,0]
            else:
                start = self.coords[i-1]

            end = self.coords[i]

            dist = (( start[0] - end[0] )**2 + (start[1] - end[1])**2) ** .5
            self.lengths[i] = dist

    def change_theta(self, new_theta, theta_ind):
        self.thetas[theta_ind] = new_theta
        self.get_trans_matrices()
        self.get_world_coords()

    def delta_theta(self, d_theta, theta_ind, to_rad = True):

        if to_rad:
            d_theta = sf.deg_to_rad(d_theta)

        self.thetas[theta_ind] = self.thetas[theta_ind] + d_theta

    def draw_links(self, screen, plane1 = 'Y', plane2 = 'Z'):

        planes = [ 'X','Y','Z']
        plane1_ind = planes.index(plane1)
        plane2_ind = planes.index(plane2)

        joints = [ [0,0] ]

        for i in range(self.n ):

            end_point = [ self.coords[i][plane1_ind], self.coords[i][plane2_ind] ]
            joints.append(end_point)


        ph.draw_robot(screen, joints)


    def inverse_kinematics(self, T, thetalist0 ):

        Slist = self.screw
        M = self.M
        eomg = 0.01
        ev = 0.01

        thetalist = np.array(thetalist0).copy()

        i = 0
        maxiterations = 20

        Tsb = FKinSpace(M,Slist, thetalist)

        Vs = np.dot(Adjoint(Tsb), \
                    se3ToVec(MatrixLog6(np.dot(TransInv(Tsb), T))))
        err = np.linalg.norm([Vs[0], Vs[1], Vs[2]]) > eomg \
              or np.linalg.norm([Vs[3], Vs[4], Vs[5]]) > ev
        while err and i < maxiterations:

            thetalist = thetalist \
                        + np.dot(np.linalg.pinv(JacobianSpace(Slist, \
                                                              thetalist)), Vs)
            i = i + 1
            Tsb = FKinSpace(M, Slist, thetalist)

            Vs = np.dot(Adjoint(Tsb), \
                        se3ToVec(MatrixLog6(np.dot(TransInv(Tsb), T))))
            eomg_c = np.linalg.norm([Vs[0], Vs[1], Vs[2]])
            ev_c = np.linalg.norm([Vs[3], Vs[4], Vs[5]])
            err = eomg_c > eomg or ev_c > ev


        return (thetalist, not err)
