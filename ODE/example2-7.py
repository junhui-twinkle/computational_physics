import numpy as np
import matplotlib.pylab as pl

g = 9.8
xl = 9.8
dt = 0.04
theta1 = 1.2
omega0 = 0.0
t0 = 0.0
nstep = 5000
q1 = 0.5
force = 1.5
force_omega = 2 / 3
t_list = []
u_list = []
v_list = []
t_list1 = []
u_list1 = []
v_list1 = []
t_list2 = []
u_list2 = []
v_list2 = []

def f1(t, u, v):
    y = v
    return v


def f2(t, u, v, q, f):
    y = - g / xl * np.sin(u) - q * v + f * np.sin(force_omega * t)
    return y


def rk4(t, u, v, q, f):
    k1 = f1(t, u, v)
    l1 = f2(t, u, v, q, f)
    u_2 = u + 1 / 2 * k1 * dt
    v_2 = v + 1 / 2 * l1 * dt
    k2 = f1(t + 1 / 2 * dt, u_2, v_2)
    l2 = f2(t + 1 / 2 * dt, u_2, v_2, q, f)
    u_3 = u + 1 / 2 * k2 * dt
    v_3 = v + 1 / 2 * l2 * dt
    k3 = f1(t + 1 / 2 * dt, u_3, v_3)
    l3 = f2(t + 1 / 2 * dt, u_3, v_3, q, f)
    u_4 = u + k3 * dt
    v_4 = v + l3 * dt
    k4 = f1(t + dt, u_4, v_4)
    l4 = f2(t + dt, u_4, v_4, q, f)
    k = 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    l = 1 / 6 * (l1 + 2 * l2 + 2 * l3 + l4)
    u += k * dt
    v += l * dt
    if u > np.pi:
        u = u - 2 * np.pi
    if u < - np.pi:
        u = u + 2 * np.pi
    return u, v


t = t0
u = theta1
v = omega0
t_list.append(t)
u_list.append(u)
v_list.append(v)

for i in range(0, nstep):
    u, v = rk4(t, u, v, q1, force)
    t += dt
    u_list.append(u)
    v_list.append(v)
    t_list.append(t)

t = t0
u = theta1
v = omega0
t_list1.append(t)
u_list1.append(u)
v_list1.append(v)

for i in range(0, nstep):
    u, v = rk4(t, u, v, q1, force)
    t += dt
    u_list1.append(u)
    v_list1.append(v)
    t_list1.append(t)

t = t0
u = theta1
v = omega0
t_list2.append(t)
u_list2.append(u)
v_list2.append(v)

for i in range(0, nstep):
    u, v = rk4(t, u, v, q1, force)
    t += dt
    u_list2.append(u)
    v_list2.append(v)
    t_list2.append(t)

fig = pl.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(t_list, u_list, 'r-', label=fr'$\theta_0={theta1}\;q={q1}\;f={force}$', lw=1)
ax2.plot(u_list, v_list, 'r-', label=fr'$\theta_0={theta1}\;q={q1}\;f={force}$', lw=1)

# ax1.plot(t_list1, u_list1, 'b-', label=fr'$\theta_0={theta1}\;q={q1}$', lw=1)
# ax2.plot(u_list1, v_list1, 'b-', label=fr'$\theta_0={theta1}\;q={q1}$', lw=1)

# ax1.plot(t_list2, u_list2, 'g-', label=fr'$\theta_0={theta1}\;q={q1}$', lw=1)
# ax2.plot(u_list2, v_list2, 'g-', label=fr'$\theta_0={theta1}\;q={q1}$', lw=1)

pl.subplots_adjust(hspace=0.35, wspace=0.3)
ax1.set_xlabel(r'$\theta$', fontsize=20)
ax1.set_ylabel(r'Time', fontsize=20)
ax2.set_xlabel(r'$\theta$', fontsize=20)
ax2.set_ylabel(r'$\omega$', fontsize=20)
# ax1.set_xlim(0, 80)
# ax1.set_ylim(-3.5, 3.5)
# ax2.set_xlim(-3.5, 3.5)
# ax2.set_ylim(-3.5, 3.5)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
fig.suptitle("Forced Simple Pendulum Motion (RK4)", fontsize=18)
pl.savefig(f"Forced_Simple_Pendulum_Motion_rk4_f=1.5.png")
pl.show()
