# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
from QtViewImage import QtImageViewer

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QPainterPath
from PyQt5.QtCore import QRectF, Qt

import os.path

class Ui_MainWindow(object):
    controller = None

    def setupUi(self, MainWindow):
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(978, 715)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.verticalSplitter = QtWidgets.QSplitter(self.centralwidget)
        # self.verticalSplitter.setOrientation(QtCore.Qt.Vertical)
        # self.verticalSplitter.setObjectName("verticalSplitter")
        # self.horizontalSplitter = QtWidgets.QSplitter(self.verticalSplitter)
        # self.horizontalSplitter.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSplitter.setObjectName("horizontalSplitter")
        # self.verticalLayoutWidget = QtWidgets.QWidget(self.horizontalSplitter)
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.imageViewLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        # self.imageViewLayout.setContentsMargins(0, 0, 0, 0)
        # self.imageViewLayout.setObjectName("imageViewLayout")
        # self.imageViewLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.imageViewLabel.setObjectName("imageViewLabel")
        # self.imageViewLayout.addWidget(self.imageViewLabel)
        # self.imageView = QtImageViewer(self.verticalLayoutWidget)
        # self.imageView.setObjectName("imageView")
        # self.imageViewLayout.addWidget(self.imageView)
        # self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.horizontalSplitter)
        # self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        # self.layerListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.layerListLayout.setContentsMargins(0, 0, 0, 0)
        # self.layerListLayout.setObjectName("layerListLayout")
        # self.toolBox = QtWidgets.QToolBox(self.verticalLayoutWidget_2)
        # self.toolBox.setObjectName("toolBox")
        # self.page = QtWidgets.QWidget()
        # self.page.setGeometry(QtCore.QRect(0, 0, 473, 307))
        # self.page.setObjectName("page")
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.layersList = QtWidgets.QListWidget(self.page)
        # self.layersList.setSelectionRectVisible(False)
        # self.layersList.setObjectName("layersList")
        # self.verticalLayout.addWidget(self.layersList)
        # self.toolBox.addItem(self.page, "Слои")
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setGeometry(QtCore.QRect(0, 0, 473, 307))
        # self.page_2.setObjectName("page_2")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.histogram = QtWidgets.QGraphicsView(self.page_2)
        # self.histogram.setObjectName("histogram")
        # self.verticalLayout_2.addWidget(self.histogram)
        # self.toolBox.addItem(self.page_2, "Гистограмма")
        # self.layerListLayout.addWidget(self.toolBox)
        # self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.verticalSplitter)
        # self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        # self.logLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        # self.logLayout.setContentsMargins(0, 0, 0, 0)
        # self.logLayout.setObjectName("logLayout")
        # self.logLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # self.logLabel.setObjectName("logLabel")
        # self.logLayout.addWidget(self.logLabel)
        # self.log = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        # self.log.setSizePolicy(sizePolicy)
        # self.log.setReadOnly(True)
        # self.log.setObjectName("log")
        # self.logLayout.addWidget(self.log)
        # self.horizontalLayout_2.addWidget(self.verticalSplitter)
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        # self.menubar.setObjectName("menubar")
        # self.menu = QtWidgets.QMenu(self.menubar)
        # self.menu.setObjectName("menu")
        # MainWindow.setMenuBar(self.menubar)
        # self.openFile = QtWidgets.QAction(MainWindow)
        # self.openFile.setObjectName("openFile")
        # self.menu.addAction(self.openFile)
        # self.menubar.addAction(self.menu.menuAction())

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.imageView = QtImageViewer(self.verticalLayoutWidget)
        self.imageView.setObjectName("imageView")
        self.imageViewLayout.addWidget(self.imageView)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.horizontalSplitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layerListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layerListLayout.setContentsMargins(0, 0, 0, 0)
        self.layerListLayout.setObjectName("layerListLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget.setObjectName("tabWidget")
        self.layersTab = QtWidgets.QWidget()
        self.layersTab.setObjectName("layersTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layersTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layersList = QtWidgets.QListWidget(self.layersTab)
        self.layersList.setSelectionRectVisible(False)
        self.layersList.setObjectName("layersList")
        self.verticalLayout.addWidget(self.layersList)
        self.tabWidget.addTab(self.layersTab, "")
        self.histogramTab = QtWidgets.QWidget()
        self.histogramTab.setObjectName("histogramTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.histogramTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.histogram = QtWidgets.QGraphicsView(self.histogramTab)
        self.histogram.setObjectName("histogram")
        self.verticalLayout_2.addWidget(self.histogram)
        self.tabWidget.addTab(self.histogramTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settingsTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.barcodeOrientationGroupBox = QtWidgets.QGroupBox(self.settingsTab)
        self.barcodeOrientationGroupBox.setObjectName("barcodeGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.barcodeOrientationGroupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.barcodeOrientationAuto = QtWidgets.QRadioButton(self.barcodeOrientationGroupBox)
        self.barcodeOrientationAuto.setObjectName("barcodeOrientationAuto")
        self.verticalLayout_6.addWidget(self.barcodeOrientationAuto)
        self.barcodeOrientationHorizontal = QtWidgets.QRadioButton(self.barcodeOrientationGroupBox)
        self.barcodeOrientationHorizontal.setObjectName("barcodeOrientationHorizontal")
        self.verticalLayout_6.addWidget(self.barcodeOrientationHorizontal)
        self.barcodeOrientationVertical = QtWidgets.QRadioButton(self.barcodeOrientationGroupBox)
        self.barcodeOrientationVertical.setObjectName("barcodeOrientationVertical")
        self.verticalLayout_6.addWidget(self.barcodeOrientationVertical)
        self.verticalLayout_4.addWidget(self.barcodeOrientationGroupBox)
        self.blockSizeGroupBox = QtWidgets.QGroupBox(self.settingsTab)
        self.blockSizeGroupBox.setObjectName("blockSizeGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.blockSizeGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider = QtWidgets.QSlider(self.blockSizeGroupBox)
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(75)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setPageStep(15)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(True)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_5.addWidget(self.horizontalSlider)
        self.verticalLayout_4.addWidget(self.blockSizeGroupBox)
        self.calculateButton = QtWidgets.QPushButton(self.settingsTab)
        self.calculateButton.setObjectName("calculateButton")
        self.verticalLayout_4.addWidget(self.calculateButton)
        self.tabWidget.addTab(self.settingsTab, "")
        self.layerListLayout.addWidget(self.tabWidget)
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
        self.verticalLayout_3.addWidget(self.verticalSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.openFile = QtWidgets.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.menu.addAction(self.openFile)
        self.menubar.addAction(self.menu.menuAction())

        MainWindow.setWindowTitle("Barcode Recognizer")
        self.menu.setTitle("Файл")
        self.openFile.setText("Открыть...")
        self.openFile.setShortcut("Ctrl+O")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.imageViewLabel.setText("Изображение")
        self.logLabel.setText("Сообщения")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.layersTab), "Слои")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogramTab), "Гистограмма")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), "Настройки")
        self.tabWidget.setCurrentWidget(self.settingsTab)

        self.barcodeOrientationAuto.setText("Авто (квадратные блоки)")
        self.barcodeOrientationHorizontal.setText("Горизонтальный")
        self.barcodeOrientationVertical.setText("Вертикальный")
        self.barcodeOrientationHorizontal.setChecked(True)

        self.blockSizeGroupBox.setTitle("Размер блока")
        self.calculateButton.setText("Вычислить")

        self.barcodeOrientationGroupBox.setTitle("Ориентация штрихкода")

        self.layersList.itemChanged.connect(self.on_layer_list_item_change)
        self.openFile.triggered.connect(self.open_file)
        self.calculateButton.clicked.connect(self.calculate)

        self.verticalSplitter.setSizes([5000, 1000])
        self.horizontalSplitter.setSizes([5000, 1000])

        self.controller.set_logger(self.logger)

    def logger(self, message):
        self.log.appendPlainText(message)
        self.log.repaint()

    def on_layer_list_item_change(self, layerListItem):
        blockLayer = self.blockLayers[layerListItem.text()]
        checkState = layerListItem.checkState()
        if checkState == QtCore.Qt.Unchecked:
            blockLayer.hide()
        else:
            blockLayer.show()

    def clearScene(self):
        if self.blockLayers == None:
            return
        for blockLayerName, blockLayer in self.blockLayers.items():
            for primitive in blockLayer.primitives:
                self.imageView.scene.removeItem(primitive)
        self.blockLayers = None

    def open_file(self):
        fileName, dummy = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open image file.")
        if len(fileName) and os.path.isfile(fileName):
            self.blockLayers = None
            self.imageView.clearImage()
            self.imageView.scene.clear()

            image = QImage(fileName)
            self.imageView.filename = fileName
            self.imageView.setImage(image)
            self.controller.set_image(fileName)

    def calculate(self):
        if self.controller.isImageSet() == False:
            return
        self.clearScene()
        orientation = "auto"
        if self.barcodeOrientationHorizontal.isChecked():
            orientation = "horizontal"
        elif self.barcodeOrientationVertical.isChecked():
            orientation = "vertical"

        self.controller.barcodeFinder.set_settings(self.horizontalSlider.value(), orientation)
        self.controller.calculate()
        self.blockLayers = self.controller.draw_layers(self.imageView.scene)



        # Заполняем список слоев
        self.layersList.clear()
        for blockLayerName, blockLayer in sorted(self.blockLayers.items()):
            item = QtWidgets.QListWidgetItem(blockLayerName)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if blockLayer.isVisible:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            self.layersList.addItem(item)

        # Рисуем гистограмму
        histogramScene = QtWidgets.QGraphicsScene()
        self.histogramDraw = self.controller.draw_histogram(histogramScene)
        self.histogram.setSceneRect(QRectF(0, 0, self.histogramDraw.h_width, self.histogramDraw.h_height))
        self.histogram.setScene(histogramScene)
        self.histogram.fitInView(self.histogram.sceneRect(),
                                 Qt.KeepAspectRatio)



