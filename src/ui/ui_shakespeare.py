#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QMainWindow, QApplication, QSystemTrayIcon, QAction, qApp, QMenu)
from PyQt5.QtGui import (QKeySequence, QIcon)
from PyQt5.QtCore import Qt
from .form_ui import Ui_MainWindow
from core.shakespeare import Shakespeare

VERSION = '0.7beta1'
BUILD_DATE = '2013-08-03'


class UI_Shakespeare(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI_Shakespeare, self).__init__(parent)
        self.setupUi(self)
        self.result_TextEdit.setFontPointSize(10)
        self.actionQuit.setShortcut(QKeySequence('Ctrl+Q'))
        self.actionHide = QAction(self, triggered=self.hide)
        self.actionHide.setShortcut(Qt.Key_Escape)
        self.engine = Shakespeare()
        self.search_lineEdit.setFocus()
        self.setupSysTray()
        self.rightCorner()

    def rightCorner(self):
        widget = QApplication.desktop()
        screenwidth = widget.width()
        screenheight = widget.height()
        windowsize = self.size()
        width = windowsize.width()
        height = windowsize.height()
        x = screenwidth - width
        y = screenheight - height
        y -= 50
        self.move(x, y)

    def setupSysTray(self):
        self.trayIcon = QSystemTrayIcon(QIcon(':/icons/imgs/shakespeare.png'))
        self.trayIcon.activated.connect(self.restore)
        quitAction = QAction(QIcon(":/icons/imgs/quit.png"), "Quit", self, triggered=qApp.quit)
        trayIconMenu = QMenu(self)
        trayIconMenu.addAction(quitAction)
        self.trayIcon.setContextMenu(trayIconMenu)
        self.trayIcon.show()
        # hide with Escape
        # esc_shorcut = QtGui.QShortcut(
        #                               QKeySequence(
        #                               Qt.Key_Escape), self)
        # self.connect(esc_shorcut, SIGNAL("activated()"), self.hide)

    def restore(self, reason):
        """Toggle main window visibility"""
        if reason == 3:
            if self.isVisible():
                self.hide()
            else:
                self.update()
                self.show()

    # @QtCore.pyqtSignature("")
    # def on_clear_pushButton_clicked(self):
    #     self.search()

    # @QtCore.pyqtSignature("")
    # def on_language_pushButton_clicked(self):
    #     self.search()

    # def statusMessage(self, amount):
    #     message = ('%i words found' % amount) if amount else 'word not found'
    #     self.statusbar.showMessage(message)

    # def renderText(self, result, reverse=False):
    #     if reverse:
    #         color1, color2 = 'Red', 'Blue'
    #     else:
    #         color1, color2 = 'Blue', 'Red'
    #     for e, s in result:
    #         self.result_TextEdit.setTextColor(QtGui.QColor(color1))
    #         self.result_TextEdit.insertPlainText(e)
    #         self.result_TextEdit.setTextColor(QtGui.QColor('Black'))
    #         self.result_TextEdit.insertPlainText(' : ')
    #         self.result_TextEdit.setTextColor(QtGui.QColor(color2))
    #         self.result_TextEdit.insertPlainText('  ' + s + '\n')

    # def search(self):
    #     self.result_TextEdit.clear()
    #     if not self.search_lineEdit.text().length():
    #         self.statusbar.clearMessage()
    #         return
    #     result = self.engine.search(self.search_lineEdit.text(),
    #                             self.searchtype_comboBox.currentIndex(),
    #                             self.exact_checkBox.isChecked(),
    #                             self.language_pushButton.isChecked())
    #     self.statusMessage(len(result))
    #     if not result:
    #         self.statusMessage(len(result))
    #         return
    #     self.renderText(result, self.language_pushButton.isChecked())

    # @QtCore.pyqtSignature("QString")
    # def on_search_lineEdit_textChanged(self):
    #     self.search()

    # @QtCore.pyqtSignature('int')
    # def on_exact_checkBox_stateChanged(self):
    #     self.search()
    #     self.searchtype_comboBox.setVisible(
    #                                     not self.exact_checkBox.isChecked())

    # @QtCore.pyqtSignature('int')
    # def on_searchtype_comboBox_currentIndexChanged(self):
    #     self.search()

    # @QtCore.pyqtSignature('')
    # def on_actionQuit_triggered(self):
    #     QtGui.qApp.quit()

    # @QtCore.pyqtSignature('')
    # def on_actionAbout_triggered(self):
    #     QtGui.QMessageBox.about(self, u"About Shakespeare",
    #     u"<h3>Shakespeare %s </h3>\
    #     English/Spanish dictionary <br/>\
    #     <hr>(C) Manuel E. Gutierrez 2007-2013 <br/>\
    #      <br/>This program is licensed under the GPL v3<br />\
    #      <br />\
    #      http://github.org/xr09/shakespeare</p>" % unicode(VERSION))

    # @QtCore.pyqtSignature('')
    # def on_actionAbout_Qt_triggered(self):
    #     QtGui.QMessageBox.aboutQt(self)

    # @QtCore.pyqtSignature("")
    # def closeEvent(self, event):
    #     self.hide()
    #     event.ignore()
from . import res_rc