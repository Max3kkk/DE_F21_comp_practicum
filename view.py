import sys

import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
)
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import controller
import model
from main_window import UiMainWindow

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._canvas = MplCanvas()
        self._axes = self._canvas.axes
        self.refresh()

        toolbar = NavigationToolbar2QT(self._canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self._canvas)
        self.setLayout(layout)
        self.show()

    def refresh(self):
        pass

    def _update_values(self, grids, params):
        self._axes.cla()
        for grid in [grids[x] for x in range(len(grids)) if params[x]]:
            self.plot(grid[0].x_values, grid[0].y_values, grid[1])
        self._canvas.draw()

    def plot(self, x: list, y: list, desc: str):
        if model.dt.show_dots is True:
            self._axes.plot(x, y, '-D', label=desc)
        else:
            self._axes.plot(x, y, '-', label=desc)
        self._axes.legend()


class Window(QMainWindow, UiMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setupUi(self)
        self._connect_signals_slots()
        self._set_default_values()

    def _connect_signals_slots(self):
        self.n0_err_spinBox.valueChanged['int'].connect(self.change_rng_err)
        self.N_err_spinBox.valueChanged['int'].connect(self.change_rng_err)
        self.exact_sol_checkBox.clicked.connect(self.change_checkbox)
        self.euler_met_checkBox.clicked.connect(self.change_checkbox)
        self.imp_euler_met_checkBox.clicked.connect(self.change_checkbox)
        self.rungekutta_met_checkBox.clicked.connect(self.change_checkbox)
        self.show_dots_checkBox.clicked.connect(self.change_point_marker)
        self.X_doubleSpinBox.valueChanged['double'].connect(self.change_grid)
        self.N_spinBox.valueChanged['int'].connect(self.change_grid)
        self.x0_doubleSpinBox.valueChanged['double'].connect(self.change_grid)
        self.y0_doubleSpinBox.valueChanged['double'].connect(self.change_grid)

    def _set_default_values(self):
        self.n0_err_spinBox.setValue(model.dt.rng_err_n0)
        self.N_err_spinBox.setValue(model.dt.rng_err_n)
        self.X_doubleSpinBox.setValue(model.dt.main_grid.x_end)
        self.N_spinBox.setValue(model.dt.main_grid.step_num)
        self.x0_doubleSpinBox.setValue(model.dt.main_grid.x_start)
        self.y0_doubleSpinBox.setValue(model.dt.main_grid.y_start)
        self.exact_sol_checkBox.setChecked(model.dt.show_exact)
        self.euler_met_checkBox.setChecked(model.dt.show_euler)
        self.imp_euler_met_checkBox.setChecked(model.dt.show_imp_euler)
        self.rungekutta_met_checkBox.setChecked(model.dt.show_runge_kutta)
        self.show_dots_checkBox.setChecked(model.dt.show_dots)

    def change_rng_err(self):
        if controller.change_rng_err(self.n0_err_spinBox.value(), self.N_err_spinBox.value()):
            self.RangeErrorsWidget.refresh()
        else:
            self.n0_err_spinBox.setValue(model.dt.rng_err_n0)
            self.N_err_spinBox.setValue(model.dt.rng_err_n)

    def change_checkbox(self):
        if controller.change_checkbox(self.exact_sol_checkBox.isChecked(), self.euler_met_checkBox.isChecked(),
                                      self.imp_euler_met_checkBox.isChecked(),
                                      self.rungekutta_met_checkBox.isChecked()):
            self.SolutionsWidget.refresh()
            self.ErrorsWidget.refresh()
            self.RangeErrorsWidget.refresh()

    def change_grid(self):
        if controller.change_grid(model.Grid(self.N_spinBox.value(), self.X_doubleSpinBox.value(),
                                             self.x0_doubleSpinBox.value(), self.y0_doubleSpinBox.value())):
            self.SolutionsWidget.refresh()
            self.ErrorsWidget.refresh()
            self.RangeErrorsWidget.refresh()
        else:
            self.X_doubleSpinBox.setValue(model.dt.main_grid.x_end)
            self.N_spinBox.setValue(model.dt.main_grid.step_num)
            self.x0_doubleSpinBox.setValue(model.dt.main_grid.x_start)
            self.y0_doubleSpinBox.setValue(model.dt.main_grid.y_start)

    def change_point_marker(self):
        model.dt.show_dots = self.show_dots_checkBox.isChecked()
        self.SolutionsWidget.refresh()
        self.ErrorsWidget.refresh()
        self.RangeErrorsWidget.refresh()


class SolutionsWidget(MplWidget):
    def refresh(self):
        grids = [(model.dt.exact_sol.get_grid(), 'Analytical solution'),
                 (model.dt.euler_met.get_grid(), 'Euler method'),
                 (model.dt.imp_euler_met.get_grid(), 'Improved Euler method'),
                 (model.dt.runge_kutta_met.get_grid(), 'Runge-Kutta method')]
        params = [model.dt.show_exact, model.dt.show_euler, model.dt.show_imp_euler, model.dt.show_runge_kutta]
        self._update_values(grids, params)


class ErrorsWidget(MplWidget):
    def refresh(self):
        grids = [(model.dt.euler_err.get_grid(), 'Euler method'),
                 (model.dt.imp_euler_err.get_grid(), 'Improved Euler method'),
                 (model.dt.runge_kutta_err.get_grid(), 'Runge-Kutta method')]
        params = [model.dt.show_euler, model.dt.show_imp_euler, model.dt.show_runge_kutta]
        self._update_values(grids, params)


class RangeErrorsWidget(MplWidget):
    def refresh(self):
        grids = [(model.dt.euler_rng_err.get_grid(), 'Euler method'),
                 (model.dt.imp_euler_rng_err.get_grid(), 'Improved Euler method'),
                 (model.dt.runge_kutta_rng_err.get_grid(), 'Runge-Kutta method')]
        params = [model.dt.show_euler, model.dt.show_imp_euler, model.dt.show_runge_kutta]
        self._update_values(grids, params)


def launch_gui():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
