from PyQt5 import QtCore, QtGui, QtWidgets

import view


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 804)
        MainWindow.setToolTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setWindowFilePath("")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 310, 104, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.err_gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.err_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.err_gridLayout.setObjectName("err_gridLayout")
        self.n0_err_label = QtWidgets.QLabel(self.layoutWidget)
        self.n0_err_label.setObjectName("n0_err_label")
        self.err_gridLayout.addWidget(self.n0_err_label, 0, 0, 1, 1)
        self.N_err_label = QtWidgets.QLabel(self.layoutWidget)
        self.N_err_label.setObjectName("N_err_label")
        self.err_gridLayout.addWidget(self.N_err_label, 1, 0, 1, 1)
        self.n0_err_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.n0_err_spinBox.setMinimum(1)
        self.n0_err_spinBox.setMaximum(10000)
        self.n0_err_spinBox.setSingleStep(1)
        self.n0_err_spinBox.setProperty("value", 5)
        self.n0_err_spinBox.setObjectName("n0_err_spinBox")
        self.err_gridLayout.addWidget(self.n0_err_spinBox, 0, 1, 1, 1)
        self.N_err_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.N_err_spinBox.setMinimum(2)
        self.N_err_spinBox.setMaximum(10000)
        self.N_err_spinBox.setSingleStep(1)
        self.N_err_spinBox.setProperty("value", 30)
        self.N_err_spinBox.setObjectName("N_err_spinBox")
        self.err_gridLayout.addWidget(self.N_err_spinBox, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 400, 581, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.err_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.err_verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.err_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.err_verticalLayout.setObjectName("err_verticalLayout")
        self.err_label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.err_label.sizePolicy().hasHeightForWidth())
        self.err_label.setSizePolicy(sizePolicy)
        self.err_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.err_label.setFont(font)
        self.err_label.setObjectName("err_label")
        self.err_verticalLayout.addWidget(self.err_label)
        self.ErrorsWidget = view.ErrorsWidget(self.layoutWidget1)
        self.ErrorsWidget.setMinimumSize(QtCore.QSize(450, 300))
        self.ErrorsWidget.setObjectName("ErrorsWidget")
        self.err_verticalLayout.addWidget(self.ErrorsWidget)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(630, 400, 581, 381))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.rng_err_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.rng_err_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rng_err_verticalLayout.setObjectName("rng_err_verticalLayout")
        self.rng_err_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rng_err_label.sizePolicy().hasHeightForWidth())
        self.rng_err_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rng_err_label.setFont(font)
        self.rng_err_label.setObjectName("rng_err_label")
        self.rng_err_verticalLayout.addWidget(self.rng_err_label)
        self.RangeErrorsWidget = view.RangeErrorsWidget(self.layoutWidget2)
        self.RangeErrorsWidget.setMinimumSize(QtCore.QSize(450, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RangeErrorsWidget.setFont(font)
        self.RangeErrorsWidget.setObjectName("RangeErrorsWidget")
        self.rng_err_verticalLayout.addWidget(self.RangeErrorsWidget)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 0, 581, 381))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.sol_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.sol_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sol_verticalLayout.setObjectName("sol_verticalLayout")
        self.sol_label = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sol_label.sizePolicy().hasHeightForWidth())
        self.sol_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sol_label.setFont(font)
        self.sol_label.setObjectName("sol_label")
        self.sol_verticalLayout.addWidget(self.sol_label)
        self.SolutionsWidget = view.SolutionsWidget(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SolutionsWidget.sizePolicy().hasHeightForWidth())
        self.SolutionsWidget.setSizePolicy(sizePolicy)
        self.SolutionsWidget.setMinimumSize(QtCore.QSize(450, 300))
        self.SolutionsWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SolutionsWidget.setAutoFillBackground(False)
        self.SolutionsWidget.setObjectName("SolutionsWidget")
        self.sol_verticalLayout.addWidget(self.SolutionsWidget)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(630, 20, 340, 190))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.sol_horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.sol_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sol_horizontalLayout.setObjectName("sol_horizontalLayout")
        self.sol_gridLayout = QtWidgets.QGridLayout()
        self.sol_gridLayout.setObjectName("sol_gridLayout")
        self.x0_label = QtWidgets.QLabel(self.layoutWidget4)
        self.x0_label.setObjectName("x0_label")
        self.sol_gridLayout.addWidget(self.x0_label, 2, 0, 1, 1)
        self.x0_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.x0_doubleSpinBox.setDecimals(6)
        self.x0_doubleSpinBox.setMinimum(-10000.0)
        self.x0_doubleSpinBox.setMaximum(10000.0)
        self.x0_doubleSpinBox.setSingleStep(0.5)
        self.x0_doubleSpinBox.setProperty("value", 2.0)
        self.x0_doubleSpinBox.setObjectName("x0_doubleSpinBox")
        self.sol_gridLayout.addWidget(self.x0_doubleSpinBox, 2, 1, 1, 1)
        self.y0_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.y0_doubleSpinBox.setDecimals(6)
        self.y0_doubleSpinBox.setMinimum(-10000.0)
        self.y0_doubleSpinBox.setMaximum(10000.0)
        self.y0_doubleSpinBox.setSingleStep(0.5)
        self.y0_doubleSpinBox.setProperty("value", 1.0)
        self.y0_doubleSpinBox.setObjectName("y0_doubleSpinBox")
        self.sol_gridLayout.addWidget(self.y0_doubleSpinBox, 3, 1, 1, 1)
        self.N_label = QtWidgets.QLabel(self.layoutWidget4)
        self.N_label.setObjectName("N_label")
        self.sol_gridLayout.addWidget(self.N_label, 0, 0, 1, 1)
        self.X_label = QtWidgets.QLabel(self.layoutWidget4)
        self.X_label.setObjectName("X_label")
        self.sol_gridLayout.addWidget(self.X_label, 1, 0, 1, 1)
        self.y0_label = QtWidgets.QLabel(self.layoutWidget4)
        self.y0_label.setObjectName("y0_label")
        self.sol_gridLayout.addWidget(self.y0_label, 3, 0, 1, 1)
        self.N_spinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.N_spinBox.setMinimum(2)
        self.N_spinBox.setMaximum(10000)
        self.N_spinBox.setProperty("value", 10)
        self.N_spinBox.setObjectName("N_spinBox")
        self.sol_gridLayout.addWidget(self.N_spinBox, 0, 1, 1, 1)
        self.X_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.X_doubleSpinBox.setDecimals(6)
        self.X_doubleSpinBox.setMinimum(-10000.0)
        self.X_doubleSpinBox.setMinimum(-10000.0)
        self.X_doubleSpinBox.setMinimum(-10000.0)
        self.X_doubleSpinBox.setMaximum(10000.0)
        self.X_doubleSpinBox.setSingleStep(0.5)
        self.X_doubleSpinBox.setProperty("value", 10.0)
        self.X_doubleSpinBox.setObjectName("X_doubleSpinBox")
        self.sol_gridLayout.addWidget(self.X_doubleSpinBox, 1, 1, 1, 1)
        self.sol_horizontalLayout.addLayout(self.sol_gridLayout)
        self.checkBox_verticalLayout = QtWidgets.QVBoxLayout()
        self.checkBox_verticalLayout.setObjectName("checkBox_verticalLayout")
        self.exact_sol_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.exact_sol_checkBox.setEnabled(True)
        self.exact_sol_checkBox.setChecked(True)
        self.exact_sol_checkBox.setObjectName("exact_sol_checkBox")
        self.checkBox_verticalLayout.addWidget(self.exact_sol_checkBox)
        self.euler_met_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.euler_met_checkBox.setEnabled(True)
        self.euler_met_checkBox.setChecked(True)
        self.euler_met_checkBox.setObjectName("euler_met_checkBox")
        self.checkBox_verticalLayout.addWidget(self.euler_met_checkBox)
        self.imp_euler_met_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.imp_euler_met_checkBox.setChecked(True)
        self.imp_euler_met_checkBox.setObjectName("imp_euler_met_checkBox")
        self.checkBox_verticalLayout.addWidget(self.imp_euler_met_checkBox)
        self.rungekutta_met_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.rungekutta_met_checkBox.setChecked(True)
        self.rungekutta_met_checkBox.setObjectName("rungekutta_met_checkBox")
        self.checkBox_verticalLayout.addWidget(self.rungekutta_met_checkBox)
        self.show_dots_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.show_dots_checkBox.setEnabled(True)
        self.show_dots_checkBox.setChecked(True)
        self.show_dots_checkBox.setObjectName("show_dots_checkBox ")
        self.checkBox_verticalLayout.addWidget(self.show_dots_checkBox)
        self.sol_horizontalLayout.addLayout(self.checkBox_verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computational Practicum"))
        self.n0_err_label.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">n</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\">:</span></p></body></html>"))
        self.N_err_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N:</span></p></body></html>"))
        self.err_label.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Error of numerical methods:</span></p></body></html>"))
        self.rng_err_label.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Error in range from n</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\"> to N:</span></p></body></html>"))
        self.sol_label.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Plot of solutions for equation y` = 3y ^ (2/3):</span></p></body></html>"))
        self.x0_label.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">x</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\">:</span></p></body></html>"))
        self.N_label.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N:</span></p></body></html>"))
        self.X_label.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">X:</span></p></body></html>"))
        self.y0_label.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">y</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\">:</span></p></body></html>"))
        self.exact_sol_checkBox.setText(_translate("MainWindow", "Analytical Solution"))
        self.euler_met_checkBox.setText(_translate("MainWindow", "Euler method"))
        self.imp_euler_met_checkBox.setText(_translate("MainWindow", "Improved Euler method"))
        self.rungekutta_met_checkBox.setText(_translate("MainWindow", "RungeKutta Method"))
        self.show_dots_checkBox.setText(_translate("MainWindow", "Show point markers"))
