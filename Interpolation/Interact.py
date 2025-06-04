import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_legendre

# 参数设置
Lhalf = 1.0
c = 1.0
dx = 0.1
dy = 0.1
N = st.sidebar.slider("Gauss-Legendre 点数 N", min_value=5, max_value=50, value=20)
w0 = st.sidebar.slider("角频率 ω", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
h = st.sidebar.slider("电荷间距 h", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
t = st.slider("时间 t", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# 网格设置
x_axis = np.arange(-3, 3, 0.1)
y_axis = np.arange(-3, 3, 0.1)
xk, wk = roots_legendre(N)
xp1 = xk * Lhalf
wp1 = wk * Lhalf
xp2 = xk * Lhalf + Lhalf
wp2 = wk * Lhalf

# 电荷分布函数
def lamda1(x, w, t):
    return np.exp(-x**2) * np.cos(w * t)

def lamda2(x, w, t):
    return -1.5 * np.exp(-x**2) * np.cos(w * t)

def f1(x, x0, y0, w, t):
    r = np.sqrt((x0 - x) ** 2 + (y0 - h) ** 2)
    return c * lamda1(x, w, t) / r

def f2(x, x0, y0, w, t):
    r = np.sqrt((x0 - x) ** 2 + (y0 + h) ** 2)
    return c * lamda2(x, w, t) / r

def u1(x0, y0):
    return np.sum([f1(x, x0, y0, w0, t) * w for x, w in zip(xp2, wp2)])

def u2(x0, y0):
    return np.sum([f2(x, x0, y0, w0, t) * w for x, w in zip(xp1, wp1)])

# 计算电势与电场
potential = []
field_x = []
field_y = []
field = []

for x0 in x_axis:
    for y0 in y_axis:
        U = u1(x0, y0) + u2(x0, y0)
        Ex = -((u1(x0 + dx, y0) - u1(x0 - dx, y0)) + (u2(x0 + dx, y0) - u2(x0 - dx, y0))) / (2 * dx)
        Ey = -((u1(x0, y0 + dy) - u1(x0, y0 - dy)) + (u2(x0, y0 + dy) - u2(x0, y0 - dy))) / (2 * dy)
        E = np.sqrt(Ex**2 + Ey**2)
        potential.append(U)
        field_x.append(Ex)
        field_y.append(Ey)
        field.append(E)

# 变成二维数组
shape = (len(x_axis), len(y_axis))
potential = np.array(potential).reshape(shape).T
field_x = np.array(field_x).reshape(shape).T
field_y = np.array(field_y).reshape(shape).T
field = np.array(field).reshape(shape).T

# 绘图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
extent = [-3, 3, -3, 3]
levels = np.arange(-4, 4, 0.1)

cs = ax1.contourf(potential, extent=extent, levels=levels, cmap='rainbow', origin='lower')
ax1.set_title(f"Potential (t = {t:.1f})")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

color = np.log(field + 1e-5)
stream = ax2.streamplot(x_axis, y_axis, field_x, field_y, color=color, cmap='rainbow', density=2)
ax2.set_title(f"Electric Field (t = {t:.1f})")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

st.pyplot(fig)
