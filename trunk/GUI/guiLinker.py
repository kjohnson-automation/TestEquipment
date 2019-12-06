# This file will link all the functions from the limiterTest to useful things in the actual back end.
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtGui
from LimiterTest_0_2 import Ui_LimiterTest

class AppWindow(Ui_LimiterTest):
    def __init__(self, window):
        Ui_LimiterTest.__init__(self)
        self.setupUi(window)
        self.window = window
        self.window.show()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    # dialog = QDialog()
    LimiterTest = AppWindow(window)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()