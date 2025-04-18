import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 10000

x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

Z = np.zeros_like(C, dtype=complex)
mandelbrot_set = np.zeros(C.shape, dtype=int)

for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    mandelbrot_set[mask] = i

ax.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.show()