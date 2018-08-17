# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cnc_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from pySerial import *
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rc_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rc_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from serial import *
from rc_constants import *
from pyRc import *

globalCommand = [0,0,0,0,0,50,0,0]

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RcMule(object):
    ser = Serial()
    mysignal = pyqtSignal(int, list)
    update = pyqtSignal()

    def setupUi(self, RcMule):
        self.beep=  pyqtSignal(int)

        RcMule.setObjectName(_fromUtf8("MilSam RC Mule"))
        RcMule.resize(604, 676)
        self.rudderSlider = QtGui.QSlider(RcMule)
        self.rudderSlider.setGeometry(QtCore.QRect(50, 90, 160, 22))
        self.rudderSlider.setProperty("value", 50)
        self.rudderSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rudderSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.rudderSlider.setObjectName(_fromUtf8("rudderSlider"))
        self.pitchSlider = QtGui.QSlider(RcMule)
        self.pitchSlider.setGeometry(QtCore.QRect(280, 10, 22, 160))
        self.pitchSlider.setProperty("value", 50)
        self.pitchSlider.setOrientation(QtCore.Qt.Vertical)
        self.pitchSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.pitchSlider.setObjectName(_fromUtf8("pitchSlider"))
        self.velocityDial = QtGui.QDial(RcMule)
        self.velocityDial.setGeometry(QtCore.QRect(460, 120, 50, 64))
        self.velocityDial.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.velocityDial.setWrapping(False)
        self.velocityDial.setNotchesVisible(True)
        self.velocityDial.setObjectName(_fromUtf8("velocityDial"))
        self.horizontalLayoutWidget = QtGui.QWidget(RcMule)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 551, 69))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.VelocityLabel_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.VelocityLabel_3.setObjectName(_fromUtf8("VelocityLabel_3"))
        self.horizontalLayout.addWidget(self.VelocityLabel_3)
        self.VelocityLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.VelocityLabel_2.setObjectName(_fromUtf8("VelocityLabel_2"))
        self.horizontalLayout.addWidget(self.VelocityLabel_2)
        self.VelocityLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.VelocityLabel.setObjectName(_fromUtf8("VelocityLabel"))
        self.horizontalLayout.addWidget(self.VelocityLabel)
        self.formLayoutWidget = QtGui.QWidget(RcMule)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 310, 231, 101))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.packetLossSb = QtGui.QSpinBox(self.formLayoutWidget)
        self.packetLossSb.setEnabled(True)
        self.packetLossSb.setObjectName(_fromUtf8("packetLossSb"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.packetLossSb)
        self.PacketLossGenLabel = QtGui.QLabel(self.formLayoutWidget)
        self.PacketLossGenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PacketLossGenLabel.setObjectName(_fromUtf8("PacketLossGenLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.PacketLossGenLabel)
        self.btiErrorSb = QtGui.QSpinBox(self.formLayoutWidget)
        self.btiErrorSb.setEnabled(True)
        self.btiErrorSb.setObjectName(_fromUtf8("btiErrorSb"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.btiErrorSb)
        self.BitErrorGenError = QtGui.QLabel(self.formLayoutWidget)
        self.BitErrorGenError.setAlignment(QtCore.Qt.AlignCenter)
        self.BitErrorGenError.setObjectName(_fromUtf8("BitErrorGenError"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.BitErrorGenError)
        self.updateRateSb = QtGui.QSpinBox(self.formLayoutWidget)
        self.updateRateSb.setEnabled(True)
        self.updateRateSb.setMaximum(999)
        self.updateRateSb.setObjectName(_fromUtf8("updateRateSb"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.updateRateSb)
        self.UpdateRateGenLabel = QtGui.QLabel(self.formLayoutWidget)
        self.UpdateRateGenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdateRateGenLabel.setObjectName(_fromUtf8("UpdateRateGenLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.UpdateRateGenLabel)
        self.VelocityLCD = QtGui.QLCDNumber(RcMule)
        self.VelocityLCD.setGeometry(QtCore.QRect(350, 20, 158, 78))
        self.VelocityLCD.setFrameShape(QtGui.QFrame.NoFrame)
        self.VelocityLCD.setFrameShadow(QtGui.QFrame.Plain)
        self.VelocityLCD.setObjectName(_fromUtf8("VelocityLCD"))
        self.formLayoutWidget_2 = QtGui.QWidget(RcMule)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 410, 183, 112))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.packetLoss = QtGui.QLabel(self.formLayoutWidget_2)
        self.packetLoss.setObjectName(_fromUtf8("packetLoss"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.packetLoss)
        self.PacketLossSalveLcd = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.PacketLossSalveLcd.setObjectName(_fromUtf8("PacketLossSalveLcd"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.PacketLossSalveLcd)
        self.RssiHost = QtGui.QLabel(self.formLayoutWidget_2)
        self.RssiHost.setObjectName(_fromUtf8("RssiHost"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.RssiHost)
        self.RssiHostLcd = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.RssiHostLcd.setObjectName(_fromUtf8("RssiHostLcd"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.RssiHostLcd)
        self.RssiSlave = QtGui.QLabel(self.formLayoutWidget_2)
        self.RssiSlave.setObjectName(_fromUtf8("RssiSlave"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.RssiSlave)
        self.RssiSlaveLcd = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.RssiSlaveLcd.setObjectName(_fromUtf8("RssiSlaveLcd"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.RssiSlaveLcd)
        self.label_7 = QtGui.QLabel(RcMule)
        self.label_7.setGeometry(QtCore.QRect(40, 270, 391, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayoutWidget = QtGui.QWidget(RcMule)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(229, 410, 331, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PacketLossLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.PacketLossLabel.setObjectName(_fromUtf8("PacketLossLabel"))
        self.verticalLayout.addWidget(self.PacketLossLabel)
        self.RssiHostLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.RssiHostLabel.setObjectName(_fromUtf8("RssiHostLabel"))
        self.verticalLayout.addWidget(self.RssiHostLabel)
        self.RssiSlaveLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.RssiSlaveLabel.setObjectName(_fromUtf8("RssiSlaveLabel"))
        self.verticalLayout.addWidget(self.RssiSlaveLabel)
        self.gridLayoutWidget_5 = QtGui.QWidget(RcMule)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 540, 441, 71))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.connectionLabel = QtGui.QLabel(self.gridLayoutWidget_5)
        self.connectionLabel.setObjectName(_fromUtf8("connectionLabel"))
        self.gridLayout_6.addWidget(self.connectionLabel, 1, 3, 1, 1)
        self.comPb = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.comPb.setObjectName(_fromUtf8("comPb"))
        self.gridLayout_6.addWidget(self.comPb, 1, 2, 1, 1)
        self.comPortSb = QtGui.QSpinBox(self.gridLayoutWidget_5)
        self.comPortSb.setProperty("value", 1)
        self.comPortSb.setObjectName(_fromUtf8("comPortSb"))
        self.gridLayout_6.addWidget(self.comPortSb, 1, 1, 1, 1)
        self.verticalLayoutWidget_4 = QtGui.QWidget(RcMule)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 590, 141, 72))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_4.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_4.addWidget(self.label_17)

        self.retranslateUi(RcMule)
        QtCore.QMetaObject.connectSlotsByName(RcMule)

    def retranslateUi(self, RcMule):
        RcMule.setWindowTitle(_translate("RcMule", "MilSam RC Mule", None))
        self.VelocityLabel_3.setText(_translate("RcMule", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Roll</span><br/></p></body></html>", None))
        self.VelocityLabel_2.setText(_translate("RcMule", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Pitch</span><br/></p></body></html>", None))
        self.VelocityLabel.setText(_translate("RcMule", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Velocity</span><br/></p></body></html>", None))
        self.PacketLossGenLabel.setText(_translate("RcMule", "Packet Loss (%, Generated)", None))
        self.BitErrorGenError.setText(_translate("RcMule", "Bit Error (%, Generated)", None))
        self.UpdateRateGenLabel.setText(_translate("RcMule", "Upate Rate (Hz. Generated)", None))
        self.packetLoss.setText(_translate("RcMule", "Packet Loss (%, Slave)", None))
        self.RssiHost.setText(_translate("RcMule", "RSSI (dB, Host)", None))
        self.RssiSlave.setText(_translate("RcMule", "RSSI (dB, Slave)", None))
        self.label_7.setText(_translate("RcMule", "Inject communication errors into UART stream and change the update rate", None))
        self.PacketLossLabel.setText(_translate("RcMule", "Packet loss, as reported by slave", None))
        self.RssiHostLabel.setText(_translate("RcMule", "RSSI, as reported by host", None))
        self.RssiSlaveLabel.setText(_translate("RcMule", "RSSI, as reported by slave", None))
        self.connectionLabel.setText(_translate("RcMule", "CONNECTION: NONE", None))
        self.comPb.setText(_translate("RcMule", "COM Connect", None))
        self.label_14.setText(_translate("RcMule", "BUAD RATE: 115200", None))
        self.label_15.setText(_translate("RcMule", "STOP BIT: ONE", None))
        self.label_16.setText(_translate("RcMule", "PARITY: NONE", None))
        self.label_17.setText(_translate("RcMule", "WLEN: 8 bits", None))

        ########################################
        ########################################

        self.get_thread = DownloadThread()

        self.setupSignals(RcMule,self.get_thread)
        self.get_thread.start()

        #RcMule.setFixedSize(614, 246)

        ########################################
        ########################################

    def setupSignals(self,rc_mule,threads):
        #set up signals

        #update values
        self.rudderSlider.valueChanged.connect(self.updateRoll)
        self.pitchSlider.valueChanged.connect(self.updatePitch)
        self.velocityDial.valueChanged.connect(self.updateVelocity)

    def updatePitch(self):
        global globalCommand
        globalCommand[SERVO_0_INDEX] = 60 + self.pitchSlider.value() * 40
        print 60 + self.pitchSlider.value() * 405

    def updateRoll(self):
        global globalCommand
        globalCommand[SERVO_1_INDEX] =   self.rudderSlider.value()

    def updateVelocity(self):
        global globalCommand
        globalCommand[MOTOR_OFFSET] =  self.velocityDial.value()

class DownloadThread(QtCore.QThread):

    poo = [1,2,3,4,5]

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.TimeToSnooz = 30
        self.connect(self, SIGNAL("foo"), self.update)

    def update(self):
        pass

    def run(self):
        global globalCommand
        foo = cmdStruct()

        while True:
            sleep(.009)
            #self.emit(SIGNAL("didSomething"),val)
            foo.updateAndSend(globalCommand,True)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    controllerMule = QtGui.QMainWindow()
    ui = Ui_RcMule()
    ui.setupUi(controllerMule)
    print "never get here"

    controllerMule.show()
    sys.exit(app.exec_())
