from typing import cast

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.axes._subplots import SubplotBase
from PyQt5.Qt import right


class MplCanvas(QWidget):  # FigureCanvasQTAgg):

    def __init__(self, parent=None, *args, **kwargs):
        # def __init__(self, *args):
        #     super(QWidget, self).__init__(*args)
        #     super(FigureCanvasQTAgg, self).__init__(self.figure)

        QWidget.__init__(self, parent=parent)
        # plt.rcParams['figure.constrained_layout.use'] = True
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        # ax = self.figure.add_subplot(111)
        gridspec = self.figure.add_gridspec(nrows=1, ncols=1, top=0.99, bottom=0.01, right=0.99)
        ax = self.figure.add_subplot(gridspec[0, 0])
        self.ax: Axes = cast(Axes, ax)
        self.ax.xaxis.set_visible(False)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class HeatMapMplCanvas(MplCanvas):
    def __init__(self, parent=None, *args, **kwargs):
        MplCanvas.__init__(self, parent=parent, *args, **kwargs)
        self.ax.get_yaxis().set_visible(False)
        self.ax.get_gridspec().update(right=0.0)
        self.canvas.draw()
        self.update()
        # TODO make sure the update geometry works. Till now, I just hide the Y Axis
