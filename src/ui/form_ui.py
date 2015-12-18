# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sat Aug  3 11:13:13 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(325, 340)
        MainWindow.setMinimumSize(QtCore.QSize(325, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/shakespeare.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.search_lineEdit.setText(_fromUtf8(""))
        self.search_lineEdit.setObjectName(_fromUtf8("search_lineEdit"))
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.clear_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clear_pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_pushButton.setIcon(icon1)
        self.clear_pushButton.setIconSize(QtCore.QSize(24, 20))
        self.clear_pushButton.setFlat(False)
        self.clear_pushButton.setObjectName(_fromUtf8("clear_pushButton"))
        self.horizontalLayout.addWidget(self.clear_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.language_pushButton = QtGui.QPushButton(self.centralwidget)
        self.language_pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/us-es.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/es-us.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.language_pushButton.setIcon(icon2)
        self.language_pushButton.setIconSize(QtCore.QSize(64, 22))
        self.language_pushButton.setCheckable(True)
        self.language_pushButton.setObjectName(_fromUtf8("language_pushButton"))
        self.horizontalLayout_2.addWidget(self.language_pushButton)
        self.searchtype_comboBox = QtGui.QComboBox(self.centralwidget)
        self.searchtype_comboBox.setObjectName(_fromUtf8("searchtype_comboBox"))
        self.searchtype_comboBox.addItem(_fromUtf8(""))
        self.searchtype_comboBox.addItem(_fromUtf8(""))
        self.searchtype_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.searchtype_comboBox)
        self.exact_checkBox = QtGui.QCheckBox(self.centralwidget)
        self.exact_checkBox.setObjectName(_fromUtf8("exact_checkBox"))
        self.horizontalLayout_2.addWidget(self.exact_checkBox)
        spacerItem = QtGui.QSpacerItem(17, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.result_TextEdit = QtGui.QTextEdit(self.centralwidget)
        self.result_TextEdit.setReadOnly(True)
        self.result_TextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.result_TextEdit.setObjectName(_fromUtf8("result_TextEdit"))
        self.gridLayout.addWidget(self.result_TextEdit, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/imgs/acercaQT.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Qt.setIcon(icon4)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.clear_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_lineEdit.clear)
        QtCore.QObject.connect(self.clear_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.result_TextEdit.clear)
        QtCore.QObject.connect(self.language_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_lineEdit.setFocus)
        QtCore.QObject.connect(self.exact_checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_lineEdit.setFocus)
        QtCore.QObject.connect(self.clear_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_lineEdit.setFocus)
        QtCore.QObject.connect(self.searchtype_comboBox, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.search_lineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Shakespeare", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_pushButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+3", "Alt+Backspace", QtGui.QApplication.UnicodeUTF8))
        self.language_pushButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+1", None, QtGui.QApplication.UnicodeUTF8))
        self.searchtype_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Starts with", None, QtGui.QApplication.UnicodeUTF8))
        self.searchtype_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Ends with", None, QtGui.QApplication.UnicodeUTF8))
        self.searchtype_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Contains", None, QtGui.QApplication.UnicodeUTF8))
        self.exact_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Exact search", None, QtGui.QApplication.UnicodeUTF8))
        self.exact_checkBox.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+2", None, QtGui.QApplication.UnicodeUTF8))
        self.result_TextEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About Shakespeare", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
