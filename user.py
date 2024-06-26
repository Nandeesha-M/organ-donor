# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from patient_log_reg import Ui_Form1234
from donor_login import Ui_Form222
from doctor_login import Ui_Form22


class Ui_Form123(object):
    def setupUi(self, Form123):
        Form123.setObjectName("Form12")
        Form123.resize(800,600)
        self.label = QtWidgets.QLabel(Form123)
        self.label.setGeometry(QtCore.QRect(0, 0, 800,600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("111.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form123)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(198,44,126);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form123)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form123)
        self.label_4.setGeometry(QtCore.QRect(50, 360, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form123)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form123)
        self.label_6.setGeometry(QtCore.QRect(50, 250, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")


        self.pushButton2 = QtWidgets.QPushButton(Form123)
        self.pushButton2.setGeometry(QtCore.QRect(250, 150, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("border-radius:30px;\n"
                                      "background-color: rgb(88,202,250);")
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.patient)

        self.pushButton3 = QtWidgets.QPushButton(Form123)
        self.pushButton3.setGeometry(QtCore.QRect(250, 250, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("border-radius:30px;\n"
                                       "background-color: rgb(88,202,250);")
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.donor)

        self.pushButton4 = QtWidgets.QPushButton(Form123)
        self.pushButton4.setGeometry(QtCore.QRect(250, 350, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("border-radius:30px;\n"
                                       "background-color: rgb(88,202,250);")
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.clicked.connect(self.doctor)

        self.retranslateUi(Form123)
        QtCore.QMetaObject.connectSlotsByName(Form123)
        Form123.setWindowTitle("Select Users")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", " SELECT USERS "))

        # self.pushButton.setText(_translate("Form", "ADMIN"))
        self.pushButton2.setText(_translate("Form", "PATIENT"))
        self.pushButton3.setText(_translate("Form", "DONOR"))
        self.pushButton4.setText(_translate("Form", "DOCTOR"))

    def doctor(self):
        print("hello")
        self.Form22 = QtWidgets.QMainWindow()
        self.Ui = Ui_Form22()
        self.Ui.setupUi(self.Form22)
        self.Form22.show()

    def donor(self):
        print("hello")

        self.Form222= QtWidgets.QMainWindow()
        self.Ui = Ui_Form222()
        self.Ui.setupUi(self.Form222)
        self.Form222.show()

    def patient(self):
        print("hello")

        self.Form1234= QtWidgets.QMainWindow()
        self.Ui = Ui_Form1234()
        self.Ui.setupUi(self.Form1234)
        self.Form1234.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form123 = QtWidgets.QWidget()
    ui = Ui_Form123()
    ui.setupUi(Form123)
    Form123.show()
    sys.exit(app.exec_())
