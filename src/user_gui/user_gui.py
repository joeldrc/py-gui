# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(1100, 600))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.remoteConnectionBox = QtWidgets.QGroupBox(self.mainFrame)
        self.remoteConnectionBox.setGeometry(QtCore.QRect(820, 0, 280, 71))
        self.remoteConnectionBox.setMinimumSize(QtCore.QSize(280, 0))
        self.remoteConnectionBox.setObjectName("remoteConnectionBox")
        self.remoteConnectionLabel = QtWidgets.QLabel(self.remoteConnectionBox)
        self.remoteConnectionLabel.setGeometry(QtCore.QRect(10, 45, 261, 21))
        self.remoteConnectionLabel.setObjectName("remoteConnectionLabel")
        self.instrumentAddress = QtWidgets.QLineEdit(self.remoteConnectionBox)
        self.instrumentAddress.setGeometry(QtCore.QRect(10, 20, 191, 20))
        self.instrumentAddress.setObjectName("instrumentAddress")
        self.connectButton = QtWidgets.QPushButton(self.remoteConnectionBox)
        self.connectButton.setGeometry(QtCore.QRect(210, 20, 61, 21))
        self.connectButton.setObjectName("connectButton")
        self.tabWidget = QtWidgets.QTabWidget(self.mainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 800, 600))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.plotTest = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.plotTest.setContentsMargins(0, 0, 0, 0)
        self.plotTest.setObjectName("plotTest")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 771, 551))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_3, "")
        self.userDataBox = QtWidgets.QGroupBox(self.mainFrame)
        self.userDataBox.setGeometry(QtCore.QRect(820, 90, 280, 271))
        self.userDataBox.setMinimumSize(QtCore.QSize(280, 0))
        self.userDataBox.setObjectName("userDataBox")
        self.label = QtWidgets.QLabel(self.userDataBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.userDataBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.userDataBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.userDataBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_4.setObjectName("label_4")
        self.userName = QtWidgets.QLineEdit(self.userDataBox)
        self.userName.setGeometry(QtCore.QRect(130, 20, 141, 20))
        self.userName.setObjectName("userName")
        self.serialName = QtWidgets.QLineEdit(self.userDataBox)
        self.serialName.setGeometry(QtCore.QRect(130, 50, 141, 20))
        self.serialName.setObjectName("serialName")
        self.serialNumber = QtWidgets.QLineEdit(self.userDataBox)
        self.serialNumber.setGeometry(QtCore.QRect(130, 80, 141, 20))
        self.serialNumber.setObjectName("serialNumber")
        self.addDetails = QtWidgets.QLineEdit(self.userDataBox)
        self.addDetails.setGeometry(QtCore.QRect(130, 110, 141, 20))
        self.addDetails.setObjectName("addDetails")
        self.progressBar = QtWidgets.QProgressBar(self.userDataBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 150, 261, 20))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.userDataBox)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 190, 111, 21))
        self.lcdNumber.setObjectName("lcdNumber")
        self.autoSave = QtWidgets.QCheckBox(self.userDataBox)
        self.autoSave.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.autoSave.setObjectName("autoSave")
        self.timeLabel = QtWidgets.QLabel(self.userDataBox)
        self.timeLabel.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.timeLabel.setObjectName("timeLabel")
        self.startMeasure = QtWidgets.QPushButton(self.userDataBox)
        self.startMeasure.setGeometry(QtCore.QRect(160, 230, 111, 21))
        self.startMeasure.setObjectName("startMeasure")
        self.otherOptionsBox = QtWidgets.QGroupBox(self.mainFrame)
        self.otherOptionsBox.setGeometry(QtCore.QRect(820, 380, 280, 221))
        self.otherOptionsBox.setMinimumSize(QtCore.QSize(280, 0))
        self.otherOptionsBox.setObjectName("otherOptionsBox")
        self.saveReference = QtWidgets.QCheckBox(self.otherOptionsBox)
        self.saveReference.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.saveReference.setObjectName("saveReference")
        self.markersOn = QtWidgets.QCheckBox(self.otherOptionsBox)
        self.markersOn.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.markersOn.setObjectName("markersOn")
        self.addTrace = QtWidgets.QPushButton(self.otherOptionsBox)
        self.addTrace.setGeometry(QtCore.QRect(10, 80, 111, 23))
        self.addTrace.setObjectName("addTrace")
        self.removeTrace = QtWidgets.QPushButton(self.otherOptionsBox)
        self.removeTrace.setGeometry(QtCore.QRect(160, 80, 111, 23))
        self.removeTrace.setObjectName("removeTrace")
        self.checkBox = QtWidgets.QCheckBox(self.otherOptionsBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 120, 101, 20))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.mainFrame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtWidgets.QAction(MainWindow)
        self.actionColor.setObjectName("actionColor")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionFont)
        self.menuEdit.addAction(self.actionColor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Editor"))
        self.remoteConnectionBox.setTitle(_translate("MainWindow", "REMOTE CONNECTION"))
        self.remoteConnectionLabel.setText(_translate("MainWindow", "NO DEVICE CONNECTED"))
        self.instrumentAddress.setText(_translate("MainWindow", "TCPIP::CFO-MD-BQPVNA1::INSTR"))
        self.connectButton.setText(_translate("MainWindow", "CONNECT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Test 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Test 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Demo"))
        self.userDataBox.setTitle(_translate("MainWindow", "USER DATA"))
        self.label.setText(_translate("MainWindow", "Name (User):"))
        self.label_2.setText(_translate("MainWindow", "Serial name:"))
        self.label_3.setText(_translate("MainWindow", "Serial number:"))
        self.label_4.setText(_translate("MainWindow", "Add details:"))
        self.autoSave.setText(_translate("MainWindow", "Auto save data"))
        self.timeLabel.setText(_translate("MainWindow", "time..."))
        self.startMeasure.setText(_translate("MainWindow", "START MEASURE"))
        self.otherOptionsBox.setTitle(_translate("MainWindow", "OTHER OPTIONS"))
        self.saveReference.setText(_translate("MainWindow", "Save Reference"))
        self.markersOn.setText(_translate("MainWindow", "Markers ON"))
        self.addTrace.setText(_translate("MainWindow", "Add trace on screen"))
        self.removeTrace.setText(_translate("MainWindow", "Remove all"))
        self.checkBox.setText(_translate("MainWindow", "Larger Window"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionColor.setText(_translate("MainWindow", "Color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
