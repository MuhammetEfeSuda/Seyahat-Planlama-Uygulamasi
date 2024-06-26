from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 1011, 731))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(85, 255, 0, 255));")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 981, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgba(255, 170, 0, 150); color: white;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 581, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: white; alternate-background-color: rgba(200, 200, 200, 50);")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(7)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        item = QtWidgets.QTableWidgetItem("Ankara - Antalya")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem("Palm Beach Resort")
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem("20000 TL")
        self.tableWidget.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem("İstanbul - Bodrum")
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem("Luxury Hotel & Resort")
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem("25000 TL")
        self.tableWidget.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem("İzmir - Çanakkale")
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem("Nur Pansiyon")
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem("8000 TL")
        self.tableWidget.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem("Bursa - İstanbul")
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem("City Hotel")
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem("10000 TL")
        self.tableWidget.setItem(3, 2, item)

        item = QtWidgets.QTableWidgetItem("İzmir - Muğla")
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem("Resort & Spa")
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem("$180")
        self.tableWidget.setItem(4, 2, item)

        item = QtWidgets.QTableWidgetItem("Eskişehir - İstanbul")
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem("Business Hotel")
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem("18000 tl")
        self.tableWidget.setItem(5, 2, item)

        item = QtWidgets.QTableWidgetItem("Adana - Gaziantep")
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem("Boutique Hotel")
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem("6000 TL")
        self.tableWidget.setItem(6, 2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        # item assignments...
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_Seyahat_Sec = QtWidgets.QPushButton(self.widget)
        self.pushButton_Seyahat_Sec.setGeometry(QtCore.QRect(110, 520, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.pushButton_Seyahat_Sec.setFont(font)
        self.pushButton_Seyahat_Sec.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Seyahat_Sec.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_Seyahat_Sec.setStyleSheet("background-color: rgba(255, 170, 0, 150); color: white; border-radius: 10px;")
        self.pushButton_Seyahat_Sec.setObjectName("pushButton_Seyahat_Sec")
        self.pushButton_Seyahat_Planla = QtWidgets.QPushButton(self.widget)
        self.pushButton_Seyahat_Planla.setGeometry(QtCore.QRect(470, 520, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.pushButton_Seyahat_Planla.setFont(font)
        self.pushButton_Seyahat_Planla.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Seyahat_Planla.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_Seyahat_Planla.setStyleSheet("background-color: rgba(255, 170, 0, 150); color: white; border-radius: 10px;")
        self.pushButton_Seyahat_Planla.setObjectName("pushButton_Seyahat_Planla")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "İKÜ SEYAHAT PLANLAMA UYGULAMASI"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rota Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Konaklama Tesisi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Konaklama Tesisi Fiyatı (Günlük)"))
        self.label_3.setText(_translate("MainWindow", "Hazır Seyahat Rotaları"))
        self.pushButton_Seyahat_Sec.setText(_translate("MainWindow", "Seyahat Seç"))
        self.pushButton_Seyahat_Planla.setText(_translate("MainWindow", "Seyahat Planla"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
