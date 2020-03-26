import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

rect = ax.patch
rect.set_facecolor('k')

N = 31
x = np.arange(N)
y = 100 * np.random.rand(N)

ax.plot(x, y, color='red', linewidth=2.0)

# formatter = mpl.ticker.FormatStrFormatter(u'%.2f руб.')
# ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    print
    'Major ticks on Y-axis %s' % type(tick)
    tick.label1On = True
    tick.label1.set_color('green')
    tick.label2On = True
    tick.label2.set_color('blue')
    # серые деления на оси ОY слева
    tick.tick1line.set_color('grey')
    tick.tick1line.set_markeredgewidth(2)
    tick.tick1line.set_markersize(25)
    # линии вспомогательной сетки для оси OX
    tick.gridOn = True
    tick.gridline.set_color('white')
    tick.gridline.set_linewidth(1.5)

for tick in ax.xaxis.get_major_ticks():
    print
    'Major ticks on X-axis %s' % type(tick)
    tick.label1On = True
    tick.label1.set_color('red')
    tick.label2On = True
    tick.label2.set_color('orange')
    # розовые деления на оси ОX сверху
    tick.tick2line.set_color('pink')
    tick.tick2line.set_markeredgewidth(2)
    tick.tick2line.set_markersize(25)
    # линии вспомогательной сетки для оси OY
    tick.gridOn = True
    tick.gridline.set_color('yellow')
    tick.gridline.set_linewidth(2.)

# save('pic_9_1', fmt='png')
# save('pic_9_1', fmt='pdf')

plt.show()