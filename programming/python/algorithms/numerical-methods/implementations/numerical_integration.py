import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("center")
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

plt.plot(x, y, label="f(x)=sin(x)")
plt.legend()

a = 0
b = np.pi
n = 100
width = (b - a) / n
x = a

for i in range(n):
    rect = mpatches.Rectangle((x, 0), width, np.sin(x), fill=False, color="purple", linewidth=2)
    plt.gca().add_patch(rect)
    x += width

plt.show()