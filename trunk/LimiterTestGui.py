# This file will link all the functions from the limiterTest to useful things in the actual back end.
import sys
import time
# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtGui
# NOTE: Need to keep this up to date. May be worth writing a
# a linker script that does base linking from gui buttons to features
from gui.LimiterTest_0_5_test import Ui_LimiterTest

import Agilent8648, AgilentE36XX, AgilentE4443
from LimiterTestForGui import LimiterTest as Test

# NOTE on how to use UIC to convert .ui to .py:
# pyuic5 LimiterTest_0_x.ui -o LimiterTest_0_x.py

class AppWindow(Ui_LimiterTest):
    def __init__(self):
        # Ui_LimiterTest.__init__(self)
        self.window = QMainWindow()
        self.setupUi(self.window)
        self.add_connections()
        self.set_default_sgs()
        self.check_checkboxes()
        self.window.show()

    def check_checkboxes(self):
        """ Checks the checkbox status """
        self.set_editable_ps1()
        self.set_editable_ps2()
        self.set_editable_sg1()
        self.set_editable_sg2()

    def set_default_sgs(self):
        """ By Default enables the signal generators for the limiter test """
        self.cb_useSigGen.setChecked(True)
        self.cb_useSigGen_2.setChecked(True)

    def set_editable_sg1(self):
        """ Enables/Disables Editable Parameters based on Using Equipment"""
        if self.cb_useSigGen.isChecked():
            editable = True
        else:
            editable = False
        self.e_SigGenGPIB.setEnabled(editable)
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
        if self.cb_usePowerSupply.isChecked():
            editable = True
        else:
            editable = False
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
        # Handles greying out boxes not to be used.
        self.cb_useSigGen.clicked.connect(self.set_editable_sg1)
        self.cb_useSigGen_2.clicked.connect(self.set_editable_sg2)
        self.cb_usePowerSupply.clicked.connect(self.set_editable_ps1)
        self.cb_usePowerSupply_2.clicked.connect(self.set_editable_ps2)

        self.b_startTest.clicked.connect(self.start_limiter_test)
        self.b_exit.clicked.connect(self.close)

    def get_test_info(self):
        """ Gets the generic test info from the GUI """
        test_info = {}
        self.update_test_info()
        test_info["p_no"] = self.e_partNumber.text()
        test_info["lot"] = self.e_lotWafer.text()
        test_info["temp"] = self.e_temp.text()
        test_info["tester"] = self.e_testOperator.text()
        return test_info

    def update_test_info(self):
        """ Updates the text for test info """
        self.e_partNumber.update()
        self.e_lotWafer.update()
        self.e_temp.update()
        self.e_testOperator.update()

    def get_sg1_params(self):
        """ Gets all the parameters from signal generator 1 """
        sg_params = {}
        if self.cb_useSigGen.isChecked():
            self.update_sg1()
            sg_params["sg1_gpib"] = self.e_SigGenGPIB.text()
            sg_params["sg1_start_f"] = self.e_startFreq.text()
            sg_params["sg1_stop_f"] = self.e_stopFreq.text()
            sg_params["sg1_step_f"] = self.e_stepFreq.text()
            sg_params["sg1_start_p"] = self.e_startPower.text()
            sg_params["sg1_stop_p"] = self.e_stopPower.text()
            sg_params["sg1_step_p"] = self.e_stepPower.text()
        return sg_params

    def update_sg1(self):
        """ Updates the text fields for Signal Generator 1 """
        self.e_SigGenGPIB.update()
        self.e_startFreq.update()
        self.e_stopFreq.update()
        self.e_stepFreq.update()
        self.e_startPower.update()
        self.e_stopPower.update()
        self.e_stepPower.update()

    def get_sg2_params(self):
        """ Gets all the parameters from signal generator 2 """
        sg2_params = {}
        if self.cb_useSigGen_2.isChecked():
            self.update_sg2()
            sg2_params["sg2_gpib"] = self.e_SigGenGPIB_2.text()
            sg2_params["sg2_start_f"] = self.e_startFreq_2.text()
            sg2_params["sg2_stop_f"] = self.e_stopFreq_2.text()
            sg2_params["sg2_step_f"] = self.e_stepFreq_2.text()
            sg2_params["sg2_start_p"] = self.e_startPower_2.text()
            sg2_params["sg2_stop_p"] = self.e_stopPower_2.text()
            sg2_params["sg2_step_p"] = self.e_stepPower_2.text()
        return sg2_params

    def update_sg2(self):
        """ Updates the text fields for Signal Generator 2 """
        self.e_SigGenGPIB_2.update()
        self.e_startFreq_2.update()
        self.e_stopFreq_2.update()
        self.e_stepFreq_2.update()
        self.e_startPower_2.update()
        self.e_stopPower_2.update()
        self.e_stepPower_2.update()

    def get_psu1_params(self):
        """ Gets all the parameters from power supply 1 """
        psu1_params = {}
        self.update_ps1()
        return psu1_params

    def update_ps1(self):
        """ Updates the test fields for Power Supply 1 """
        pass

    def get_psu2_params(self):
        """ Gets all the parameters from power supply 2 """
        psu2_params = {}
        self.update_ps2()
        return psu2_params

    def update_ps2(self):
        """ Updates the test fields for Power Supply 2 """
        pass

    def get_spectrum_analyzer_params(self):
        """ Gets the spectrum analyzer parameters """
        sa_params = {}
        self.update_spectrum_analyzer()
        sa_params["sa_gpib"] = self.e_specAnalyzerGPIB.text()
        if self.cb_man_vrbw.isChecked():
            sa_params["sa_vb"] = self.e_videoBW.text()
            sa_params["sa_rb"] = self.e_resolutionBW.text()
        return sa_params

    def update_spectrum_analyzer(self):
        """ Updates the text fields for the spectrum analyzer """
        self.e_specAnalyzerGPIB.update()
        self.e_resolutionBW.update()
        self.e_videoBW.update()

    def generate_kwargs(self):
        """ Gathers available fields and creates the params dictionary with them for use in the limiter test """
        returned_kwargs = {}
        returned_kwargs.update(self.get_test_info())
        returned_kwargs.update(self.get_sg1_params())
        returned_kwargs.update(self.get_sg2_params())
        ### SHOULD DO NOTHING FOR RIGHT NOW ###
        returned_kwargs.update(self.get_psu1_params())
        returned_kwargs.update(self.get_psu2_params())
        #######################################
        returned_kwargs.update(self.get_spectrum_analyzer_params())
        return returned_kwargs

    def generic_field_update(self, fields):
        """ Updates <fields> from UI view for getting data """
        if not isinstance(fields, list):
            fields = [fields]
        for field in fields:
            try:
                field = getattr(self, field)
            except NameError:
                print("No attribute {0}".format(field))
                continue
            try:
                field.update()
            except AttributeError:
                print("Failed to update {0}".format(field))
                continue

    def plot_file(self, file_location):
        """ Prints the plot data in the gui """
        print("File Location: {0}".format(file_location.name))

    def start_limiter_test(self):
        """ this is where the magic will happend, it will pull in all fields from the gui and execute the limiter test """
        params = self.generate_kwargs()
        test = Test(kwargs=params)
        write_file = test.test_OIP3()
        self.plot_file(write_file)

    def close(self):
        print("User has exited")
        sys.exit("User has closed the gui")

def main():
    print("main")
    app = QApplication(sys.argv)
    # dialog = QDialog()
    w_LimiterTest = AppWindow()
    print("executing")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
