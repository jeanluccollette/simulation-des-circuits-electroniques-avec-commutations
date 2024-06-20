# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:02:15 2015

@author: Collette
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def ode_convres(t, x, c, l1, L, R, r1, fh):
    ve = x[0]
    i_1 = x[1]
    i_s = x[2]
    E = 200*np.sign(np.sin(2*np.pi*fh*t))
    xp0 = (1/c)*(i_1-i_s*np.sign(ve))
    xp1 = (1/l1)*(E-ve-r1*i_1)
    xp2 = (1/L)*(abs(ve)-R*i_s)
    return np.array([xp0, xp1, xp2])


c = 1e-8
l1 = 1e-3
L = 5e-2
R = 500
r1 = 0.02
fh = 40000
t_start = 0.0
t_final = 1e-3
delta_t = 1e-7
x0 = [0, 0, 0]

sol = solve_ivp(lambda t, x: ode_convres(t, x, c, l1, L, R, r1, fh), [
                0, t_final], x0, rtol=1e-10, atol=1e-10)
t = sol.t.T
x = sol.y.T
plt.figure()
plt.semilogy(t[0:-1], np.diff(t), 'o-', lw=0.5, ms=1)
plt.grid('on')
plt.title('Pas de temps')
plt.xlabel('temps (en s)')
plt.ylabel('h_n')

ve = x[:, 0]
i_1 = x[:, 1]
i_s = x[:, 2]
tensions = np.zeros((len(t), 2))
courants = np.zeros((len(t), 4))
tensions[:, 0] = ve
tensions[:, 1] = R*i_s
courants[:, 0] = np.sign(np.sin(2*np.pi*fh*t))
courants[:, 1] = i_1
courants[:, 2] = i_s
courants[:, 3] = i_1-i_s*np.sign(ve)
plt.figure()
pt = plt.plot(t, tensions, lw=0.5)
plt.grid('on')
plt.title('Tensions (en V)')
plt.xlabel('temps (en s)')
plt.legend(pt, ['v_e', 'R*i_s'])
plt.figure()
pt = plt.plot(t, courants, lw=0.5)
plt.grid('on')
plt.title('Courants (en A)')
plt.xlabel('temps (en s)')
plt.legend(pt, ['signal de commande', 'i_1', 'i_s', 'i_c'])
plt.show()
