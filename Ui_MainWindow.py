# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/pyFinder/MainWindow.ui'
#
# Created: Sun Dec 23 16:06:16 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 360)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 21))
        self.label.setObjectName("label")
        self.keywordList = QtGui.QLineEdit(self.centralWidget)
        self.keywordList.setGeometry(QtCore.QRect(150, 230, 301, 22))
        self.keywordList.setObjectName("keywordList")
        self.selectButton = QtGui.QPushButton(self.centralWidget)
        self.selectButton.setGeometry(QtCore.QRect(80, 320, 91, 23))
        self.selectButton.setObjectName("selectButton")
        self.searchButton = QtGui.QPushButton(self.centralWidget)
        self.searchButton.setGeometry(QtCore.QRect(270, 320, 91, 23))
        self.searchButton.setObjectName("searchButton")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 121, 21))
        self.label_2.setObjectName("label_2")
        self.fileList = QtGui.QTableWidget(self.centralWidget)
        self.fileList.setGeometry(QtCore.QRect(20, 30, 431, 192))
        self.fileList.setObjectName("fileList")
        self.fileList.setColumnCount(2)
        self.fileList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(1, item)
        self.fileList.horizontalHeader().setStretchLastSection(True)
        self.buttonBox = QtGui.QGroupBox(self.centralWidget)
        self.buttonBox.setGeometry(QtCore.QRect(20, 260, 431, 61))
        self.buttonBox.setObjectName("buttonBox")
        self.useBMHBNFS = QtGui.QRadioButton(self.buttonBox)
        self.useBMHBNFS.setGeometry(QtCore.QRect(40, 30, 94, 21))
        self.useBMHBNFS.setChecked(True)
        self.useBMHBNFS.setObjectName("useBMHBNFS")
        self.useKMP = QtGui.QRadioButton(self.buttonBox)
        self.useKMP.setGeometry(QtCore.QRect(170, 30, 94, 21))
        self.useKMP.setObjectName("useKMP")
        self.useBM = QtGui.QRadioButton(self.buttonBox)
        self.useBM.setGeometry(QtCore.QRect(300, 30, 94, 21))
        self.useBM.setObjectName("useBM")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "待查询的文件列表:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setText(QtGui.QApplication.translate("MainWindow", "选择文件", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "查询", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "关键词列表(空格分隔):", None, QtGui.QApplication.UnicodeUTF8))
        self.fileList.setSortingEnabled(True)
        self.fileList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "文件名", None, QtGui.QApplication.UnicodeUTF8))
        self.fileList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "包含的关键字", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox.setTitle(QtGui.QApplication.translate("MainWindow", "匹配算法选择", None, QtGui.QApplication.UnicodeUTF8))
        self.useBMHBNFS.setText(QtGui.QApplication.translate("MainWindow", "BMHBNFS", None, QtGui.QApplication.UnicodeUTF8))
        self.useKMP.setText(QtGui.QApplication.translate("MainWindow", "KMP", None, QtGui.QApplication.UnicodeUTF8))
        self.useBM.setText(QtGui.QApplication.translate("MainWindow", "BM", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

