import numpy as np
import matplotlib.pylab as pl
import matplotlib.animation as animation
import random
import sys


def func(num, xlist, ylist, line):
    line.set_data(xlist[0:num], ylist[0:num])
    return (line,)


try:
    nstep = int(input("Please enter the number of random walk steps (99 < n < 30001): "))
except ValueError:
    print('Please enter an integer.')
except Exception as e:
    print(f'Unknown Fault: {type(e).__name__} Fault Description: {e}')
else:
    if nstep < 100:
        print('Too few steps!')
        sys.exit()
    if nstep > 30000:
        print('Too many steps!')
        sys.exit()
    nsteplist = np.arange(0, nstep, 1)
    iwalkers = 10000
    anis = []
    r2list = np.zeros(nstep, dtype=float)  # 存储每一步的均方位移
    ree = np.zeros(iwalkers, dtype=float)  # 存储每次游走后的链段距
    random.seed(None)
    for iwalker in range(0, iwalkers):
        if iwalker < 3:
            with open(f'random_walk_{iwalker}.dat', 'w') as wfile:
                x = 0.0
                y = 0.0
                xlist1 = []
                ylist1 = []
                xlist1.append(x)
                ylist1.append(y)
                for istep in range(0, nstep):
                    theta = random.random() * 2.0 * np.pi
                    dx = np.cos(theta)
                    dy = np.sin(theta)
                    x += dx
                    y += dy
                    xlist1.append(x)
                    ylist1.append(y)
                    wfile.write('%d\t%.2f\t%.2f\n' % (istep, x, y))
                    r2 = x * x + y * y
                    r2list[istep] += r2 / iwalkers
                ree[iwalker] = np.sqrt(x * x + y * y)
                fig1 = pl.figure(figsize=(5, 5))
                line1, = pl.plot([], [], 'g', lw=1)
                pl.xlim(-100, 100)
                pl.ylim(-100, 100)
                pl.xlabel('X', size=20)
                pl.ylabel('Y', size=20)
                ani = animation.FuncAnimation(fig1, func, frames=nstep, fargs=(xlist1, ylist1, line1),
                                              interval=0, blit=True)
                anis.append(ani)
        else:
            x = 0.0
            y = 0.0
            for istep in range(0, nstep):
                theta = random.random() * 2.0 * np.pi
                dx = np.cos(theta)
                dy = np.sin(theta)
                x += dx
                y += dy
                r2 = x * x + y * y
                r2list[istep] += r2 / iwalkers
            ree[iwalker] = np.sqrt(x * x + y * y)
    hist, edges = np.histogram(ree, bins=50)
    dist = (edges[0:-1] + edges[1:]) / 2
    probility_density = hist / (2 * np.pi * dist)
    fig_MSD = pl.figure()
    pl.xlabel('Steps')
    pl.ylabel('MSD')
    pl.plot(nsteplist, r2list)
    fig_PDF = pl.figure()
    pl.xlabel('Distance')
    pl.ylabel('Probility Density')
    pl.plot(dist, probility_density)
    pl.show()
