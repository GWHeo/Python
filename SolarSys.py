from visual import *
import numpy as np
### Radius scale of planets is enlarged x100 than real scale, the sun is enlarged x10

## Define constants
## (detailed information quoted from Wikipedia)
G = 6.7e-11

def DeriveApsis(eccentricity, aphelion, perihelion):
    a = (aphelion + perihelion)/2
    b = sqrt(a**2 - a**2*eccentricity**2)
    apsis_list = [a, b]
    return apsis_list


class property:
    def __init__(self, aphelion, perihelion, eccentricity, period, radius, mass, col):
        self.a = aphelion
        self.p = perihelion
        self.e = eccentricity
        self.t = period
        self.r = radius
        self.m = mass
        self.c = col
    def apsis(self):
        return DeriveApsis(self.e, self.a, self.p)
    def period(self):
        return 2*pi/self.t  #sec/year
    def ball(self):
        self.b = sphere(pos=(self.a,0,0), radius=self.r, mass=self.m, color=self.c, make_trail=True)
        return self.b


Sun = sphere(pos=(0,0,0), radius=6.955e6, mass=1.9891e30, color=color.yellow, material=materials.emissive)
lamp = local_light(pos=(0,0,0), color=color.yellow)
scene.ambient = 0

Mercury = property(6.9817e7, 4.6001e7, 0.205, 0.240, (4.8794e5)/2, 3.302e23, (0,1,0))
Jupiter = property(8.1652e8, 7.4057e8, 0.0488, 11.86, 6.99e6, 1.8986e27, (1,0,0))

"""
class solar_system:
    def Sun(self):
        self.ball = sphere(pos=(0,0,0), radius=6.955e6, mass=1.9891e30, color=color.yellow, material=materials.emissive)
        self.lamp = local_light(pos=(0,0,0), color=color.yellow)
        scene.ambient = 0
        return self.ball
    def Mercury(self):
        self.Mercury_aphelion = 4.6001e7
        self.Mercury_perihelion = 6.9817e7
        self.ball = sphere(pos=(self.Mercury_aphelion,0,0), radius=4.8794e5/2, mass=3.302e23, color=color.gray)
        return self.ball
    def Mercury_apsis(self):
        return DeriveApsis(0.205, self.Jupiter_aphelion, self.Jupiter_perihelion)
    def Mercury_period(self):
        return

    def Jupiter(self):
        self.Jupiter_aphelion = 8.1652e8
        self.Jupiter_perihelion = 7.4057e8
        self.ball = sphere(pos=(self.Jupiter_aphelion,0,0), radius=6.99e6, mass=1.8986e27, color=color.red, make_trail=True)
        return self.ball
    def Jupiter_apsis(self):
        return DeriveApsis(0.0488, self.Jupiter_aphelion, self.Jupiter_perihelion)


planets = solar_system()
S = planets.Sun()
M = planets.Mercury()
J = planets.Jupiter()
dt = 0.01
period = 2*pi/11.86  #sec/year
theta = 0
"""
dt = 0.01
Mercury_theta = 0
Jupiter_theta = 0
print Jupiter.period()
while True:
    rate(100)
    """
    Mercury_theta += Mercury.period()*dt
    Mercury.ball().pos += (-Mercury.apsis()[0]*Mercury.period()*sin(Mercury_theta)*dt,
                         Mercury.apsis()[1]*Mercury.period()*cos(Mercury_theta)*dt,
                         0)
    """
    Jupiter_theta += Jupiter.period()*dt
    Jupiter.ball().pos += (-Jupiter.apsis()[0]*Jupiter.period()*sin(Jupiter_theta)*dt,
                           Jupiter.apsis()[1]*Jupiter.period()*cos(Jupiter_theta)*dt,
                           0)
