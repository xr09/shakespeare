#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Dec 29, 2009 on StormWind

2009 - 2013 Manuel E. Gutierrez <dhunterkde@gmail.com>
"""

import sys
from PyQt4.QtGui import QApplication
from ui.ui_shakespeare import UI_Shakespeare

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    shak = UI_Shakespeare()
    shak.show()
    sys.exit(ap.exec_())
