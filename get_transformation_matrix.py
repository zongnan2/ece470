import numpy as np
from scipy.linalg import expm
import support_functions as sf
import params

thetas = np.radians([0,90,0,0])
omegas = params.omegas
qs_or_vs = params.qs_or_vs
rot_joints = params.rot_joints

screws = sf.get_screws_mats(omegas, qs_or_vs, rot_joints)

for i in screws:
    print (i)
