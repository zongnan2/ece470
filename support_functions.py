import numpy as np
from scipy.linalg import expm


def skew_semetric(w):

    grid = np.zeros((3,3))
    try:
        grid[0] = [0, -1*w[2][0], w[1][0] ]
    except:
        grid[0] = [0, -1*w[2], w[1] ]
    try:
        grid[1] = [w[2][0], 0, -w[0][0]   ]
    except:
        grid[1] = [w[2], 0, -w[0]   ]
    try:
        grid[2] = [-1*w[1][0], w[0][0], 0 ]
    except:
        grid[2] = [-1*w[1], w[0], 0 ]

    return grid

def screw_bracket(screw):

    omega = screw[:3]
    nu = screw[3:6]

    skew_sem_om = skew_semetric(omega)

    brack_s = np.zeros((4,4))
    brack_s[ :3, :3] = skew_sem_om
    try:
        brack_s[ 0, 3] = nu[0][0]
    except:
        brack_s[ 0, 3] = nu[0]

    try:
        brack_s[ 1, 3] = nu[1][0]
    except:
        brack_s[ 1, 3] = nu[1]

    try:
        brack_s[ 2, 3] = nu[2][0]
    except:
        brack_s[ 2, 3] = nu[2]

    return brack_s

def mat_exp(mat):
    return expm(mat)

def mat_mult(a,b):
    return np.matmul(a,b)

def deg_to_rad(deg):
    return np.radians(deg)

def calculate_trans_matrix(screws, thetas, M):

    bracket_screws = []
    for i in screws:
        bracket_screws.append(i)

def get_screws_mats(omegas, qs_or_vs, rot_joints):

    screws = []

    for i in range(len(omegas)):
        screw = np.zeros((6,1))
        screw[:3] = omegas[i]

        if rot_joints[i]:
            #rotational joint
            #v = -w x q
            flat_neg_omega = [-omegas[i][0][0], -omegas[i][1][0], -omegas[i][2][0]]
            flat_q = [qs_or_vs[i][0][0],qs_or_vs[i][1][0],qs_or_vs[i][2][0]]
            v = np.cross( flat_neg_omega, flat_q )

            v_nested = np.array([ [v[0]], [v[1]], [v[2]] ])
            screw[3:6] = v_nested

        else:
            #prismatic joint
            screw[3:6] = qs_or_vs[i]
            pass

        screws.append(screw)
    return screws

def sep_screws_to_one_mat(sep_screws):

    screw = np.zeros((6,len(sep_screws)))

    for i in range(len(sep_screws)):
        curr_screw = sep_screws[i]
        for j in range(6):

            screw[j,i] = curr_screw[j][0]

    return screw
