# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_plot.ui'
#
# Created: Tue Sep  1 23:02:36 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 718)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plotHBar = QtGui.QScrollBar(self.centralwidget)
        self.plotHBar.setOrientation(QtCore.Qt.Horizontal)
        self.plotHBar.setObjectName("plotHBar")
        self.gridLayout.addWidget(self.plotHBar, 1, 0, 1, 3)
        self.filePosBox = QtGui.QGroupBox(self.centralwidget)
        self.filePosBox.setMinimumSize(QtCore.QSize(0, 120))
        self.filePosBox.setObjectName("filePosBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.filePosBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.filePosLayout = QtGui.QFormLayout()
        self.filePosLayout.setObjectName("filePosLayout")
        self.filePosStartLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.filePosStartLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.filePosStartLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.filePosStartLineEdit.setObjectName("filePosStartLineEdit")
        self.filePosLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.filePosStartLineEdit)
        self.filePosStopLabel = QtGui.QLabel(self.filePosBox)
        self.filePosStopLabel.setObjectName("filePosStopLabel")
        self.filePosLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.filePosStopLabel)
        self.filePosStopLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.filePosStopLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.filePosStopLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.filePosStopLineEdit.setObjectName("filePosStopLineEdit")
        self.filePosLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.filePosStopLineEdit)
        self.filePosLengthLabel = QtGui.QLabel(self.filePosBox)
        self.filePosLengthLabel.setObjectName("filePosLengthLabel")
        self.filePosLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.filePosLengthLabel)
        self.filePosLengthLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.filePosLengthLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.filePosLengthLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.filePosLengthLineEdit.setObjectName("filePosLengthLineEdit")
        self.filePosLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.filePosLengthLineEdit)
        self.filePosStartLabel = QtGui.QLabel(self.filePosBox)
        self.filePosStartLabel.setObjectName("filePosStartLabel")
        self.filePosLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.filePosStartLabel)
        self.gridLayout_4.addLayout(self.filePosLayout, 0, 0, 1, 1)
        self.fileTimeLayout = QtGui.QFormLayout()
        self.fileTimeLayout.setObjectName("fileTimeLayout")
        self.fileTimeStartLabel = QtGui.QLabel(self.filePosBox)
        self.fileTimeStartLabel.setObjectName("fileTimeStartLabel")
        self.fileTimeLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.fileTimeStartLabel)
        self.fileTimeStartLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.fileTimeStartLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.fileTimeStartLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fileTimeStartLineEdit.setObjectName("fileTimeStartLineEdit")
        self.fileTimeLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.fileTimeStartLineEdit)
        self.fileTimeStopLabel = QtGui.QLabel(self.filePosBox)
        self.fileTimeStopLabel.setObjectName("fileTimeStopLabel")
        self.fileTimeLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.fileTimeStopLabel)
        self.fileTimeStopLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.fileTimeStopLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.fileTimeStopLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fileTimeStopLineEdit.setObjectName("fileTimeStopLineEdit")
        self.fileTimeLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fileTimeStopLineEdit)
        self.fileTimeLengthLabel = QtGui.QLabel(self.filePosBox)
        self.fileTimeLengthLabel.setObjectName("fileTimeLengthLabel")
        self.fileTimeLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.fileTimeLengthLabel)
        self.fileTimeLengthLineEdit = QtGui.QLineEdit(self.filePosBox)
        self.fileTimeLengthLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.fileTimeLengthLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fileTimeLengthLineEdit.setObjectName("fileTimeLengthLineEdit")
        self.fileTimeLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fileTimeLengthLineEdit)
        self.gridLayout_4.addLayout(self.fileTimeLayout, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.filePosBox, 2, 0, 1, 1)
        self.displayGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.displayGroupBox.setMinimumSize(QtCore.QSize(170, 0))
        self.displayGroupBox.setObjectName("displayGroupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.displayGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.colorComboBox = QtGui.QComboBox(self.displayGroupBox)
        self.colorComboBox.setObjectName("colorComboBox")
        self.gridLayout_2.addWidget(self.colorComboBox, 0, 0, 1, 2)
        self.lineWidthSpinBox = QtGui.QSpinBox(self.displayGroupBox)
        self.lineWidthSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.lineWidthSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineWidthSpinBox.setObjectName("lineWidthSpinBox")
        self.gridLayout_2.addWidget(self.lineWidthSpinBox, 1, 1, 1, 1)
        self.lineWidthLabel = QtGui.QLabel(self.displayGroupBox)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.gridLayout_2.addWidget(self.lineWidthLabel, 1, 0, 1, 1)
        self.lineStyleLabel = QtGui.QLabel(self.displayGroupBox)
        self.lineStyleLabel.setObjectName("lineStyleLabel")
        self.gridLayout_2.addWidget(self.lineStyleLabel, 2, 0, 1, 1)
        self.lineStyleComboBox = QtGui.QComboBox(self.displayGroupBox)
        self.lineStyleComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.lineStyleComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineStyleComboBox.setObjectName("lineStyleComboBox")
        self.gridLayout_2.addWidget(self.lineStyleComboBox, 2, 1, 1, 1)
        self.styleSizeLabel = QtGui.QLabel(self.displayGroupBox)
        self.styleSizeLabel.setObjectName("styleSizeLabel")
        self.gridLayout_2.addWidget(self.styleSizeLabel, 3, 0, 1, 1)
        self.styleSizeSpinBox = QtGui.QSpinBox(self.displayGroupBox)
        self.styleSizeSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.styleSizeSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.styleSizeSpinBox.setObjectName("styleSizeSpinBox")
        self.gridLayout_2.addWidget(self.styleSizeSpinBox, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.displayGroupBox, 2, 2, 1, 1)
        self.sysGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.sysGroupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.sysGroupBox.setObjectName("sysGroupBox")
        self.formLayout = QtGui.QFormLayout(self.sysGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.sampleRateLabel = QtGui.QLabel(self.sysGroupBox)
        self.sampleRateLabel.setObjectName("sampleRateLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.sampleRateLabel)
        self.sampleRateLineEdit = QtGui.QLineEdit(self.sysGroupBox)
        self.sampleRateLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.sampleRateLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sampleRateLineEdit.setObjectName("sampleRateLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sampleRateLineEdit)
        self.gridLayout.addWidget(self.sysGroupBox, 2, 1, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabGroup = QtGui.QTabWidget(self.frame)
        self.tabGroup.setMinimumSize(QtCore.QSize(0, 0))
        self.tabGroup.setObjectName("tabGroup")
        self.timeTab = QtGui.QWidget()
        self.timeTab.setObjectName("timeTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.timeTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timePlot = Qwt5.QwtPlot(self.timeTab)
        self.timePlot.setObjectName("timePlot")
        self.horizontalLayout.addWidget(self.timePlot)
        self.tabGroup.addTab(self.timeTab, "")
        self.freqTab = QtGui.QWidget()
        self.freqTab.setObjectName("freqTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.freqTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fftPropBox = QtGui.QGroupBox(self.freqTab)
        self.fftPropBox.setMinimumSize(QtCore.QSize(160, 0))
        self.fftPropBox.setObjectName("fftPropBox")
        self.formLayout_4 = QtGui.QFormLayout(self.fftPropBox)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.psdFFTSizeLabel = QtGui.QLabel(self.fftPropBox)
        self.psdFFTSizeLabel.setObjectName("psdFFTSizeLabel")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.psdFFTSizeLabel)
        self.psdFFTComboBox = QtGui.QComboBox(self.fftPropBox)
        self.psdFFTComboBox.setMinimumSize(QtCore.QSize(96, 0))
        self.psdFFTComboBox.setMaximumSize(QtCore.QSize(96, 16777215))
        self.psdFFTComboBox.setObjectName("psdFFTComboBox")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.psdFFTComboBox)
        self.horizontalLayout_2.addWidget(self.fftPropBox)
        self.freqPlot = Qwt5.QwtPlot(self.freqTab)
        self.freqPlot.setObjectName("freqPlot")
        self.horizontalLayout_2.addWidget(self.freqPlot)
        self.tabGroup.addTab(self.freqTab, "")
        self.specTab = QtGui.QWidget()
        self.specTab.setObjectName("specTab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.specTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.specTab)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.specFFTLabel = QtGui.QLabel(self.groupBox)
        self.specFFTLabel.setObjectName("specFFTLabel")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.specFFTLabel)
        self.specFFTComboBox = QtGui.QComboBox(self.groupBox)
        self.specFFTComboBox.setMinimumSize(QtCore.QSize(96, 0))
        self.specFFTComboBox.setMaximumSize(QtCore.QSize(96, 16777215))
        self.specFFTComboBox.setObjectName("specFFTComboBox")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.specFFTComboBox)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.specPlot = Qwt5.QwtPlot(self.specTab)
        self.specPlot.setObjectName("specPlot")
        self.horizontalLayout_3.addWidget(self.specPlot)
        self.tabGroup.addTab(self.specTab, "")
        self.gridLayout_3.addWidget(self.tabGroup, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 927, 24))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_reload = QtGui.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")
        self.menu_File.addAction(self.action_open)
        self.menu_File.addAction(self.action_reload)
        self.menu_File.addAction(self.action_exit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tabGroup.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.filePosBox.setTitle(QtGui.QApplication.translate("MainWindow", "File Position", None, QtGui.QApplication.UnicodeUTF8))
        self.filePosStopLabel.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.filePosLengthLabel.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.filePosStartLabel.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTimeStartLabel.setText(QtGui.QApplication.translate("MainWindow", "time start (sec)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTimeStopLabel.setText(QtGui.QApplication.translate("MainWindow", "time stop (sec)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTimeLengthLabel.setText(QtGui.QApplication.translate("MainWindow", "time length (sec)", None, QtGui.QApplication.UnicodeUTF8))
        self.displayGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Display Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.lineWidthLabel.setText(QtGui.QApplication.translate("MainWindow", "Line Width", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyleLabel.setText(QtGui.QApplication.translate("MainWindow", "Line Style", None, QtGui.QApplication.UnicodeUTF8))
        self.styleSizeLabel.setText(QtGui.QApplication.translate("MainWindow", "Style Size", None, QtGui.QApplication.UnicodeUTF8))
        self.sysGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "System Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.sampleRateLabel.setText(QtGui.QApplication.translate("MainWindow", "Sample Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.timeTab), QtGui.QApplication.translate("MainWindow", "Time Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.fftPropBox.setTitle(QtGui.QApplication.translate("MainWindow", "FFT Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.psdFFTSizeLabel.setText(QtGui.QApplication.translate("MainWindow", "FFT Size", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.freqTab), QtGui.QApplication.translate("MainWindow", "Frequency Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Spectrogram Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.specFFTLabel.setText(QtGui.QApplication.translate("MainWindow", "FFT Size", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.specTab), QtGui.QApplication.translate("MainWindow", "Spectrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setText(QtGui.QApplication.translate("MainWindow", "&Reload", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qwt5