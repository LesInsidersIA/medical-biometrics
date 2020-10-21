import numpy as np
import matplotlib.pyplot as plt
import imageio

class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('Use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()

dirname = 'data/'

# read as volume
vol = imageio.volread(dirname, 'DICOM')

fig, ax = plt.subplots(1, 1)
tracker = IndexTracker(ax, vol)


fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
plt.show()