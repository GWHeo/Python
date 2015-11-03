__author__ = 'Gun-woo'
import numpy as np
import pylab

linear_v = np.array([0])
for i in range(0, 101):
    linear_v = np.append(linear_v, np.arange(0,i))

v1 = np.random.normal(20, 2, 1000)
v2 = np.random.normal(70, 5, 1000)
v3 = np.hstack((v1,v2,linear_v))

pylab.hist(v3, bins=100)
pylab.show()