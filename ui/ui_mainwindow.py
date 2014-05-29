# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created: Sat May 24 23:02:45 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(763, 711)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter_1 = QtGui.QSplitter(self.splitter_2)
        self.splitter_1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_1.setObjectName(_fromUtf8("splitter_1"))
        self.graphicsView = QtGui.QGraphicsView(self.splitter_1)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.layoutWidget = QtGui.QWidget(self.splitter_1)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonLoad = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonLoad.setObjectName(_fromUtf8("pushButtonLoad"))
        self.verticalLayout.addWidget(self.pushButtonLoad)
        self.comboBoxLang = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxLang.setObjectName(_fromUtf8("comboBoxLang"))
        self.verticalLayout.addWidget(self.comboBoxLang)
        self.comboBoxPSM = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxPSM.setObjectName(_fromUtf8("comboBoxPSM"))
        self.verticalLayout.addWidget(self.comboBoxPSM)
        self.comboBoxRIL = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxRIL.setObjectName(_fromUtf8("comboBoxRIL"))
        self.verticalLayout.addWidget(self.comboBoxRIL)
        self.pushButtonShow = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonShow.setObjectName(_fromUtf8("pushButtonShow"))
        self.verticalLayout.addWidget(self.pushButtonShow)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonRestart = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonRestart.setObjectName(_fromUtf8("pushButtonRestart"))
        self.verticalLayout.addWidget(self.pushButtonRestart)
        self.pushButtonQuit = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonQuit.setObjectName(_fromUtf8("pushButtonQuit"))
        self.verticalLayout.addWidget(self.pushButtonQuit)
        self.textEdit = QtGui.QTextEdit(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBarZoom = QtGui.QToolBar(MainWindow)
        self.toolBarZoom.setObjectName(_fromUtf8("toolBarZoom"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarZoom)
        self.actionZoomFit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/zoom_fit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomFit.setIcon(icon)
        self.actionZoomFit.setObjectName(_fromUtf8("actionZoomFit"))
        self.actionZoomTo1 = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/zoom_1 to_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomTo1.setIcon(icon1)
        self.actionZoomTo1.setObjectName(_fromUtf8("actionZoomTo1"))
        self.actionZoomIn = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/zoom_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon2)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/zoom_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon3)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.toolBarZoom.addAction(self.actionZoomFit)
        self.toolBarZoom.addAction(self.actionZoomTo1)
        self.toolBarZoom.addAction(self.actionZoomIn)
        self.toolBarZoom.addAction(self.actionZoomOut)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButtonQuit, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButtonLoad.setText(_translate("MainWindow", "Load Image", None))
        self.pushButtonShow.setText(_translate("MainWindow", "Analyze", None))
        self.pushButtonRestart.setText(_translate("MainWindow", "Restart program", None))
        self.pushButtonQuit.setText(_translate("MainWindow", "Quit", None))
        self.toolBarZoom.setWindowTitle(_translate("MainWindow", "zoomBar", None))
        self.actionZoomFit.setText(_translate("MainWindow", "Fit image to window", None))
        self.actionZoomFit.setToolTip(_translate("MainWindow", "Fit Image to scene", None))
        self.actionZoomTo1.setText(_translate("MainWindow", "1:1", None))
        self.actionZoomTo1.setToolTip(_translate("MainWindow", "Show image without zoom", None))
        self.actionZoomIn.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoomOut.setText(_translate("MainWindow", "Zoom Out", None))

import resources_rc
