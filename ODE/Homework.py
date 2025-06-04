import numpy as np
import matplotlib.pylab as pl

x0 = 0
velocity0 = 10
t0 =0.0
nstep = 2000
alpha = 1
beta = 1
gamma = 5
delta = 1
omega = 1
dt = 0.2


def fx(t, x, velocity):
    y = velocity
    return y


def fvelocity(t, x, velocity):
    y = -gamma * velocity - alpha * x - beta * x * x * x + delta * np.cos(omega * t)
    return y


def rk4(t, x, velocity):
    k1 = fx(t=t, x=x, velocity=velocity)
    l1 = fvelocity(t=t, x=x, velocity=velocity)
    k2 = fx(t=t + dt / 2, x=x + k1 * dt / 2, velocity=velocity + l1 * dt / 2)
    l2 = fvelocity(t=t + dt / 2, x=x + k1 * dt / 2, velocity=velocity + l1 * dt / 2)
    k3 = fx(t=t + dt / 2, x=x + k2 * dt / 2, velocity=velocity + l2 * dt / 2)
    l3 = fvelocity(t=t + dt / 2, x=x + k2 * dt / 2, velocity=velocity + l2 * dt / 2)
    k4 = fx(t=t + dt, x=x + k3 * dt, velocity=velocity + l3 * dt)
    l4 = fvelocity(t=t + dt, x=x + k3 * dt, velocity=velocity + l3 * dt)
    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    l = (l1 + 2 * l2 + 2 * l3 + l4) / 6
    x += k * dt
    velocity += l * dt
    return x, velocity


xT = []
velocityT = []
timeT = []

t = t0
x = x0
velocity = velocity0
timeT.append(t)
xT.append(x)
velocityT.append(velocity)

for i in range(nstep):
    x, velocity = rk4(t, x, velocity)
    t += dt
    timeT.append(t)
    xT.append(x)
    velocityT.append(velocity)

fig =pl.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(timeT, xT, 'r-', label=fr'$x_0={x0}\;v_0={velocity0}$', lw=1)
ax2.plot(xT, velocityT, 'r-', label=fr'$x_0={x0}\;v_0={velocity0}$', lw=1)
pl.subplots_adjust(hspace=0.35, wspace=0.3)
ax1.set_ylabel(r'x', fontsize=20)
ax1.set_xlabel(r'Time', fontsize=20)
ax2.set_ylabel(r'x', fontsize=20)
ax2.set_xlabel(r'Velocity', fontsize=20)
# ax1.set_xlim(0, 60)
# ax1.set_ylim(-1.5, 1.5)
# ax2.set_xlim(-1.5, 1.5)
# ax2.set_ylim(-1.5, 1.5)

ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
fig.suptitle(fr"Duffing Equation (RK4 Method), $\alpha$={alpha}, $\beta$={beta}, $\gamma$={gamma}, $\delta$={delta}, $\omega$={omega}", fontsize=18)
pl.savefig(fr"Duffing Equation (RK4 Method)_alpha={alpha}_beta={beta}_gamma={gamma}_delta$={delta}_omega$={omega}.png")
pl.show()

