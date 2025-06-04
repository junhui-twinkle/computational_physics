import numpy as np
import matplotlib.pylab as pl

N = 101  # number of points
Lhalf = 1.0  # half-length of the stem
Lfull = 2 * Lhalf
h = Lfull / (N - 1)  # integration step
c = 1.0  # determine the unit of field c = 1/4piepsilon
dx = 0.05
dy = 0.05
xx = np.zeros(N)
for i in range(0, N, 1):
    xx[i] = -Lhalf + i * h  # coordinate along the x-axis
x_axis = np.arange(-3, 3, 0.05)
y_axis = np.arange(-3, 3, 0.05)

field_x = []
field_y = []
field = []
potential = []


# 电荷密度函数
def lamda(x):
    y = np.exp(-(x ** 2))
    return y


# 点到任意点的电势
def f(x, x0, y0):
    y = lamda(x)
    r = np.sqrt((x0 - x) ** 2 + y0 ** 2)
    return c * y / r


# 积分到任意点的电势 左矩形
def U(x0, y0, list_points, step):
    U = 0.0
    for i in range(1, len(list_points) - 1, 2):
        U += 1 / 3 * (f(list_points[i - 1], x0, y0) + 4 * f(list_points[i], x0, y0) + f(list_points[i + 1], x0, y0)) * step
    return U


for x0 in x_axis:
    for y0 in y_axis:
        potential.append(U(x0, y0, list_points=xx, step=h))

for x0 in x_axis:
    for y0 in y_axis:
        Ex = -1 * (U(x0 + dx, y0, list_points=xx, step=h) - U(x0 - dx, y0, list_points=xx, step=h)) / (2 * h)
        Ey = -1 * (U(x0, y0 + dy, list_points=xx, step=h) - U(x0, y0 - dy, list_points=xx, step=h)) / (2 * h)
        E = np.sqrt(Ex ** 2 + Ey ** 2)
        field_x.append(Ex)
        field_y.append(Ey)
        field.append(E)

afield_x = np.array(field_x)
afield_y = np.array(field_y)
afield = np.array(field)
apotential = np.array(potential)

afield_x_2D = afield_x.reshape(len(x_axis), len(y_axis))
afield_y_2D = afield_y.reshape(len(x_axis), len(y_axis))
afield_2D = afield.reshape(len(x_axis), len(y_axis))
apotential_2D = apotential.reshape(len(x_axis), len(y_axis))

afield_x_2D_T = afield_x_2D.T
afield_y_2D_T = afield_y_2D.T
afield_2D_T = afield_2D.T
apotential_2D_T = apotential_2D.T

fig = pl.figure(figsize=(15, 7))
ax1 = fig.add_subplot(1, 2, 1)
extent = [-3, 3, -3, 3]
levels = np.arange(0, 5, 0.1)
cs = ax1.contourf(apotential_2D_T, extent=extent, levels=levels, cmap=pl.cm.rainbow, origin='lower')
cbar1 = fig.colorbar(cs, ax=ax1)  # 设置颜色条标签

ax2 = fig.add_subplot(1, 2, 2)
color = np.log(afield_2D_T)
stream = ax2.streamplot(x=x_axis, y=y_axis, u=afield_x_2D_T, v=afield_y_2D_T, color=color, cmap=pl.cm.rainbow,
               linewidth=1.0, density=2, arrowstyle='->', arrowsize=1.5)
cbar2 = fig.colorbar(stream.lines, ax=ax2)
ax1.set_xlabel('X', size=20)
ax1.set_ylabel('Y', size=20)
ax2.set_xlabel('X', size=20)
ax2.set_ylabel('Y', size=20)
ax1.set_xlim(-3.0, 3.0)
ax1.set_ylim(-3.0, 3.0)
ax2.set_xlim(-3.0, 3.0)
ax2.set_ylim(-3.0, 3.0)
ax1.set_title('Potential', size=20)
ax2.set_title('Electric field', size=20)
pl.show()
