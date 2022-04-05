# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalSplitter = QtWidgets.QSplitter(self.centralwidget)
        self.verticalSplitter.setOrientation(QtCore.Qt.Vertical)
        self.verticalSplitter.setObjectName("verticalSplitter")
        self.horizontalSplitter = QtWidgets.QSplitter(self.verticalSplitter)
        self.horizontalSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSplitter.setObjectName("horizontalSplitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.horizontalSplitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.imageViewLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imageViewLayout.setContentsMargins(0, 0, 0, 0)
        self.imageViewLayout.setObjectName("imageViewLayout")
        self.imageViewLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageViewLabel.setObjectName("imageViewLabel")
        self.imageViewLayout.addWidget(self.imageViewLabel)
        self.imageView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.imageView.setObjectName("imageView")
        self.imageViewLayout.addWidget(self.imageView)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.horizontalSplitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layerListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layerListLayout.setContentsMargins(0, 0, 0, 0)
        self.layerListLayout.setObjectName("layerListLayout")
        self.layerListLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.layerListLabel.setObjectName("layerListLabel")
        self.layerListLayout.addWidget(self.layerListLabel)
        self.layersList = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.layersList.setSelectionRectVisible(False)
        self.layersList.setObjectName("layersList")
        self.layerListLayout.addWidget(self.layersList)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.verticalSplitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.logLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.logLayout.setContentsMargins(0, 0, 0, 0)
        self.logLayout.setObjectName("logLayout")
        self.logLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.logLabel.setObjectName("logLabel")
        self.logLayout.addWidget(self.logLabel)
        self.log = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.logLayout.addWidget(self.log)
        self.gridLayout.addWidget(self.verticalSplitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.openFile = QtWidgets.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.menu.addAction(self.openFile)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Barcode Recognizer"))
        self.imageViewLabel.setText(_translate("MainWindow", "Изображение"))
        self.layerListLabel.setText(_translate("MainWindow", "Слои"))
        self.logLabel.setText(_translate("MainWindow", "Сообщения"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.openFile.setText(_translate("MainWindow", "Открыть..."))
        self.openFile.setShortcut(_translate("MainWindow", "Ctrl+O"))


