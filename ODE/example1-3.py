import numpy as np
import matplotlib.pylab as pl

lamda = 0.5
n0 = 1.0
t0 = 0
dt = 1.5
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
    k1 = -lamda * n_numerical  # n点斜率
    n_mid = n_numerical + k1 * dt / 2  # 中点值
    k2 = - lamda * n_mid  # 中点斜率
    n_numerical = n_numerical + k2 * dt # n+1点值
    n_analytical = n0 * np.exp(-lamda * t)
    time.append(t)
    nt_numerical.append(n_numerical)
    nt_analytical.append(n_analytical)

pl.xlabel('Time')
pl.ylabel('Nuclei amount')
pl.xlim(0, 12)
pl.plot(time, nt_analytical, 'k-')
pl.plot(time, nt_numerical, 'ro', ms=2)
pl.savefig(f"2rd Runge Kuttar Method dt={dt}.png")
pl.show()
