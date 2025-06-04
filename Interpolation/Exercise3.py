import numpy as np
import matplotlib.pylab as pl
import scipy.interpolate as sp

# 调用sp.lagrange函数，两次分段插值
energy_list = []
signal_list = []

with open('calibrate.dat', 'r') as infile:
    for lines in infile:
        words = lines.split()
        energy_list.append(float(words[0]))
        signal_list.append(float(words[1]))

# 两个分段插值
lag1 = sp.lagrange(signal_list[0:3], energy_list[0:3])
lag2 = sp.lagrange(signal_list[2:], energy_list[2:])
signal1 = np.arange(1300, signal_list[2], 1)
signal2 = np.arange(signal_list[2], 1800)
energy1 = lag1(signal1)
energy2 = lag2(signal2)

pl.xlabel('Signal(mV)')
pl.ylabel('Energy(keV)')
pl.xlim(1300, 1800)
pl.ylim(5000, 6000)
pl.plot(signal_list, energy_list, 'kd')
pl.plot(signal1, energy1, 'r-')
pl.plot(signal2, energy2, 'r-')
pl.show()
