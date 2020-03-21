import numpy as np
from scipy.linalg import expm
import support_functions as sf
import params


def get_t(M = [], thetas = [], omegas = [], qs_or_vs = [], rot_joints = [], screw = []):

    if thetas == []:
        thetas = np.radians([0,90,0,90])

    if omegas == []:
        omegas = params.omegas

    if qs_or_vs == []:
        qs_or_vs = params.qs_or_vs

    if rot_joints == []:
        rot_joints = params.rot_joints

    if M == []:
        M = params.M

    if screw == []:
        screws = sf.get_screws_mats(omegas, qs_or_vs, rot_joints)
        screws = sf.sep_screws_to_one_mat(screws)
    else:
        screws = screw

    screw_bracks = []
    for i in range(len(thetas)):
        screw_bracks.append( sf.screw_bracket(screw[:, i]) )

    if len(thetas) > 0:

        mat = sf.mat_exp(screw_bracks[0] * thetas[0])

        for i in range(1, len(thetas)):
            two = screw_bracks[i] * thetas[i]
            mat = sf.mat_mult( mat, sf.mat_exp(two) )


        T = sf.mat_mult(mat, M)
        return T

    else:
        return M


def tool_vector_to_body_vector(T, tool_point):

    tool_point = np.append(tool_point, [1])
    a = np.matmul(T, tool_point)

    a = a[:3]
    return a


if __name__ == '__main__':
    T = get_t()
    print (T)

    print (tool_vector_to_body_vector(T, [ 0,0,0] ))
