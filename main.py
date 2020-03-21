import time
import ball
import arm
import params
import support_functions as sf

'''
to show kinematics -> kinematics_test.py
use keys 1,2,3,4 to rotate joints
'''

screw = sf.get_screws_mats(params.omegas, params.qs_or_vs, params.rot_joints)
screw = sf.sep_screws_to_one_mat(screw)


robot = arm.Robot(params.Ms, screw)
time.sleep(1)
robot.change_theta( sf.deg_to_rad(90), 1 )
time.sleep(1)




print ()
