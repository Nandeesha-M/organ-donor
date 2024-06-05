from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

class Ui_DonorDetailsForm(object):
    def setupUi(self, DonorDetailsForm):
        self.DonorDetailsForm = DonorDetailsForm
        DonorDetailsForm.setObjectName("DonorDetailsForm")
        DonorDetailsForm.resize(800, 650)

        # Background label
        self.background_label = QtWidgets.QLabel(DonorDetailsForm)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 650))
        self.background_label.setPixmap(QtGui.QPixmap("444.jpeg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        # Title label
        self.label_2 = QtWidgets.QLabel(DonorDetailsForm)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)  # Set font bold
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(198,44,126);")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("DONOR DETAILS")

        # Name label and line edit
        self.name_label = QtWidgets.QLabel(DonorDetailsForm)
        self.name_label.setGeometry(QtCore.QRect(100, 150, 91, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.name_label.setFont(font)  # Apply font to label
        self.name_label.setObjectName("name_label")
        self.name_label.setText("Name:")
        self.name_lineEdit = QtWidgets.QLineEdit(DonorDetailsForm)
        self.name_lineEdit.setGeometry(QtCore.QRect(320, 150, 191, 31))
        self.name_lineEdit.setObjectName("name_lineEdit")

        # Gender label and combo box
        self.gender_label = QtWidgets.QLabel(DonorDetailsForm)
        self.gender_label.setGeometry(QtCore.QRect(100, 200, 191, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.gender_label.setFont(font)  # Apply font to label
        self.gender_label.setObjectName("gender_label")
        self.gender_label.setText("Gender:")
        self.gender_comboBox = QtWidgets.QComboBox(DonorDetailsForm)
        self.gender_comboBox.setGeometry(QtCore.QRect(320, 200, 191, 31))
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItems(["Male", "Female", "Others"])

        # Blood group label and combo box
        self.blood_group_label = QtWidgets.QLabel(DonorDetailsForm)
        self.blood_group_label.setGeometry(QtCore.QRect(100, 250, 291, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.blood_group_label.setFont(font)  # Apply font to label
        self.blood_group_label.setObjectName("blood_group_label")
        self.blood_group_label.setText("Blood Group:")
        self.blood_group_comboBox = QtWidgets.QComboBox(DonorDetailsForm)
        self.blood_group_comboBox.setGeometry(QtCore.QRect(320, 250, 191, 31))
        self.blood_group_comboBox.setObjectName("blood_group_comboBox")
        self.blood_group_comboBox.addItem("")
        self.blood_group_comboBox.addItems(["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])

        # Address label and text edit
        self.address_label = QtWidgets.QLabel(DonorDetailsForm)
        self.address_label.setGeometry(QtCore.QRect(100, 300, 191, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.address_label.setFont(font)  # Apply font to label
        self.address_label.setObjectName("address_label")
        self.address_label.setText("Address:")
        self.address_textEdit = QtWidgets.QTextEdit(DonorDetailsForm)
        self.address_textEdit.setGeometry(QtCore.QRect(320, 300, 191, 61))
        self.address_textEdit.setObjectName("address_textEdit")

        # Age label and spin box
        self.age_label = QtWidgets.QLabel(DonorDetailsForm)
        self.age_label.setGeometry(QtCore.QRect(100, 380, 91, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.age_label.setFont(font)  # Apply font to label
        self.age_label.setObjectName("age_label")
        self.age_label.setText("Age:")
        self.age_spinBox = QtWidgets.QSpinBox(DonorDetailsForm)
        self.age_spinBox.setGeometry(QtCore.QRect(320, 380, 191, 31))
        self.age_spinBox.setObjectName("age_spinBox")

        # Mobile number label and line edit
        self.mobile_number_label = QtWidgets.QLabel(DonorDetailsForm)
        self.mobile_number_label.setGeometry(QtCore.QRect(100, 430, 221, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.mobile_number_label.setFont(font)  # Apply font to label
        self.mobile_number_label.setObjectName("mobile_number_label")
        self.mobile_number_label.setText("Mobile Number:")
        self.mobile_number_lineEdit = QtWidgets.QLineEdit(DonorDetailsForm)
        self.mobile_number_lineEdit.setGeometry(QtCore.QRect(320, 430, 191, 31))
        self.mobile_number_lineEdit.setObjectName("mobile_number_lineEdit")

        # Email ID label and line edit
        self.email_label = QtWidgets.QLabel(DonorDetailsForm)
        self.email_label.setGeometry(QtCore.QRect(100, 480, 191, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.email_label.setFont(font)  # Apply font to label
        self.email_label.setObjectName("email_label")
        self.email_label.setText("Email ID:")
        self.email_lineEdit = QtWidgets.QLineEdit(DonorDetailsForm)
        self.email_lineEdit.setGeometry(QtCore.QRect(320, 480, 191, 31))
        self.email_lineEdit.setObjectName("email_lineEdit")

        # Organ label and line edit
        self.organ_label = QtWidgets.QLabel(DonorDetailsForm)
        self.organ_label.setGeometry(QtCore.QRect(100, 530, 221, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.organ_label.setFont(font)  # Apply font to label
        self.organ_label.setObjectName("organ_label")
        self.organ_label.setText("Donating Organ:")
        self.organ_lineEdit = QtWidgets.QLineEdit(DonorDetailsForm)
        self.organ_lineEdit.setGeometry(QtCore.QRect(320, 530, 191, 31))
        self.organ_lineEdit.setObjectName("organ_lineEdit")

        # Date label and date-time edit
        self.date_label = QtWidgets.QLabel(DonorDetailsForm)
        self.date_label.setGeometry(QtCore.QRect(100, 580, 91, 31))
        font = QtGui.QFont()  # Set font
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font bold
        self.date_label.setFont(font)  # Apply font to label
        self.date_label.setObjectName("date_label")
        self.date_label.setText("Date:")
        self.date_edit = QtWidgets.QDateTimeEdit(DonorDetailsForm)
        self.date_edit.setGeometry(QtCore.QRect(320, 580, 191, 31))
        self.date_edit.setDateTime(QtCore.QDateTime.currentDateTime())  # Set current date and time
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd-MM-yyyy")  # Set date display format

        # Submit button
        self.submit_button = QtWidgets.QPushButton(DonorDetailsForm)
        self.submit_button.setGeometry(QtCore.QRect(550, 250, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("border-radius:30px;\n"
                                         "background-color: rgb(88,202,250);")
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.saveData)

        # Exit button
        self.exit_button = QtWidgets.QPushButton(DonorDetailsForm)
        self.exit_button.setGeometry(QtCore.QRect(550, 450, 191, 61))
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

        self.retranslateUi(DonorDetailsForm)
        QtCore.QMetaObject.connectSlotsByName(DonorDetailsForm)

    def retranslateUi(self, DonorDetailsForm):
        _translate = QtCore.QCoreApplication.translate
        DonorDetailsForm.setWindowTitle(_translate("DonorDetailsForm", "Donor Details"))
        self.blood_group_comboBox.setItemText(0, _translate("DonorDetailsForm", "Select Blood Group"))
        self.gender_comboBox.setItemText(0, _translate("DonorDetailsForm", "Select Gender"))

    def saveData(self):
        name = self.name_lineEdit.text().strip()
        gender = self.gender_comboBox.currentText().strip()
        blood_group = self.blood_group_comboBox.currentText().strip()
        address = self.address_textEdit.toPlainText().strip()
        age = self.age_spinBox.value()
        mobile_number = self.mobile_number_lineEdit.text().strip()
        email = self.email_lineEdit.text().strip()
        organ = self.organ_lineEdit.text().strip()
        date = self.date_edit.dateTime().toString("dd-MM-yyyy")

        if not (name and gender and blood_group and address and mobile_number and email and organ and date):
            QtWidgets.QMessageBox.critical(None, 'Error', 'Please fill in all the details.')
            return

        if not mobile_number.isdigit() or len(mobile_number) != 10:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Mobile number should be a 10-digit number.')
            return

        try:
            con = sqlite3.connect('organ.db')
            cursor = con.cursor()

            cursor.execute("INSERT INTO donor_details (Name, Gender, 'Blood Group', Address, Age, 'Mobile Number', 'email ID', 'Donating organ', Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (name, gender, blood_group, address, age, mobile_number, email, organ, date))
            con.commit()
            QtWidgets.QMessageBox.information(None, 'Success', 'Details saved successfully.')
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            con.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DonorDetailsForm = QtWidgets.QWidget()
    ui = Ui_DonorDetailsForm()
    ui.setupUi(DonorDetailsForm)
    DonorDetailsForm.show()
    sys.exit(app.exec_())
