# Program to plot ball's velocity wrt time

from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
g  = 9.81
t  = linspace(0, 1, 1000)

y  = v0*t - 0.5*g*t**2

plt.plot(t,y)
plt.show()




