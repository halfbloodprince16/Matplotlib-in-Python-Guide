#subplots
import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

xs ,ys = create_plots()
ax1 = fig.add_subplot(221)
plt.plot(xs,ys)

xs ,ys = create_plots()
ax2 = fig.add_subplot(222)
plt.plot(xs,ys)

xs ,ys = create_plots()
ax3 = fig.add_subplot(212)
plt.plot(xs,ys)

plt.show()