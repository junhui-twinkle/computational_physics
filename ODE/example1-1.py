import numpy as np
import matplotlib.pylab as pl

lamda = 0.5
n0 = 1.0
t0 = 0
dt = 0.1
nstep = 5000

nt_numerical = []
nt_analytic = []
time = []
# Euler's Method求解
n_numerical = n0
t = t0

nt_analytic.append(n0)
nt_numerical.append(n0)
time.append(t0)

for i in range(1, nstep):
    t = t0 + i * dt
    n_numerical = n_numerical - lamda * n_numerical * dt
    n_analytic = n0 * np.exp(-lamda * t)
    nt_numerical.append(n_numerical)
    nt_analytic.append(n_analytic)
    time.append(t)

pl.plot(time, nt_numerical, 'ro', ms=2)
pl.plot(time, nt_analytic, 'k-')
pl.xlabel('Time')
pl.ylabel('Nuclei amount')
pl.xlim(0, 12)
pl.show()
