import math


#bipadal_irc_IK


def inverse_kinematics(x, y, z):
    theta_1 = 0
    theta_2 = 0
    theta_3 = 0


    phi_1 = 0
    phi_2 = 0
    phi_3 = 0

    pos_1 = 0
    pos_2 = 0
    pos_3 = 0

    pos_4 = 0
    pos_5 = 0

   

    r_1 = z
    r_2 = x
    r_3 = math.sqrt(r_1**2 + r_2**2)

    a_1 = 130  # [mm] 축 길이 일치 구조

    todegree = 180 / math.pi

    if x >= 0:
        phi_2 = math.atan2(r_1, abs(r_2))
        phi_1 = math.acos(r_3**2 / (2 * a_1 * r_3))
        theta_2 = abs(phi_2) - phi_1
        pos_2 = theta_2 * todegree - 90
    else:
        phi_2 = math.atan2(r_1, abs(r_2))
        phi_1 = math.acos(r_3**2 / (2 * a_1 * r_3))
        theta_2 = math.pi - (abs(phi_2) + abs(phi_1))
        pos_2 = theta_2 * todegree - 90

    phi_3 = math.acos((r_3**2 - 2 * a_1**2) / (-2 * a_1**2))
    theta_3 = math.pi - phi_3
    pos_3 = theta_3 * todegree

   

    if y >=0:
        theta_1 = math.atan2(-1*r_1,y)
        pos_1= theta_1 * todegree
    else:
        theta_1 = abs(math.atan2(r_1,y))
        pos_1 = theta_1 * todegree

    pos_1 -= 90
    pos_4 = pos_2 + pos_3
    pos_5 = pos_1


    return pos_1, pos_2, pos_3, pos_4, pos_5
angle = []
angle=inverse_kinematics(0,100,-200)
print(angle)
