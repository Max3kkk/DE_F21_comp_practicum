import sys
import controller
import model
import matplotlib
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        s2 = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(model.exact_sol.get_grid().x_values, model.exact_sol.get_grid().y_values, 'g')
        s2.axes.plot(model.imp_euler_met.get_grid().x_values, model.imp_euler_met.get_grid().y_values, 'r')
        self.setCentralWidget(sc)
        self.setMenuWidget(s2)

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
