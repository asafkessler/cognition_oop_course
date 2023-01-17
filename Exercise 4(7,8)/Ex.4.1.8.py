
def vol_dif(r):
    """
    you calculate the volume of the ball as if each side equals (2/sqrt(3))*r(ball)
    :param r:
    :return: 
    """
    from math import pi
    from math import sqrt
    vol_ball = (4 * pi * pow(r, 3)) / 3
    vol_box = pow((2*r) / sqrt(3), 3)

    return vol_ball - vol_box

if __name__ == "__main__":
    r = 3
    print(vol_dif(r))
