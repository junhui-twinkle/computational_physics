import numpy as np
import matplotlib.pylab as pl

n_0 = 1.0
lamda = 0.5
t_0 = 0
nstep = 5000
dt = 0.5

t = t_0
n_num = n_0
n_ana = n_0
n_numerical = []
n_analytical = []
time_list = []
n_numerical.append(n_num)
n_analytical.append(n_ana)
time_list.append(t)

for i in range(0, nstep):
    t += dt
    '''
    Euler's Method
    k1 = - lamda * n_num
    n_num = n_num + k1 * dt
    '''
    '''
    Improved Euler's Method
    k1 = - lamda * n_num
    n_p = n_num + k1 * dt
    k2 = - lamda * n_p
    n_num = n_num + 1 / 2 * (k1 + k2) * dt
    '''
    '''
    RK2
    k1 = - lamda * n_num
    n_mid = n_num + 1 / 2 * k1 * dt
    k2 = - lamda * n_mid
    n_num = n_num + k2 * dt
    '''
    k1 = - lamda * n_num
    n_2 = n_num + 1 / 2 * k1 * dt
    k2 = - lamda * n_2
    n_3 = n_num + 1 / 2 * k2 * dt
    k3 = - lamda * n_3
    n_4 = n_num + k3 * dt
    k4 = - lamda * n_4
    k = 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    n_num = n_num + k * dt
    n_ana = n_0 * np.exp(- lamda * t)
    n_numerical.append(n_num)
    n_analytical.append(n_ana)
    time_list.append(t)

pl.plot(time_list, n_numerical, 'ro', ms=2)
pl.plot(time_list, n_analytical, 'k-')
pl.xlabel('Time')
pl.ylabel('Nuclei amount')
pl.xlim(0, 12)
pl.show()
