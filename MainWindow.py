# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os
from PySide.QtCore import Slot, QFile
from PySide.QtGui import QMainWindow, QDesktopWidget, QFileDialog, QMessageBox, QTableWidgetItem
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()
        self.files = None
    
    def center(self, parent=None):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    
    @Slot()
    def on_selectButton_clicked(self):
        self.fileList.clearContents()
        self.files = QFileDialog.getOpenFileNames(self, u'选择文件')[0]
        self.fileNames = map(lambda x: os.path.split(x)[1], self.files)
        self.fileList.setRowCount(len(self.fileNames))
        for idx, fileName in enumerate(self.fileNames):
            self.fileList.setItem(idx, 0, QTableWidgetItem(fileName))
        
    @Slot()
    def on_searchButton_clicked(self):
        if self.files is None:
            QMessageBox.critical(self, u'错误', u'未选择要查询的文件')
        else:
            self.keywords = self.keywordList.text()
            if self.keywords == '':
                QMessageBox.critical(self, u'错误', u'未输入要查询的关键词')
                
        