import time
import ball
import bat
import params

#initilize class
Ball = ball.Ball()

#shoot the ball vertically upward
Ball.shoot()

while Ball.y >= 0:

    #update the balls height and velocity

    Ball.move()


print (Ball.y_history)

import matplotlib.pyplot as plt

plt.scatter(Ball.time_steps, Ball.y_history)
plt.show()
