import numpy as np
import matplotlib.pylab as pl
import matplotlib.animation as animation

g = 9.8
xl = 9.8
dt = 0.04
theta0 = 1.2
omega0 = 0.0
t0 = 0.0
nstep = 2000
q = 0.5
force = 0.5
force_omega = 2 / 3
t_list = []
u_list = []
v_list = []

def f1(t, u, v):
    y = v
    return v


def f2(t, u, v):
    y = - g / xl * np.sin(u) - q * v + force * np.sin(force_omega * t)
    return y


def rk4(t, u, v):
    k1 = f1(t, u, v)
    l1 = f2(t, u, v)
    u_2 = u + 1 / 2 * k1 * dt
    v_2 = v + 1 / 2 * l1 * dt
    k2 = f1(t + 1 / 2 * dt, u_2, v_2)
    l2 = f2(t + 1 / 2 * dt, u_2, v_2)
    u_3 = u + 1 / 2 * k2 * dt
    v_3 = v + 1 / 2 * l2 * dt
    k3 = f1(t + 1 / 2 * dt, u_3, v_3)
    l3 = f2(t + 1 / 2 * dt, u_3, v_3)
    u_4 = u + k3 * dt
    v_4 = v + l3 * dt
    k4 = f1(t + dt, u_4, v_4)
    l4 = f2(t + dt, u_4, v_4)
    k = 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    l = 1 / 6 * (l1 + 2 * l2 + 2 * l3 + l4)
    u += k * dt
    v += l * dt
    if u > np.pi:
        u -= 2 * np.pi
    if u < -np.pi:
        u += 2 * np.pi
    return u, v


def get_coordinate(u):
    x = xl * np.sin(u)
    y = -xl * np.cos(u)
    return x, y


t = t0
u = theta0
v = omega0
t_list.append(t)
u_list.append(u)
v_list.append(v)

for i in range(0, nstep):
    u, v = rk4(t, u, v)
    t += dt
    u_list.append(u)
    v_list.append(v)
    t_list.append(t)

fig = pl.figure(figsize=(6, 6))
ax = fig.add_subplot(aspect='equal')
x0, y0 = get_coordinate(u=theta0)
line1, = ax.plot([0, x0], [0, y0], lw=3, c='k')

bob_radius = 0.5
circle1 = ax.add_patch(pl.Circle(get_coordinate(u=theta0), bob_radius, fc='r', zorder=3))

ax.set_xlim(-xl * 1.2, xl * 1.2)
ax.set_ylim(-xl * 1.2, xl * 1.2)


def func(num, line, circle, u_list):
    x, y = get_coordinate(u_list[num])
    line.set_data([0, x], [0, y])
    circle.set_center((x, y))
    return line, circle

fig.suptitle(fr"Forced Pendulum Motion Animation $q={q}\;f={force}$", fontsize=16)
ani = animation.FuncAnimation(fig, func, frames=nstep, fargs=(line1, circle1, u_list),repeat=False, interval=dt * 0.1)
ani.save("forced_pendulum_animation_f0.5.gif", writer="pillow", fps=20)
pl.show()
