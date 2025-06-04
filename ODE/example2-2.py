import numpy as np
import matplotlib.pylab as pl

g = 9.8
xl = 9.8
dt = 0.04
theta0 = 0.2
theta1 = 1.2
omega0 = 0.0
t0 = 0.0
nstep = 2000
twopi = 2 * np.pi


def fTheta(t, theta, omega):
    y = omega
    return y


def fOmega(t, theta, omega):
    y = -g / xl * np.sin(theta)
    return y


def rk4(t, theta, omega):
    k1 = fTheta(t=t, theta=theta, omega=omega)
    l1 = fOmega(t=t, theta=theta, omega=omega)
    k2 = fTheta(t=t + dt / 2, theta=theta + k1 * dt / 2, omega=omega + l1 * dt / 2)
    l2 = fOmega(t=t + dt / 2, theta=theta + k1 * dt / 2, omega=omega + l1 * dt / 2)
    k3 = fTheta(t=t + dt / 2, theta=theta + k2 * dt / 2, omega=omega + l2 * dt / 2)
    l3 = fOmega(t=t + dt / 2, theta=theta + k2 * dt / 2, omega=omega + l2 * dt / 2)
    k4 = fTheta(t=t + dt, theta=theta + k3 * dt, omega=omega + l3 * dt)
    l4 = fOmega(t=t + dt, theta=theta + k3 * dt, omega=omega + l3 * dt)
    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    l = (l1 + 2 * l2 + 2 * l3 + l4) / 6
    theta += k * dt
    omega += l * dt
    return theta, omega


thetaT = []
omegaT = []
timeT = []
thetaT1 = []
omegaT1 = []
timeT1 = []

t = t0
theta = theta0
omega = omega0
timeT.append(t)
thetaT.append(theta)
omegaT.append(omega)

for i in range(nstep):
    theta, omega = rk4(t, theta, omega)
    t += dt
    timeT.append(t)
    thetaT.append(theta)
    omegaT.append(omega)

t=t0
theta = theta1
omega = omega0
timeT1.append(t)
thetaT1.append(theta)
omegaT1.append(omega)

for i in range(nstep):
    theta, omega = rk4(t, theta, omega)
    t += dt
    timeT1.append(t)
    thetaT1.append(theta)
    omegaT1.append(omega)

fig =pl.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(timeT, thetaT, 'r-', label=fr'$\theta_0={theta0}$', lw=1)
ax2.plot(thetaT, omegaT, 'r-', label=fr'$\theta_0={theta0}$', lw=1)
ax1.plot(timeT1, thetaT1, 'b-', label=fr'$\theta_0={theta1}$', lw=1)
ax2.plot(thetaT1, omegaT1, 'b-', label=fr'$\theta_0={theta1}$', lw=1)
pl.subplots_adjust(hspace=0.35, wspace=0.3)
ax1.set_ylabel(r'$\theta$', fontsize=20)
ax1.set_xlabel(r'Time', fontsize=20)
ax2.set_ylabel(r'$\theta$', fontsize=20)
ax2.set_xlabel(r'$\omega$', fontsize=20)
ax1.set_xlim(0, 30)
ax1.set_ylim(-1.5, 1.5)
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)

ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
fig.suptitle(fr"Comparison of Simple Pendulum Motions ($\theta_0={theta0}\ and\ \theta_0={theta1}$)", fontsize=18)
pl.savefig(f"pendulum_compare_theta0={theta0}_and_theta1={theta1}_rk4.png")
pl.show()

