__author__ = 'Gun-woo'
import numpy as np
import pylab
class histogram:
    def h1(self):
        self.v1 = np.random.normal(20, 2, 1000)
        return self.v1
    def h2(self):
        self.v2 = np.random.normal(70, 5, 1000)
        return self.v2
    def lin(self):
        self.linear_v = np.array([0])
        for i in range(0, 101):
            self.linear_v = np.append(self.linear_v, np.arange(0,i))
        return self.linear_v
    def merge(self, *args):
        self.v3 = np.hstack((args))
        return self.v3

    def draw(self, histo):
        pylab.hist(histo, bins=100)
        pylab.show()
"""
a = histogram()
v1 = a.h1()
v2 = a.h2()
v3 = a.lin()
m1 = a.merge(v1,v2,v3)
a.draw(m1)
"""