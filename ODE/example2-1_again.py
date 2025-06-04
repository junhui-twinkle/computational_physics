import numpy as np
import matplotlib.pylab as pl

g = 9.8
xl = 9.8
dt = 0.04
theta0 = 0.2
omega0 = 0.0
t0 = 0.0
nstep = 2000
t_list = []
u_list = []
v_list = []

def f1(t, u, v):
    y = v
    return v


def f2(t, u, v):
    y = - g / xl * np.sin(u)
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
    return u, v


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

fig = pl.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(t_list, u_list, 'r-', label=fr'$\theta_0={theta0}$', lw=1)
ax2.plot(u_list, v_list, 'r-', label=fr'$\theta_0={theta0}$', lw=1)
pl.subplots_adjust(hspace=0.35, wspace=0.3)
ax1.set_xlabel(r'$\theta$', fontsize=20)
ax1.set_ylabel(r'Time', fontsize=20)
ax2.set_xlabel(r'$\theta$', fontsize=20)
ax2.set_ylabel(r'$\omega$', fontsize=20)
ax1.set_xlim(0, 30)
ax1.set_ylim(-1.5, 1.5)
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax1.legend()
ax2.legend(loc='upper right', title='Legend Title', shadow=True, facecolor='pink')
fig.suptitle("Simple Pendulum Motion (RK4)", fontsize=18)
pl.show()
