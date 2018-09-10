#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from ui.ui_shakespeare import UI_Shakespeare

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    shak = UI_Shakespeare()
    shak.show()
    sys.exit(ap.exec_())
