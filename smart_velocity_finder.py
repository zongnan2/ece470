import numpy as np
import matplotlib.pyplot as plt
import params

def test():

    time = np.linspace(0, 2, 100)
    y = 10*time -4.9*(time**2)

    plt.plot(y)
    plt.show()

def add_to_front(new, old, limit = params.max_velocity_hist):

    old.insert(0, new)
    if len(old) > limit:
        old = old[:limit]

    return old


def get_weights(n):

    ###Weights = [0.5, 0.25, 0.125, etc]

    ran = np.linspace(1, n, n)
    weights = 1 / (2**ran)
    weights[0] += (1 - sum(weights))

    return weights

def find_velocity(time, pos, accel):

    #finds velocity based on historical time and position data

    ##[oldest, next oldest, newest]
    vs = np.zeros( len(time) - 1 )
    weights = get_weights(len(time) - 1)

    ###Calculate the velocity using the historical values of the position and time
    for i in range(len(time) -1):

        dx = pos[-1] - pos[i]
        dt = time[-1] - time[i]

        v0 = (dx - 0.5*accel*dt**2)/dt
        vs[i] = v0 + accel*dt

    #return a weighted calculation of the current velocity which takes into account possible signal error
    return np.dot(weights, vs)


if __name__ == '__main__':

    time = np.linspace(0, 2, 100)
    y = 10*time *.5*params.gravity*(time**2)

    get_weights(10)

    print (find_velocity(time[:10], y[:10], params.gravity))
