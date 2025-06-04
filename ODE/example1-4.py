import numpy as np
import matplotlib.pylab as pl

lamda = 0.5
n0 = 1.0
t0 = 0
dt = 0.5
nstep = 5000

n_numerical = n0
n_analytical = n0

time = []
nt_numerical = []
nt_analytical = []

nt_numerical.append(n_numerical)
nt_analytical.append(n_analytical)
time.append(t0)

for i in range(1, nstep):
    t = t0 + i * dt
    k1 = - lamda * n_numerical  # n点斜率
    n_mid1 = n_numerical + (k1 * dt) / 2  # 中点值1
    k2 = - lamda * n_mid1  # 中点斜率1
    n_mid2 = n_numerical + (k2 * dt) / 2 # 中点值2
    k3 = - lamda * n_mid2  # 中点斜率2
    n_3 = n_numerical + k3 * dt  # 第三点值
    k4 = - lamda * n_3  # 第三点斜率
    n_numerical = n_numerical + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
    n_analytical = n0 * np.exp(-lamda * t)
    time.append(t)
    nt_numerical.append(n_numerical)
    nt_analytical.append(n_analytical)

pl.xlabel('Time')
pl.ylabel('Nuclei amount')
pl.xlim(0, 12)
pl.plot(time, nt_analytical, 'k-')
pl.plot(time, nt_numerical, 'ro', ms=2)
pl.savefig(f"4th Runge Kuttar Method dt={dt}.png")
pl.show()
