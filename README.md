# ece470
project files

----
This system contains a ball launcher and a bat, two individual systems.

In ball.py, a Ball class is defined. This Ball class allows a ball to be shot from the vertical cannon. It will be connected to a distance sensor which will track the position of the ball.
In bat.py, a Bat class is defined. This bat class will have operations such a swing, and angle control of the bat.
smart_velocity_finder.py is a program which uses the historical positions of the ball to Calculate the current velocity of the ball, using physics kinematics equations.
params.py stores the constants of the system, such as height, length, weight, and others.
main.py contains the controls of the system, such as initilizing classes, calling the ball to be shot, and telling the bat when to swing
