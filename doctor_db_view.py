from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

class Ui_Form12(object):
    def setupUi(self, Form12):
        Form12.setObjectName("Form12")
        Form12.resize(800, 600)

        self.background_label = QtWidgets.QLabel(Form12)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background_label.setPixmap(QtGui.QPixmap("888.jpeg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        self.label_2 = QtWidgets.QLabel(Form12)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(198,44,126)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.tableWidget = QtWidgets.QTableWidget(Form12)
        self.tableWidget.setGeometry(QtCore.QRect(100, 180, 650, 350))
        self.tableWidget.setObjectName("tableWidget")

        self.pushButton = QtWidgets.QPushButton(Form12)
        self.pushButton.setGeometry(QtCore.QRect(170, 100, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:30px;\n"
                                      "background-color: rgb(88,202,250);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.overall)

        self.exitButton = QtWidgets.QPushButton(Form12)
        self.exitButton.setGeometry(QtCore.QRect(240, 540, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("border-radius:30px;\n"
                                      "background-color: rgb(88,202,250);")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(QtWidgets.qApp.quit)

        self.back_button = QtWidgets.QPushButton(Form12)
        self.back_button.setGeometry(QtCore.QRect(550, 540, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("border-radius:30px;\n"
                                       "background-color: rgb(88,202,250);")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("Back")
        self.back_button.clicked.connect(Form12.close)
        self.retranslateUi(Form12)
        QtCore.QMetaObject.connectSlotsByName(Form12)
        Form12.setWindowTitle("Database View")

    def retranslateUi(self, Form12):
        _translate = QtCore.QCoreApplication.translate
        Form12.setWindowTitle(_translate("Form12", "Form"))
        self.pushButton.setText(_translate("Form12", "VIEW"))
        self.label_2.setText(_translate("Form", "DONOR DETAILS"))

    def overall(self):
        try:
            # Clear the table
            self.tableWidget.clear()

            # Connect to the database
            con = sqlite3.connect('organ.db')
            cursor = con.cursor()

            # Execute SELECT query for student table
            cursor.execute("PRAGMA table_info(donor_details)")
            columns = cursor.fetchall()

            # Set column count and headers
            self.tableWidget.setColumnCount(len(columns))
            header_labels = [column[1] for column in columns]
            self.tableWidget.setHorizontalHeaderLabels(header_labels)
            self.tableWidget.setStyleSheet("background-color: transparent;")

            # Execute SELECT query for donor_details table
            cursor.execute("SELECT * FROM donor_details")
            result = cursor.fetchall()

            # Populate the table with data
            if result:
                self.tableWidget.setRowCount(len(result))
                for row_num, row_data in enumerate(result):
                    for col_num, col_data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(col_data))
                        item.setForeground(QtGui.QColor(0,0,0))
                        font = QtGui.QFont()
                        font.setPointSize(18)
                        item.setFont(font)
                        self.tableWidget.setItem(row_num, col_num, item)
            else:
                QtWidgets.QMessageBox.information(None, 'No Records', 'No records found in the table.')

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f"An error occurred: {str(e)}")
        finally:
            cursor.close()
            con.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form12 = QtWidgets.QWidget()
    ui = Ui_Form12()
    ui.setupUi(Form12)
    Form12.show()
    sys.exit(app.exec_())
