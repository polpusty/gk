# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gk_ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

import sys

from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtWidgets, QtGui

from matplotlib import pyplot as plt

from bitmap import Bitmap8BitGrey


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 716)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1081, 631))
        self.label.setObjectName("label")
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidget(self.label)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 1081, 631))
        MainWindow.setCentralWidget(self.centralWidget)
        self.markArea = QtWidgets.QPushButton(self.centralWidget)
        self.markArea.setGeometry(QtCore.QRect(10, 650, 80, 22))
        self.markArea.setObjectName("markArea")
        self.histogram = QtWidgets.QPushButton(self.centralWidget)
        self.histogram.setGeometry(QtCore.QRect(100, 650, 80, 22))
        self.histogram.setObjectName("histogram")

        self.brightnessSlider = QtWidgets.QSlider(self.centralWidget)
        self.brightnessSlider.setGeometry(QtCore.QRect(190, 650, 160, 16))
        self.brightnessSlider.setMinimum(-255)
        self.brightnessSlider.setMaximum(255)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")

        self.contrastSlider = QtWidgets.QSlider(self.centralWidget)
        self.contrastSlider.setGeometry(QtCore.QRect(370, 650, 160, 16))
        self.contrastSlider.setMinimum(-256)
        self.contrastSlider.setMaximum(256)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")

        self.gammaSlider = QtWidgets.QSlider(self.centralWidget)
        self.gammaSlider.setGeometry(QtCore.QRect(550, 650, 160, 16))
        self.gammaSlider.setMinimum(-256)
        self.gammaSlider.setMaximum(256)
        self.gammaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSlider.setObjectName("gammaSlider")

        self.brightnessText = QtWidgets.QLabel(self.centralWidget)
        self.brightnessText.setGeometry(QtCore.QRect(210, 670, 113, 22))
        self.brightnessText.setObjectName("brightnessText")
        self.brightnessText.setText("Brightness")
        self.contrastText = QtWidgets.QLabel(self.centralWidget)
        self.contrastText.setGeometry(QtCore.QRect(390, 670, 113, 22))
        self.contrastText.setObjectName("contrastText")
        self.contrastText.setText("Contrast")
        self.gammaText = QtWidgets.QLabel(self.centralWidget)
        self.gammaText.setGeometry(QtCore.QRect(580, 670, 113, 22))
        self.gammaText.setObjectName("gammaText")
        self.gammaText.setText("Gamma")

        self.acceptChange = QtWidgets.QPushButton(self.centralWidget)
        self.acceptChange.setGeometry(QtCore.QRect(979, 650, 111, 22))
        self.acceptChange.setObjectName("acceptChange")

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1100, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.markArea.clicked.connect(self.action_mark)
        self.histogram.clicked.connect(self.action_histogram)
        self.acceptChange.clicked.connect(self.action_accept)
        self.brightnessSlider.valueChanged.connect(self.action_brightness)
        self.contrastSlider.valueChanged.connect(self.action_contrast)
        self.gammaSlider.valueChanged.connect(self.action_gamma)

        self.rubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self.centralWidget)
        self.rubberBand.setStyle(QtWidgets.QStyleFactory().create('Windows'))
        self.start_origin = QtCore.QPoint()
        self.end_origin = QtCore.QPoint()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computer Graphics Programming"))

        self.markArea.setText(_translate("MainWindow", "Mark area"))
        self.histogram.setText(_translate("MainWindow", "Histogram"))
        self.acceptChange.setText(_translate("MainWindow", "Accept Changes"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.stateMarkArea = False
        self.lastChangedValue = 0
        self.openFileName = None
        self.saveAsFileName = None
        self.saveAsExtension = None
        self.setup_actions()
        self.setupUi(self)

    def setup_actions(self):
        self.actionOpen = QtWidgets.QAction("Open", self)
        self.actionOpen.triggered.connect(self.action_open)

        self.actionSave = QtWidgets.QAction("Save", self)
        self.actionSave.triggered.connect(self.action_save)

        self.actionSave_As = QtWidgets.QAction("Save as", self)
        self.actionSave_As.triggered.connect(self.action_save_as)

        self.actionExit = QtWidgets.QAction("Exit", self)
        self.actionExit.triggered.connect(self.action_exit)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.openFileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Save as",
                                                                     "", "All Files (*);; BMP Images (*.bmp)",
                                                                     options=options)

    def saveFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.saveAsFileName, self.saveAsExtension = QtWidgets.QFileDialog.getSaveFileName(self, "Save as",
                                                                     "", "BMP Image (.bmp);; PNG Image (.png);; JPG Image (.jpg)",
                                                                     options=options)

    def set_pixmap(self):
        self.bmp_img = ImageQt(self.bmp.to_image())
        pix = QtGui.QPixmap.fromImage(self.bmp_img)
        self.label.resize(pix.size())
        self.label.setPixmap(pix)

    def action_open(self):
        self.openFileNameDialog()
        self.bmp = Bitmap8BitGrey(self.openFileName)
        self.set_pixmap()

    def action_save(self):
        if getattr(self, 'bmp', False):
            self.bmp.save()

    def action_save_as(self):
        if getattr(self, 'bmp', False):
            self.saveFileNameDialog()
            self.bmp.save_as(self.saveAsFileName, self.saveAsExtension)

    def action_exit(self):
        sys.exit()

    def action_mark(self):
        self.stateMarkArea = not self.stateMarkArea
        self.markArea.setStyleSheet("background-color: " + "blue" if self.stateMarkArea else "white")
        if not self.stateMarkArea:
            self.rubberBand.hide()

    def action_histogram(self):
        if getattr(self, 'bmp', False):
            data_histogram = self.bmp.histogram_of_brightness(*self.get_editing_area())
            plt.hist(data_histogram, 256, [0, 256])
            plt.title('Histogram of brightness')
            plt.show()

    def action_accept(self):
        if getattr(self, 'bmp', False):
            self.bmp.accept_change()
            self.brightnessSlider.setValue(0)
            self.contrastSlider.setValue(0)
            self.gammaSlider.setValue(0)

    def action_brightness(self, value):
        if getattr(self, 'bmp', False):
            self.bmp.change_brightness(value, *self.get_editing_area())
            self.set_pixmap()

    def action_contrast(self, value):
        if getattr(self, 'bmp', False):
            self.bmp.change_contrast(value, *self.get_editing_area())
            self.set_pixmap()

    def action_gamma(self, value):
        if getattr(self, 'bmp', False):
            self.bmp.change_gamma(value, *self.get_editing_area())
            self.set_pixmap()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.stateMarkArea:
            pos = event.pos()
            pos.setY(pos.y() - 25)
            self.start_origin = QtCore.QPoint(pos)
            self.rubberBand.setGeometry(QtCore.QRect(self.start_origin, QtCore.QSize()).normalized())
            self.rubberBand.show()

    def mouseMoveEvent(self, event):
        pos = event.pos()
        pos.setY(pos.y() - 25)
        self.end_origin = QtCore.QPoint(pos)
        if not self.start_origin.isNull():
            self.rubberBand.setGeometry(QtCore.QRect(self.start_origin, self.end_origin).normalized())

    def get_editing_area(self):
        positive = lambda x: x if x > 0 else 0
        if self.start_origin and self.end_origin and self.stateMarkArea:
            start_origin_area_x = positive(self.start_origin.x() - 10 + self.scrollArea.horizontalScrollBar().value())
            start_origin_area_y = positive(self.start_origin.y() - 10 + self.scrollArea.verticalScrollBar().value())
            end_origin_area_x = positive(self.end_origin.x() - 10 + self.scrollArea.horizontalScrollBar().value())
            end_origin_area_y = positive(self.end_origin.y() - 10 + self.scrollArea.verticalScrollBar().value())
            point_left_top = (
                min(start_origin_area_x, end_origin_area_x),
                min(start_origin_area_y, end_origin_area_y)
            )
            point_right_bottom = (
                max(start_origin_area_x, end_origin_area_x),
                max(start_origin_area_y, end_origin_area_y)
            )
            return point_left_top, point_right_bottom
        return (0, 0), self.bmp.size
