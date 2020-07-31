#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Interface gráfica do programa de automatização do evo
"""

__version__ = "0.0.1"
__author__ = "Daniel Mascarenhas"
__email__ = "daniel.mascarenhas@siemens-healthineers.com"
__maintainer__ = "Daniel Mascarenhas"                         # should be the person who will fix bugs and make improvements
__copyright__ = "Copyright 2020, Siemens Healthineers"
__license__ = "GPL"
__status__ = "Prototype"                               # Prototype, Development or Production
__credits__ = ["Daniel Mascarenhas", "Gersiano Santana"]                      # also include contributors that wrote no code

# --------------------------------------------------------------------------------

# Import built-in modules first
# followed by third-party modules
# followed by any changes to the path
# your own modules.

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


def main(args=None):
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
