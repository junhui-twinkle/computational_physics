import numpy as np
import matplotlib.pylab as pl

q1 = 10.0
q2 = 10.0
a1 = 1.0
a2 = 3.0
theta = np.pi / 3
dx = 0.05
dy = 0.05
xstep = 0.05
ystep = 0.05
x_min = -5.0
x_max = 5.0
y_min = -5.0
y_max = 5.0


def potential(x, y):
    y = - q1 / (np.sqrt((x + a1) ** 2 + y ** 2)) + q1 / (np.sqrt((x - a1) ** 2 + y ** 2)) \
        - q2 / (np.sqrt((x + a2 * np.cos(theta)) ** 2 + (y + a2 * np.sin(theta)) ** 2)) \
        + q2 / (np.sqrt((x - a2 * np.cos(theta)) ** 2 + (y - a2 * np.sin(theta)) ** 2))
    return y


# 要计算的点
x_axis = np.arange(x_min, x_max, xstep)
y_axis = np.arange(y_min, y_max, ystep)
field_x = []
field_y = []
field = []
Potential = []

for x0 in x_axis:
    for y0 in y_axis:
        Ex = - 1.0 * (potential(x0 + dx, y0) - potential(x0 - dx, y0)) / (2 * dx)
        Ey = - 1.0 * (potential(x0, y0 + dy) - potential(x0, y0 - dy)) / (2 * dy)
        E = np.sqrt(Ex ** 2 + Ey ** 2)
        Potential.append(potential(x0, y0))
        field_x.append(Ex)
        field_y.append(Ey)
        field.append(E)

aPotential = np.array(Potential)
afield_x = np.array(field_x)
afield_y = np.array(field_y)
afield = np.array(field)

aPotential.shape = (len(x_axis), len(y_axis))
afield_x.shape = (len(x_axis), len(y_axis))
afield_y.shape = (len(x_axis), len(y_axis))
afield.shape = (len(x_axis), len(y_axis))

aPotential_T = aPotential.T
afield_x_T = afield_x.T
afield_y_T = afield_y.T
afield_T = afield.T

fig = pl.figure(figsize=(15, 7))
ax1 = fig.add_subplot(1, 2, 1)
extent = [-5.0, 5.0, -5.0, 5.0]
levels = np.arange(-100, 100, 1)
cs = ax1.contour(aPotential_T, levels=levels, origin='lower', extent=extent, cmap=pl.cm.rainbow)

color = np.log(afield_T)
ax2 = fig.add_subplot(1, 2, 2)
ax2.streamplot(x_axis, y_axis, afield_x_T, afield_y_T, color=color, cmap=pl.cm.rainbow,
               linewidth=1.0, density=2, arrowstyle='->', arrowsize=1.5)

ax1.set_xlabel('X', size=20)
ax1.set_ylabel('Y', size=20)
ax2.set_xlabel('X', size=20)
ax2.set_ylabel('Y', size=20)
ax1.set_xlim(-5.0, 5.0)
ax1.set_ylim(-5.0, 5.0)
ax2.set_xlim(-5.0, 5.0)
ax2.set_ylim(-5.0, 5.0)
ax1.set_title('Potential', size=20)
ax2.set_title('Electric field', size=20)
pl.show()
