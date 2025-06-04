import numpy as np
import matplotlib.pylab as pl

energy_list = []
signal_list = []


def Lagrange_interpolation(xlist, ylist, n, x):
    result = 0.0
    for i in range(0, n):
        a = 1.0
        for j in range(0, n):
            if j != i:
                a *= (x - xlist[j]) / (xlist[i] - xlist[j])
        result += a * ylist[i]
    return result


with open('calibrate.dat', 'r') as infile:
    for lines in infile:
        words = lines.split()
        energy_list.append(float(words[0]))
        signal_list.append(float(words[1]))

signal_list1 = np.arange(1300, 1800, 1)
energy_list1 = Lagrange_interpolation(signal_list, energy_list, 5, signal_list1)

y1 = Lagrange_interpolation(signal_list, energy_list, 5, 1588)
pl.xlabel('Signal(mV)')
pl.ylabel('Energy(keV)')
pl.xlim(1300, 1800)
pl.ylim(5000, 6000)
pl.plot(signal_list1, energy_list1, 'r')
pl.plot(signal_list, energy_list, 'kd')
print(f'1588mV corresponds to {y1} keV.')
pl.show()
