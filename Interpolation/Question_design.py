import numpy as np
import matplotlib.pylab as pl
from scipy.special import roots_legendre
import matplotlib.animation as animation

Lhalf = 1.0
c = 1.0
dx = 0.1
dy = 0.1
N = 20
x_axis = np.arange(-3, 3, 0.1)
y_axis = np.arange(-3, 3, 0.1)
w0 = 1
h = 0.5
dt = 1
frames = 10

xk, wk = roots_legendre(N)
xp1 = xk * Lhalf
wp1 = wk * Lhalf
xp2 = xk * Lhalf + Lhalf
wp2 = wk * Lhalf
fig = pl.figure(figsize=(15, 7))
ax1 = fig.add_subplot(1, 2, 1)
extent = [-3, 3, -3, 3]
levels = np.arange(-4, 4, 0.1)
ax2 = fig.add_subplot(1, 2, 2)

def lamda1(x, w, t):
    y = np.exp(-(x ** 2)) * np.cos(w * t)
    return y


def lamda2(x, w, t):
    y = -1.5 * np.exp(-(x ** 2)) * np.cos(w * t)
    return y


def f1(x, x0, y0, w, t):
    y = lamda1(x, w, t)
    r = np.sqrt((x0 - x) ** 2 + (y0 - h) ** 2)
    return c * y / r


def f2(x, x0, y0, w, t):
    y = lamda2(x, w, t)
    r = np.sqrt((x0 - x) ** 2 + (y0 + h) ** 2)
    return c * y / r


def u1(x0, y0, n, x_list, w_list, w, t):
    U = 0.0
    for i in range(0, n, 1):
        U += f1(x_list[i], x0, y0, w, t) * w_list[i]
    return U


def u2(x0, y0, n, x_list, w_list, w, t):
    U = 0.0
    for i in range(0, n, 1):
        U += f2(x_list[i], x0, y0, w, t) * w_list[i]
    return U


def compute(t0):
    field_x = []
    field_y = []
    field = []
    potential = []
    for x0 in x_axis:
        for y0 in y_axis:
            potential1 = (u1(x0, y0, n=N, x_list=xp2, w_list=wp2, w=w0, t=t0) +
                          u2(x0, y0, n=N, x_list=xp1, w_list=wp1, w=w0, t=t0))
            Ex = (- ((u1(x0 + dx, y0, n=N, x_list=xp2, w_list=wp2, w=w0, t=t0) -
                      u1(x0 - dx, y0, n=N, x_list=xp2, w_list=wp2, w=w0, t=t0)) / (2 * dx))
                  - ((u2(x0 + dx, y0, n=N, x_list=xp1, w_list=wp1, w=w0, t=t0) -
                      u2(x0 - dx, y0, n=N, x_list=xp1, w_list=wp1, w=w0, t=t0)) / (2 * dx)))
            Ey = (- ((u1(x0, y0 + dy, n=N, x_list=xp2, w_list=wp2, w=w0, t=t0) -
                      u1(x0, y0 - dy, n=N, x_list=xp2, w_list=wp2, w=w0, t=t0)) / (2 * dy))
                  - ((u2(x0, y0 + dy, n=N, x_list=xp1, w_list=wp1, w=w0, t=t0) -
                      u2(x0, y0 - dy, n=N, x_list=xp1, w_list=wp1, w=w0, t=t0)) / (2 * dy)))
            E = np.sqrt((Ex ** 2) + (Ey ** 2))
            field_x.append(Ex)
            field_y.append(Ey)
            field.append(E)
            potential.append(potential1)
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
    return apotential_2D_T, afield_x_2D_T, afield_y_2D_T, afield_2D_T


def init():
    apotential_2D_T, afield_x_2D_T, afield_y_2D_T, afield_2D_T = compute(t0=0)
    cs = ax1.contourf(apotential_2D_T, extent=extent, levels=levels, cmap=pl.cm.rainbow, origin='lower')
    cbar1 = fig.colorbar(cs, ax=ax1)
    color = np.log(afield_2D_T)
    stream = ax2.streamplot(x_axis, y_axis, afield_x_2D_T, afield_y_2D_T, color=color, cmap=pl.cm.rainbow,
                            density=2, arrowstyle='->', linewidth=1, arrowsize=1.5)
    return []


def update(frame):
    ax1.clear()
    ax2.clear()
    t = frame * dt
    ax1.set_xlabel('X', size=20)
    ax1.set_ylabel('Y', size=20)
    ax2.set_xlabel('X', size=20)
    ax2.set_ylabel('Y', size=20)
    ax1.set_xlim(-3.0, 3.0)
    ax1.set_ylim(-3.0, 3.0)
    ax2.set_xlim(-3.0, 3.0)
    ax2.set_ylim(-3.0, 3.0)
    ax1.set_title(f'Potential (t = {t})', size=20)
    ax2.set_title(f'Electric field (t = {t})', size=20)
    apotential_2D_T, afield_x_2D_T, afield_y_2D_T, afield_2D_T = compute(t0=t)
    cs = ax1.contourf(apotential_2D_T, extent=extent, levels=levels, cmap=pl.cm.rainbow, origin='lower')

    color = np.log(afield_2D_T)
    stream = ax2.streamplot(x_axis, y_axis, afield_x_2D_T, afield_y_2D_T, color=color, cmap=pl.cm.rainbow,
                            density=2, arrowstyle='->', linewidth=1, arrowsize=1.5)
    return []

ani = animation.FuncAnimation(fig=fig, func=update, frames=range(1, frames + 1), init_func=init, blit=False, repeat=False)
pl.show()

