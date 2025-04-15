import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0-np.pi*4, np.pi*4, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1)
ax.plot(x, y2)

plt.show()