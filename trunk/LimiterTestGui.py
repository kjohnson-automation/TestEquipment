# This file will link all the functions from the limiterTest to useful things in the actual back end.
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtGui
from GUI.LimiterTest_0_2 import Ui_LimiterTest

import Agilent8648, AgilentE36XX, AgilentE4443
import LimiterTest

# NOTE on how to use UIC to convert .ui to .py:
# pyuic5 LimiterTest_0_2.ui -o LimiterTest_0_2.py

class AppWindow(Ui_LimiterTest):
    def __init__(self, window):
        Ui_LimiterTest.__init__(self)
        self.setupUi(window)
        self.window = window
        self.add_connections()
        self.window.show()
        self.check_checkboxes()

    def check_checkboxes(self):
        """ Checks the checkbox status """
        self.set_editable_ps1()
        self.set_editable_ps2()
        self.set_editable_sg1()
        self.set_editable_sg2()

    def set_editable_sg1(self):
        """ Enables/Disables Editable Parameters based on Using Equipment"""
        if self.cb_useSigGen.isChecked():
            editable = True
        else:
            editable = False
        self.e_SigGenGPIB_2.setEnabled(editable)
        self.e_startFreq.setEnabled(editable)
        self.e_stopFreq.setEnabled(editable)
        self.e_stepFreq.setEnabled(editable)
        self.e_startPower.setEnabled(editable)
        self.e_stopPower.setEnabled(editable)
        self.e_stepPower.setEnabled(editable)

    def set_editable_sg2(self):
        """ Enables/Disables Signal Generator 2 Parameters based on checkbox """
        if self.cb_useSigGen_2.isChecked():
            editable = True
        else:
            editable = False
        self.e_SigGenGPIB_2.setEnabled(editable)
        self.e_startFreq_2.setEnabled(editable)
        self.e_stopFreq_2.setEnabled(editable)
        self.e_stepFreq_2.setEnabled(editable)
        self.e_startPower_2.setEnabled(editable)
        self.e_stopPower_2.setEnabled(editable)
        self.e_stepPower_2.setEnabled(editable)

    def set_editable_ps1(self):
        """ Enables/Disables Editable Parameters based on Using Equipment"""
        print("setting ps1 enables")
        if self.cb_usePowerSupply.isChecked():
            editable = True
        else:
            editable = False
        print("Editable: {0}".format(editable))
        self.e_psuGPIB.setEnabled(editable)
        self.e_psuStartV.setEnabled(editable)
        self.e_psuStopV.setEnabled(editable)
        self.e_psuStepV.setEnabled(editable)

    def set_editable_ps2(self):
        """ Enables/Disables the Editable parameters for PS2 based on checkbox """
        if self.cb_usePowerSupply_2.isChecked():
            editable = True
        else:
            editable = False
        self.e_psuGPIB_2.setEnabled(editable)
        self.e_psuStartV_2.setEnabled(editable)
        self.e_psuStopV_2.setEnabled(editable)
        self.e_psuStepV_2.setEnabled(editable)

    def add_connections(self):
        """ Links the fields of the gui to test equipment attributes """
        self.b_startTest.clicked.connect(self.start_limiter_test)
        # Handles greying out boxes not to be used.
        self.cb_useSigGen.clicked.connect(self.set_editable_sg1)
        self.cb_useSigGen_2.clicked.connect(self.set_editable_sg2)
        self.cb_usePowerSupply.clicked.connect(self.set_editable_ps1)
        self.cb_usePowerSupply_2.clicked.connect(self.set_editable_ps2)

        self.b_exit.clicked.connect(self.close)

    def start_limiter_test(self):
        """ this is where the magic will happend, it will pull in all fields from the gui and execute the limiter test """
        limiter

    def close(self):
        print("User has exited")
        sys.exit("User has closed the gui")

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    # dialog = QDialog()
    LimiterTest = AppWindow(window)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
