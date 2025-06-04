import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([[1.1, 2, 3, 6], [4, 5, 6, 7], [5, 8, 100, 2]])
c = np.zeros((2, 3))
d = np.ones((2, 4))
e = np.eye(4)
f = np.arange(0, 10, 2)
g = np.linspace(0, 10, 2)

'''
print(a.shape)      # 数组形状 → (2, 3)
print(a.ndim)      # 维度 → 2
print(a.size)       # 总元素个数 → 6
print(a.dtype)      # 数据类型 → int64 / float64
print(b.shape)      # 数组形状 → (2, 3)
print(b.ndim)      # 维度 → 2
print(b.size)       # 总元素个数 → 6
print(b.dtype)      # 数据类型 → int64 / float64


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


print(a[1])
print(b[1])
print(b[1, :])
print(b[1, 2])
print(b[:, 1])
print(b[0:2, :])
print(a + 1)
print(np.sqrt(b))
print(np.exp(b))


a1 = a.reshape((7, 1))
b1 = b.T
b2 = b.flatten()
b3 = b.reshape(2, 6)
b.shape = (2, 6)
print(a1)
print(b1)
print(b2)
print(b3)
print(b)
'''

xlist = np.zeros(100)
print(type(len(xlist)))
print(len(xlist))