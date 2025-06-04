import numpy as np
import matplotlib.pylab as pl
import scipy.interpolate as sp

# 调用sp.lagrange函数
energy_list = []
signal_list = []

with open('calibrate.dat', 'r') as infile:
    for lines in infile:
        words = lines.split()
        energy_list.append(float(words[0]))
        signal_list.append(float(words[1]))

Lagrange_interpolation = sp.lagrange(signal_list, energy_list)
signal_list1 = np.arange(1300, 1800, 1)
energy_list1 = Lagrange_interpolation(signal_list1)

y1 = Lagrange_interpolation(1588)
pl.xlabel('Signal(mV)')
pl.ylabel('Energy(keV)')
pl.xlim(1300, 1800)
pl.ylim(5000, 6000)
pl.plot(signal_list1, energy_list1, 'r')
pl.plot(signal_list, energy_list, 'kd')
print(f'1588mV corresponds to {y1} keV.')
pl.show()
