# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:02:15 2015

@author: Collette
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def ampli(epsilon):
    global V_cc
    return V_cc*np.arctan(10000*(epsilon-1e-9))/(np.pi/2)


def ode_oscillateur(x, V_cc, C, C_A, R):
    V = x[0]
    epsilon = x[1]
    sortie_ampli = ampli(epsilon)
    xp0 = (2*sortie_ampli-3*V-2*epsilon)/(R*C)
    xp1 = (sortie_ampli-2*V-2*epsilon)/(R*C_A)
    return np.array([xp0, xp1])


V_cc = 15
C = 1e-6
C_A = 1e-10
R = 10e3
t_start = 0.0
t_final = 0.05
delta_t = 1e-6
x0 = [0, 0]
sol = solve_ivp(lambda t, x: ode_oscillateur(x, V_cc, C, C_A, R), [
                0, t_final], x0, rtol=1e-10, atol=1e-10)
t = sol.t.T
x = sol.y.T
plt.figure()
plt.semilogy(t[0:-1], np.diff(t), 'o-', lw=0.5, ms=1)
plt.grid('on')
plt.title('Pas de temps')
plt.xlabel('temps (en s)')
plt.ylabel('h_n')

V = x[:, 0]
y = ampli(x[:, 1])
plt.figure()
pt = plt.plot(t, V, t, y, lw=0.5)
plt.grid('on')
plt.title('Tensions (en V)')
plt.xlabel('temps (en s)')
plt.legend(pt, ['V', 'y'])
plt.show()
