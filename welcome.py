

from PyQt5 import QtCore, QtGui, QtWidgets
from user import Ui_Form123

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 800,600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("222.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 871, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        # self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("color: rgb(255,255,255);background-color: rgb(233,23,51);")
        self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(Form)
        # self.label_3.setGeometry(QtCore.QRect(0, 50, 811, 51))
        # font = QtGui.QFont()
        # font.setPointSize(26)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_3.setFont(font)
        # self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(233,23,51);")
        # self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 260, 1711, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 250, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 520, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(88,202,250);")
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.setStyleSheet("border-radius: 20px;\n"
        #                               "background-color: rgb(225,200,200);")
        self.pushButton.clicked.connect(self.next_page)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle("Welcome")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", " ORGAN DONATION MANAGEMENT SYSTEM"))
        # self.label_3.setText(_translate("Form", ""))


        self.pushButton.setText(_translate("Form", "NEXT"))

    def next_page(self):
        print("hello")


        self.Form123 = QtWidgets.QMainWindow()
        self.Ui = Ui_Form123()
        self.Ui.setupUi(self.Form123)
        self.Form123.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
