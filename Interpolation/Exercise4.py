import numpy as np
import scipy.interpolate as sp
import matplotlib.pylab as pl

# 调用sp.splrep()与sp.splev()进行三次样条插值

energy_list = []
signal_list = []
signal_list1 = np.arange(1300, 1800, 1)

with open('calibrate.dat', 'r') as infile:
    for lines in infile:
        words = lines.split()
        energy_list.append(float(words[0]))
        signal_list.append(float(words[1]))
tck = sp.splrep(signal_list, energy_list, k=3, s=0)
energy_list1 = sp.splev(signal_list1, tck)
y = sp.splev(1588, tck)
print(f'1588mV correspnds to {y} keV.')

t, c, k = tck
print(type(tck))
print(len(tck))
print("t =", t)
print("c =", c)
print("k =", k)
pl.xlim(1300, 1800)
pl.ylim(5000, 6000)
pl.xlabel('Signal(mV)')
pl.ylabel('Energy(keV)')
pl.plot(signal_list1, energy_list1, 'r-')
pl.plot(signal_list, energy_list, 'kd')
pl.show()
