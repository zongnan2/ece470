import time
import ball
import arm
import params
import support_functions as sf
import launcher
import pygame_help as ph
import pygame
import numpy as np

'''
to show kinematics -> kinematics_test.py
use keys 1,2,3,4 to rotate joints
'''

def check_old_balls(balls):

    for i in range(len(balls)-1, -1, -1):
        ball = balls[i]
        if ball.coords[1] < -2:
            del balls[i]

    return balls

def check_hit(balls, robot):

    for i in range(len(balls)-1, -1, -1):
        ball = balls[i]

        robot.get_trans_matrices
        robot_x1 = robot.Ts[-1][1][-1]
        robot_x2 = robot.Ts[-1][2][-1]
        ball_x1 = ball.coords[0]
        ball_x2 = ball.coords[1]

        dist = ((robot_x1-ball_x1)**2 + (robot_x2-ball_x2)**2)**.5

        if dist < 0.1:
            del balls[i]

    return balls




plane1 = 'Y'
plane2 = 'Z'

screen = ph.get_screen(params.length, params.width)
clock = pygame.time.Clock()

screw = sf.get_screws_mats(params.omegas, params.qs_or_vs, params.rot_joints)
screw = sf.sep_screws_to_one_mat(screw)

robot = arm.Robot(params.Ms, screw, screen)
launcher = launcher.Launcher(screen)
balls = []

cooldown = 1.5
last_shot = time.time()
time_steps_needed = 5
times = []

while True:

    ph.fill_screen(screen, params.background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            pygame.quit()

    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()


        if keys[pygame.K_UP]:
            launcher.up()

        if keys[pygame.K_DOWN]:
            launcher.down()

        if keys[pygame.K_LEFT]:
            launcher.left()

        if keys[pygame.K_RIGHT]:
            launcher.right()

        if keys[pygame.K_a]:
            launcher.counter_clock()

        if keys[pygame.K_s]:
            launcher.clockwise()

        if keys[pygame.K_SPACE]:

            #if (time.time() - last_shot) > cooldown:
            if len(balls) == 0:
                last_shot = time.time()
                new_ball = launcher.shoot()
                balls.append(new_ball)
                success = False
                ball_hist_coords = []
                times = []

        if keys[pygame.K_z]:
            break

    ph.fill_screen(screen, params.background_color)


    for ball_num in range(len(balls)):
        ball = balls[0]

        ready = ball.update()
        ball.draw(screen)

        if ready and not success:
            #ph.draw_circle(screen, (255,255,255), ph.world_coord_to_pixel_coord([ball.x_peak, ball.y_peak]), ball.radius)
            peak1 = ball.x_peak
            peak2 = ball.y_peak

            T_temp = np.array([
            [1,0,0,0],
            [0,1,0,peak1],
            [0,0,1,peak2],
            [0,0,0,1]
            ])

            thetas, success = robot.inverse_kinematics(T_temp, robot.thetas)

            if success:
                success_iter = 0
                curr_thetas = np.array(robot.thetas)
                thetas = np.array(thetas)
                d_theta = (thetas - curr_thetas) / time_steps_needed


        if ready and success:

            for i in range(len(thetas)):
                robot.change_theta( robot.thetas[i] + d_theta[i] , i)
            success_iter += 1

            if success_iter == time_steps_needed:
                success = False


    robot.get_trans_matrices()
    robot.get_world_coords()
    robot.draw_links(screen)
    launcher.draw(screen)



    balls = check_old_balls(balls)
    balls = check_hit(balls, robot)

    ph.flip_screen()

    clock.tick(params.dt)



print ()
