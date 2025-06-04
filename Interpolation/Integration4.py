from scipy.special import roots_legendre
import matplotlib.pylab as pl


def f(x):
    return x ** 4 - 2 * x +1


N1 = 3
N2 = 10
N3 = 20
a = 0.0
b = 2.0
xk, wk = roots_legendre(N1)
xk2, wk2 = roots_legendre(N2)
xk3, wk3 = roots_legendre(N3)
xp = xk * (b - a) / 2 + (a + b) / 2
wp = wk * (b - a) / 2

s1 = 0
for i in range(0, N1, 1):
    s1 += wp[i] * f(xp[i])

print(s1)

fig = pl.figure(figsize=(15, 7))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
ax1.stem(xk, wk)
ax2.stem(xk2, wk2)
ax3.stem(xk3, wk3)
ax1.set_xlim(-1.1, 1.1)
ax1.set_ylim(0, 1)
ax1.set_xlabel('$x_k$', size=20)
ax1.set_ylabel('$w_k$', size=20)
ax2.set_xlim(-1.1, 1.1)
ax2.set_ylim(0, 1)
ax2.set_xlabel('$x_k$', size=20)
ax2.set_ylabel('$w_k$', size=20)
ax3.set_xlim(-1.1, 1.1)
ax3.set_ylim(0, 1)
ax3.set_xlabel('$x_k$', size=20)
ax3.set_ylabel('$w_k$', size=20)
pl.show()
