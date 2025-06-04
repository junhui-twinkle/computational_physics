import numpy as np
import matplotlib.pylab as pl
from scipy.special import roots_legendre

Lhalf = 1.0
Lfull = 2 * Lhalf
c = 1.0
dx = 0.05
dy = 0.05
N = 20
x_axis = np.arange(-3, 3, 0.05)
y_axis = np.arange(-3, 3, 0.05)

field_x = []
field_y = []
field = []
potential = []

xk, wk = roots_legendre(N)
xp = xk * Lhalf
wp = wk * Lhalf


def lamda(x):
    y = np.exp(-(x ** 2))
    return y


def f(x, x0, y0):
    y = lamda(x)
    r = np.sqrt((x0 - x) ** 2 + y0 ** 2)
    return c * y / r


def u(x0, y0, n, x_list, w_list):
    U = 0.0
    for i in range(0, n, 1):
        U += f(x_list[i], x0, y0) * w_list[i]
    return U


for x0 in x_axis:
    for y0 in y_axis:
        potential1 = u(x0, y0, n=N, x_list=xp, w_list=wp)
        Ex = - (u(x0 + dx, y0, n=N, x_list=xp, w_list=wp) - u(x0 - dx, y0, n=N, x_list=xp, w_list=wp)) / (2 * dx)
        Ey = - (u(x0, y0 + dy, n=N, x_list=xp, w_list=wp) - u(x0, y0 - dy, n=N, x_list=xp, w_list=wp)) / (2 * dy)
        E = np.sqrt((Ex ** 2) + (Ey ** 2))
        potential.append(potential1)
        field_x.append(Ex)
        field_y.append(Ey)
        field.append(E)

apotential = np.array(potential)
afield_x = np.array(field_x)
afield_y = np.array(field_y)
afield = np.array(field)
apotential_2D = apotential.reshape(len(x_axis), len(y_axis))
afield_x_2D = afield_x.reshape(len(x_axis), len(y_axis))
afield_y_2D = afield_y.reshape(len(x_axis), len(y_axis))
afield_2D = afield.reshape(len(x_axis), len(y_axis))
apotential_2D_T = apotential_2D.T
afield_x_2D_T = afield_x_2D.T
afield_y_2D_T = afield_y_2D.T
afield_2D_T = afield_2D.T

fig = pl.figure(figsize=(15, 7))
ax1 = fig.add_subplot(1, 2, 1)
extent = [-3, 3, -3, 3]
levels = np.arange(0, 5, 0.1)
cs = ax1.contourf(apotential_2D_T, extent=extent, levels=levels, cmap=pl.cm.rainbow, origin='lower')
cbar1 = fig.colorbar(cs, ax=ax1)

ax2 = fig.add_subplot(1, 2, 2)
color = np.log(afield_2D_T)
stream = ax2.streamplot(x_axis, y_axis, afield_x_2D_T, afield_y_2D_T, color=color, cmap=pl.cm.rainbow,
                        density=2, arrowstyle='->', linewidth=1, arrowsize=1.5)
cbar2 = fig.colorbar(stream.lines, ax=ax2)

ax1.set_xlabel('X', size=20)
ax1.set_ylabel('Y', size=20)
ax2.set_xlabel('X', size=20)
ax2.set_ylabel('Y', size=20)
ax1.set_xlim(-3.0, 3.0)
ax1.set_ylim(-3.0, 3.0)
ax2.set_xlim(-3.0, 3.0)
ax2.set_ylim(-3.0, 3.0)
ax1.set_title('Potential', size=20)
ax2.set_title('Electric field', size=20)
pl.show()
