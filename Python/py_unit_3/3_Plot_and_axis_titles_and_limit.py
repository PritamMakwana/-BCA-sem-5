import numpy as np
import pylab as pl
# Make an array of x values
x = [1, 2, 3, 4, 5]
# Make an array of y values for each x value
y = [1, 4, 9, 16, 25]
# use pylab to plot x and y
pl.plot(x, y)
# give plot a title
pl.title('Plot of y vs. x')
# make axis labels
pl.xlabel('x axis')
pl.ylabel('y axis')
# set axis limits
pl.xlim(0.0, 7.0)
pl.ylim(0.0, 30.)
# show the plot on the screen
pl.show()