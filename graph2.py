import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, NullFormatter

majorLocator   = MultipleLocator(5)
# Автоматический подбор промежуточных делений. Количество созданных делений равно n-1
minorLocator   = AutoMinorLocator(n=3)

majorFormatter = FormatStrFormatter('%d')
minorFormatter = FormatStrFormatter('%.2f')

N = 10
x = np.arange(-N, N+1, 1)
y = (np.random.random(len(x))*2.-1)*N

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.plot(x, y)

xax = ax.xaxis
yax = ax.yaxis

xax.set_major_locator(majorLocator)
xax.set_major_formatter(majorFormatter)
yax.set_major_locator(majorLocator)
yax.set_major_formatter(majorFormatter)

xax.set_minor_locator(minorLocator)
xax.set_minor_formatter(minorFormatter)
yax.set_minor_locator(minorLocator)
yax.set_minor_formatter(NullFormatter()) # скрываем подписи вспомогательных делений по оси OY

ax.grid(True, which='major', color='k', linestyle='solid')

ax.grid(True, which='minor', color='grey', linestyle='dashed', alpha=0.5)
#yax.grid(True, which='minor', color='grey', linestyle='dashed', alpha=0.5)

#for label in xax.get_ticklabels():
#    label.set_color('red')
#    label.set_rotation(30)
#    label.set_fontsize(12)

# для вспомогательных for the minor ticks, use no labels; default NullFormatter

# save('pic_9_2_1', fmt='png')
# save('pic_9_2_1', fmt='pdf')

plt.show()