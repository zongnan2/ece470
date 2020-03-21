import time
import ball
import arm
import params
import support_functions as sf
import pygame
import pygame_help as ph

screw = sf.get_screws_mats(params.omegas, params.qs_or_vs, params.rot_joints)
screw = sf.sep_screws_to_one_mat(screw)

robot = arm.Robot(params.Ms, screw)

pygame.key.set_repeat(30, 30)
clock = pygame.time.Clock()

d_theta = 2

robot.get_trans_matrices()
robot.get_world_coords()
robot.draw_links()
ph.flip_screen()
robot.print_info()
print ('Transformation Matrices')
for i in range(robot.n):
    print (robot.Ts[i])

print ('Joint Coords')
for i in range(robot.n):
    print (robot.coords[i])

print ()
print ('Press 1,2,3,4 to rotate the respective joint')
print ('Hold spacebar for negative rotation')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            pygame.quit()

    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        move = [False, False, False, False]
        one = False
        neg = 1

        if keys[pygame.K_1]:
            move[0] = True
            one = True

        if keys[pygame.K_2]:
            move[1] = True
            one = True

        if keys[pygame.K_3]:
            move[2] = True
            one = True

        if keys[pygame.K_4]:
            move[3] = True
            one = True

        if keys[pygame.K_SPACE]:
            neg = -1

        if keys[pygame.K_z]:
            break


    if one:
        for i in range(len(move)):
            if move[i]:
                print ('moving joint ' + str(i))
                robot.delta_theta(d_theta*neg, i)

        robot.get_trans_matrices()
        robot.get_world_coords()
        robot.draw_links()
        ph.flip_screen()


    clock.tick(params.dt)
