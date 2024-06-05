from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

class Ui_DoctorUpdateForm(object):
    def setupUi(self, DoctorUpdateForm):
        DoctorUpdateForm.setObjectName("DoctorUpdateForm")
        DoctorUpdateForm.resize(800, 600)

        # Background label
        self.background_label = QtWidgets.QLabel(DoctorUpdateForm)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background_label.setPixmap(QtGui.QPixmap("88.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        # Title label
        self.label_2 = QtWidgets.QLabel(DoctorUpdateForm)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(198,44,126);")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("ORGAN DETAILS")

        # Blood group label and combo box
        self.blood_group_label = QtWidgets.QLabel(DoctorUpdateForm)
        self.blood_group_label.setGeometry(QtCore.QRect(200, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.blood_group_label.setFont(font)
        self.blood_group_label.setObjectName("blood_group_label")
        self.blood_group_label.setText("Blood Group:")
        self.blood_group_comboBox = QtWidgets.QComboBox(DoctorUpdateForm)
        self.blood_group_comboBox.setGeometry(QtCore.QRect(450, 150, 191, 31))
        self.blood_group_comboBox.setObjectName("blood_group_comboBox")
        self.blood_group_comboBox.addItems(["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])

        # Organ name label and line edit
        self.organ_name_label = QtWidgets.QLabel(DoctorUpdateForm)
        self.organ_name_label.setGeometry(QtCore.QRect(200, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.organ_name_label.setFont(font)
        self.organ_name_label.setObjectName("organ_name_label")
        self.organ_name_label.setText("Organ Name:")
        self.organ_name_lineEdit = QtWidgets.QLineEdit(DoctorUpdateForm)
        self.organ_name_lineEdit.setGeometry(QtCore.QRect(450, 200, 191, 31))
        self.organ_name_lineEdit.setObjectName("organ_name_lineEdit")

        # Date label and date-time edit
        self.date_label = QtWidgets.QLabel(DoctorUpdateForm)
        self.date_label.setGeometry(QtCore.QRect(200, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.date_label.setText("Date:")
        self.date_edit = QtWidgets.QDateEdit(DoctorUpdateForm)
        self.date_edit.setGeometry(QtCore.QRect(450, 250, 191, 31))
        self.date_edit.setObjectName("date_edit")
        self.date_edit.setDate(QtCore.QDate(2024, 1, 1))  # Set initial date
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd-MM-yyyy")  # Set date display format

        # Time label and time edit
        self.time_label = QtWidgets.QLabel(DoctorUpdateForm)
        self.time_label.setGeometry(QtCore.QRect(200, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.time_label.setText("Time:")
        self.time_edit = QtWidgets.QTimeEdit(DoctorUpdateForm)
        self.time_edit.setGeometry(QtCore.QRect(450, 300, 191, 31))
        self.time_edit.setObjectName("time_edit")
        self.time_edit.setDisplayFormat("h  h:mm AP")  # Set time display format

        # Submit button
        self.submit_button = QtWidgets.QPushButton(DoctorUpdateForm)
        self.submit_button.setGeometry(QtCore.QRect(350, 520, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("border-radius:30px;\n"
                                         "background-color: rgb(88,202,250);")
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.saveData)  # Connect the button to saveData method

        self.back_button = QtWidgets.QPushButton(DoctorUpdateForm)
        self.back_button.setGeometry(QtCore.QRect(150, 520, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("border-radius:30px;\n"
                                       "background-color: rgb(88,202,250);")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("Back")
        self.back_button.clicked.connect(DoctorUpdateForm.close)
        # Exit button
        self.exit_button = QtWidgets.QPushButton(DoctorUpdateForm)
        self.exit_button.setGeometry(QtCore.QRect(550, 520, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("border-radius:30px;\n"
                                       "background-color: rgb(88,202,250);")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("Exit")
        self.exit_button.clicked.connect(QtWidgets.qApp.quit)

        self.retranslateUi(DoctorUpdateForm)
        QtCore.QMetaObject.connectSlotsByName(DoctorUpdateForm)

    def retranslateUi(self, DoctorUpdateForm):
        _translate = QtCore.QCoreApplication.translate
        DoctorUpdateForm.setWindowTitle(_translate("DoctorUpdateForm", "Doctor Update"))
        # Add translation for labels if needed
        self.blood_group_comboBox.setItemText(0, _translate("DoctorUpdateForm", "Select Blood Group"))

    def saveData(self):
        blood_group = self.blood_group_comboBox.currentText()
        organ_name = self.organ_name_lineEdit.text()
        date = self.date_edit.date().toString("dd-MM-yyyy")
        time = self.time_edit.time().toString("hh:mm AP")

        if not (blood_group and organ_name and date and time):
            QtWidgets.QMessageBox.critical(None, 'Error', 'Please fill in all the details.')
            return

        try:
            con = sqlite3.connect('organ.db')
            cursor = con.cursor()

            cursor.execute("INSERT INTO doctor_update ('Blood group', 'Organ Name', 'Date', 'Time') VALUES (?, ?, ?, ?)",
                           (blood_group, organ_name, date, time))
            con.commit()
            QtWidgets.QMessageBox.information(None, 'Success', 'Details saved successfully.')
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            con.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DoctorUpdateForm = QtWidgets.QWidget()
    ui = Ui_DoctorUpdateForm()
    ui.setupUi(DoctorUpdateForm)
    DoctorUpdateForm.show()
    sys.exit(app.exec_())
