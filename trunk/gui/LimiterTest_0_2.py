# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LimiterTest_0_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LimiterTest(object):
    def setupUi(self, LimiterTest):
        LimiterTest.setObjectName("LimiterTest")
        LimiterTest.resize(1580, 970)
        self.centralwidget = QtWidgets.QWidget(LimiterTest)
        self.centralwidget.setObjectName("centralwidget")
        self.w_sigGen = QtWidgets.QWidget(self.centralwidget)
        self.w_sigGen.setGeometry(QtCore.QRect(30, 200, 431, 301))
        self.w_sigGen.setObjectName("w_sigGen")
        self.cb_useSigGen = QtWidgets.QCheckBox(self.w_sigGen)
        self.cb_useSigGen.setGeometry(QtCore.QRect(30, 10, 151, 20))
        self.cb_useSigGen.setObjectName("cb_useSigGen")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.w_sigGen)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 381, 241))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.l_sigGenGPIB = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_sigGenGPIB.setObjectName("l_sigGenGPIB")
        self.verticalLayout_3.addWidget(self.l_sigGenGPIB)
        self.l_startFreq = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_startFreq.setObjectName("l_startFreq")
        self.verticalLayout_3.addWidget(self.l_startFreq)
        self.l_stopFreq = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_stopFreq.setObjectName("l_stopFreq")
        self.verticalLayout_3.addWidget(self.l_stopFreq)
        self.l_stepFreq = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_stepFreq.setObjectName("l_stepFreq")
        self.verticalLayout_3.addWidget(self.l_stepFreq)
        self.l_startPower = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_startPower.setObjectName("l_startPower")
        self.verticalLayout_3.addWidget(self.l_startPower)
        self.l_stopPower = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_stopPower.setObjectName("l_stopPower")
        self.verticalLayout_3.addWidget(self.l_stopPower)
        self.l_stepPower = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.l_stepPower.setObjectName("l_stepPower")
        self.verticalLayout_3.addWidget(self.l_stepPower)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.e_SigGenGPIB = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_SigGenGPIB.setObjectName("e_SigGenGPIB")
        self.verticalLayout_4.addWidget(self.e_SigGenGPIB)
        self.e_startFreq = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_startFreq.setObjectName("e_startFreq")
        self.verticalLayout_4.addWidget(self.e_startFreq)
        self.e_stopFreq = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_stopFreq.setObjectName("e_stopFreq")
        self.verticalLayout_4.addWidget(self.e_stopFreq)
        self.e_stepFreq = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_stepFreq.setObjectName("e_stepFreq")
        self.verticalLayout_4.addWidget(self.e_stepFreq)
        self.e_startPower = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_startPower.setObjectName("e_startPower")
        self.verticalLayout_4.addWidget(self.e_startPower)
        self.e_stopPower = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_stopPower.setObjectName("e_stopPower")
        self.verticalLayout_4.addWidget(self.e_stopPower)
        self.e_stepPower = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.e_stepPower.setObjectName("e_stepPower")
        self.verticalLayout_4.addWidget(self.e_stepPower)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.w_sigGen_2 = QtWidgets.QWidget(self.centralwidget)
        self.w_sigGen_2.setGeometry(QtCore.QRect(30, 530, 431, 301))
        self.w_sigGen_2.setObjectName("w_sigGen_2")
        self.cb_useSigGen_2 = QtWidgets.QCheckBox(self.w_sigGen_2)
        self.cb_useSigGen_2.setGeometry(QtCore.QRect(30, 10, 151, 20))
        self.cb_useSigGen_2.setObjectName("cb_useSigGen_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.w_sigGen_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 40, 381, 241))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_sigGenGPIB_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_sigGenGPIB_2.setObjectName("l_sigGenGPIB_2")
        self.verticalLayout_5.addWidget(self.l_sigGenGPIB_2)
        self.l_startFreq_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_startFreq_2.setObjectName("l_startFreq_2")
        self.verticalLayout_5.addWidget(self.l_startFreq_2)
        self.l_stopFreq_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_stopFreq_2.setObjectName("l_stopFreq_2")
        self.verticalLayout_5.addWidget(self.l_stopFreq_2)
        self.l_stepFreq_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_stepFreq_2.setObjectName("l_stepFreq_2")
        self.verticalLayout_5.addWidget(self.l_stepFreq_2)
        self.l_startPower_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_startPower_2.setObjectName("l_startPower_2")
        self.verticalLayout_5.addWidget(self.l_startPower_2)
        self.l_stopPower_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_stopPower_2.setObjectName("l_stopPower_2")
        self.verticalLayout_5.addWidget(self.l_stopPower_2)
        self.l_stepPower_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l_stepPower_2.setObjectName("l_stepPower_2")
        self.verticalLayout_5.addWidget(self.l_stepPower_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.e_SigGenGPIB_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_SigGenGPIB_2.setObjectName("e_SigGenGPIB_2")
        self.verticalLayout_6.addWidget(self.e_SigGenGPIB_2)
        self.e_startFreq_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_startFreq_2.setObjectName("e_startFreq_2")
        self.verticalLayout_6.addWidget(self.e_startFreq_2)
        self.e_stopFreq_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_stopFreq_2.setObjectName("e_stopFreq_2")
        self.verticalLayout_6.addWidget(self.e_stopFreq_2)
        self.e_stepFreq_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_stepFreq_2.setObjectName("e_stepFreq_2")
        self.verticalLayout_6.addWidget(self.e_stepFreq_2)
        self.e_startPower_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_startPower_2.setObjectName("e_startPower_2")
        self.verticalLayout_6.addWidget(self.e_startPower_2)
        self.e_stopPower_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_stopPower_2.setObjectName("e_stopPower_2")
        self.verticalLayout_6.addWidget(self.e_stopPower_2)
        self.e_stepPower_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.e_stepPower_2.setObjectName("e_stepPower_2")
        self.verticalLayout_6.addWidget(self.e_stepPower_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 431, 181))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 381, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_partNumber = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_partNumber.setObjectName("l_partNumber")
        self.verticalLayout.addWidget(self.l_partNumber)
        self.l_lotWafer = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_lotWafer.setObjectName("l_lotWafer")
        self.verticalLayout.addWidget(self.l_lotWafer)
        self.l_temp = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_temp.setObjectName("l_temp")
        self.verticalLayout.addWidget(self.l_temp)
        self.l_testOperator = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_testOperator.setObjectName("l_testOperator")
        self.verticalLayout.addWidget(self.l_testOperator)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.e_partNumber = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.e_partNumber.setObjectName("e_partNumber")
        self.verticalLayout_2.addWidget(self.e_partNumber)
        self.e_lotWafter = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.e_lotWafter.setObjectName("e_lotWafter")
        self.verticalLayout_2.addWidget(self.e_lotWafter)
        self.e_temp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.e_temp.setObjectName("e_temp")
        self.verticalLayout_2.addWidget(self.e_temp)
        self.e_testOperator = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.e_testOperator.setObjectName("e_testOperator")
        self.verticalLayout_2.addWidget(self.e_testOperator)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.w_psu = QtWidgets.QWidget(self.centralwidget)
        self.w_psu.setGeometry(QtCore.QRect(500, 10, 271, 201))
        self.w_psu.setObjectName("w_psu")
        self.cb_usePowerSupply = QtWidgets.QCheckBox(self.w_psu)
        self.cb_usePowerSupply.setGeometry(QtCore.QRect(30, 10, 131, 21))
        self.cb_usePowerSupply.setObjectName("cb_usePowerSupply")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.w_psu)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 40, 211, 141))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.l_psuGPIB = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.l_psuGPIB.setObjectName("l_psuGPIB")
        self.verticalLayout_7.addWidget(self.l_psuGPIB)
        self.l_psuStartV = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.l_psuStartV.setObjectName("l_psuStartV")
        self.verticalLayout_7.addWidget(self.l_psuStartV)
        self.l_psuStopV = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.l_psuStopV.setObjectName("l_psuStopV")
        self.verticalLayout_7.addWidget(self.l_psuStopV)
        self.l_psuStepV = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.l_psuStepV.setObjectName("l_psuStepV")
        self.verticalLayout_7.addWidget(self.l_psuStepV)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.e_psuGPIB = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.e_psuGPIB.setObjectName("e_psuGPIB")
        self.verticalLayout_8.addWidget(self.e_psuGPIB)
        self.e_psuStartV = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.e_psuStartV.setObjectName("e_psuStartV")
        self.verticalLayout_8.addWidget(self.e_psuStartV)
        self.e_psuStopV = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.e_psuStopV.setObjectName("e_psuStopV")
        self.verticalLayout_8.addWidget(self.e_psuStopV)
        self.e_psuStepV = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.e_psuStepV.setObjectName("e_psuStepV")
        self.verticalLayout_8.addWidget(self.e_psuStepV)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.w_psu_2 = QtWidgets.QWidget(self.centralwidget)
        self.w_psu_2.setGeometry(QtCore.QRect(790, 10, 271, 201))
        self.w_psu_2.setObjectName("w_psu_2")
        self.cb_usePowerSupply_2 = QtWidgets.QCheckBox(self.w_psu_2)
        self.cb_usePowerSupply_2.setGeometry(QtCore.QRect(30, 10, 131, 21))
        self.cb_usePowerSupply_2.setObjectName("cb_usePowerSupply_2")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.w_psu_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(30, 40, 211, 141))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.l_psuGPIB_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.l_psuGPIB_2.setObjectName("l_psuGPIB_2")
        self.verticalLayout_11.addWidget(self.l_psuGPIB_2)
        self.l_psuStartV_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.l_psuStartV_2.setObjectName("l_psuStartV_2")
        self.verticalLayout_11.addWidget(self.l_psuStartV_2)
        self.l_psuStopV_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.l_psuStopV_2.setObjectName("l_psuStopV_2")
        self.verticalLayout_11.addWidget(self.l_psuStopV_2)
        self.l_psuStepV_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.l_psuStepV_2.setObjectName("l_psuStepV_2")
        self.verticalLayout_11.addWidget(self.l_psuStepV_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.e_psuGPIB_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.e_psuGPIB_2.setObjectName("e_psuGPIB_2")
        self.verticalLayout_12.addWidget(self.e_psuGPIB_2)
        self.e_psuStartV_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.e_psuStartV_2.setObjectName("e_psuStartV_2")
        self.verticalLayout_12.addWidget(self.e_psuStartV_2)
        self.e_psuStopV_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.e_psuStopV_2.setObjectName("e_psuStopV_2")
        self.verticalLayout_12.addWidget(self.e_psuStopV_2)
        self.e_psuStepV_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.e_psuStepV_2.setObjectName("e_psuStepV_2")
        self.verticalLayout_12.addWidget(self.e_psuStepV_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.w_spectrumAnalyzer = QtWidgets.QWidget(self.centralwidget)
        self.w_spectrumAnalyzer.setGeometry(QtCore.QRect(1090, 10, 381, 191))
        self.w_spectrumAnalyzer.setObjectName("w_spectrumAnalyzer")
        self.checkBox = QtWidgets.QCheckBox(self.w_spectrumAnalyzer)
        self.checkBox.setGeometry(QtCore.QRect(40, 20, 231, 20))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.w_spectrumAnalyzer)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(40, 60, 301, 101))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.l_specAnalyzer = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.l_specAnalyzer.setObjectName("l_specAnalyzer")
        self.verticalLayout_9.addWidget(self.l_specAnalyzer)
        self.l_videoBW = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.l_videoBW.setObjectName("l_videoBW")
        self.verticalLayout_9.addWidget(self.l_videoBW)
        self.l_resolutionBW = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.l_resolutionBW.setObjectName("l_resolutionBW")
        self.verticalLayout_9.addWidget(self.l_resolutionBW)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.e_specAnalyzerGPIB = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.e_specAnalyzerGPIB.setObjectName("e_specAnalyzerGPIB")
        self.verticalLayout_10.addWidget(self.e_specAnalyzerGPIB)
        self.e_videoBW = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.e_videoBW.setObjectName("e_videoBW")
        self.verticalLayout_10.addWidget(self.e_videoBW)
        self.e_resolutionBW = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.e_resolutionBW.setObjectName("e_resolutionBW")
        self.verticalLayout_10.addWidget(self.e_resolutionBW)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.w_MatPlot = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.w_MatPlot.setGeometry(QtCore.QRect(530, 260, 961, 561))
        self.w_MatPlot.setObjectName("w_MatPlot")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(1180, 840, 311, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.b_exit = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.b_exit.setObjectName("b_exit")
        self.horizontalLayout_8.addWidget(self.b_exit)
        self.b_startTest = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.b_startTest.setObjectName("b_startTest")
        self.horizontalLayout_8.addWidget(self.b_startTest)
        LimiterTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LimiterTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1579, 26))
        self.menubar.setObjectName("menubar")
        self.menuLimiter_Test_Gui = QtWidgets.QMenu(self.menubar)
        self.menuLimiter_Test_Gui.setObjectName("menuLimiter_Test_Gui")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        LimiterTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LimiterTest)
        self.statusbar.setObjectName("statusbar")
        LimiterTest.setStatusBar(self.statusbar)
        self.actionAbout_Limiter_Test_Gui = QtWidgets.QAction(LimiterTest)
        self.actionAbout_Limiter_Test_Gui.setObjectName("actionAbout_Limiter_Test_Gui")
        self.actionSave_Settings = QtWidgets.QAction(LimiterTest)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionExit = QtWidgets.QAction(LimiterTest)
        self.actionExit.setObjectName("actionExit")
        self.menuLimiter_Test_Gui.addAction(self.actionSave_Settings)
        self.menuLimiter_Test_Gui.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Limiter_Test_Gui)
        self.menubar.addAction(self.menuLimiter_Test_Gui.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(LimiterTest)
        QtCore.QMetaObject.connectSlotsByName(LimiterTest)

    def retranslateUi(self, LimiterTest):
        _translate = QtCore.QCoreApplication.translate
        LimiterTest.setWindowTitle(_translate("LimiterTest", "LimiterTest"))
        self.cb_useSigGen.setText(_translate("LimiterTest", "Use Signal Generator"))
        self.l_sigGenGPIB.setText(_translate("LimiterTest", "GPIB Address:"))
        self.l_startFreq.setText(_translate("LimiterTest", "Start Frequency:"))
        self.l_stopFreq.setText(_translate("LimiterTest", "Stop Frequency:"))
        self.l_stepFreq.setText(_translate("LimiterTest", "Step Frequency:"))
        self.l_startPower.setText(_translate("LimiterTest", "Start Power:"))
        self.l_stopPower.setText(_translate("LimiterTest", "Stop Power:"))
        self.l_stepPower.setText(_translate("LimiterTest", "Step Power:"))
        self.e_SigGenGPIB.setText(_translate("LimiterTest", "19"))
        self.cb_useSigGen_2.setText(_translate("LimiterTest", "Use Signal Generator"))
        self.l_sigGenGPIB_2.setText(_translate("LimiterTest", "GPIB Address:"))
        self.l_startFreq_2.setText(_translate("LimiterTest", "Start Frequency:"))
        self.l_stopFreq_2.setText(_translate("LimiterTest", "Stop Frequency:"))
        self.l_stepFreq_2.setText(_translate("LimiterTest", "Step Frequency:"))
        self.l_startPower_2.setText(_translate("LimiterTest", "Start Power:"))
        self.l_stopPower_2.setText(_translate("LimiterTest", "Stop Power:"))
        self.l_stepPower_2.setText(_translate("LimiterTest", "Step Power:"))
        self.e_SigGenGPIB_2.setText(_translate("LimiterTest", "21"))
        self.l_partNumber.setText(_translate("LimiterTest", "Part Number:"))
        self.l_lotWafer.setText(_translate("LimiterTest", "Lot/Wafer:"))
        self.l_temp.setText(_translate("LimiterTest", "DUT Temp:"))
        self.l_testOperator.setText(_translate("LimiterTest", "Tester:"))
        self.cb_usePowerSupply.setText(_translate("LimiterTest", "Use Power Supply"))
        self.l_psuGPIB.setText(_translate("LimiterTest", "GPIB Address:"))
        self.l_psuStartV.setText(_translate("LimiterTest", "Start Voltage:"))
        self.l_psuStopV.setText(_translate("LimiterTest", "Stop Voltage:"))
        self.l_psuStepV.setText(_translate("LimiterTest", "Step Voltage:"))
        self.e_psuGPIB.setText(_translate("LimiterTest", "6"))
        self.cb_usePowerSupply_2.setText(_translate("LimiterTest", "Use Power Supply"))
        self.l_psuGPIB_2.setText(_translate("LimiterTest", "GPIB Address:"))
        self.l_psuStartV_2.setText(_translate("LimiterTest", "Start Voltage:"))
        self.l_psuStopV_2.setText(_translate("LimiterTest", "Stop Voltage:"))
        self.l_psuStepV_2.setText(_translate("LimiterTest", "Step Voltage:"))
        self.e_psuGPIB_2.setText(_translate("LimiterTest", "5"))
        self.checkBox.setText(_translate("LimiterTest", "Manually Set Video/Resolution BW"))
        self.l_specAnalyzer.setText(_translate("LimiterTest", "Spectrum Analyzer GPIB:"))
        self.l_videoBW.setText(_translate("LimiterTest", "Video Bandwidth:"))
        self.l_resolutionBW.setText(_translate("LimiterTest", "Resolution Bandwidth:"))
        self.e_specAnalyzerGPIB.setText(_translate("LimiterTest", "18"))
        self.b_exit.setText(_translate("LimiterTest", "Exit"))
        self.b_startTest.setText(_translate("LimiterTest", "Start Test"))
        self.menuLimiter_Test_Gui.setTitle(_translate("LimiterTest", "File"))
        self.menuAbout.setTitle(_translate("LimiterTest", "About"))
        self.actionAbout_Limiter_Test_Gui.setText(_translate("LimiterTest", "About Limiter Test Gui"))
        self.actionSave_Settings.setText(_translate("LimiterTest", "Save Settings"))
        self.actionExit.setText(_translate("LimiterTest", "Exit"))
