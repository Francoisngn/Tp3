from re import S
from PyQt5.QtWidgets import (
    
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys
import webbrowser

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)   #modifie la taille 

        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(100,1)
        self.text = QLineEdit(self)
        self.text.move(10, 30)

        self.label2 = QLabel("Enter your hostname:", self)
        self.label2.move(100,60)
        self.text = QLineEdit(self)
        self.text.move(100, 100)

        self.label3 = QLabel("Please enter your IP:", self)
        self.label3.move(100,50)
        self.text13 = QLineEdit(self)
        self.text23.move(100, 75)      

    
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)
        self.button = QPushButton("Send", self)
        self.button.move(100, 250)

        self.button.clicked.connect(self.on_click) #to go  to the page with coordonates just
        self.button.pressed.connect(self.on_click) #permet davoir le sms derreur si les coordonnes sont fausses

        self.show() # permet d afficher la fenetre

    def on_click(self):
        hostname = self.text.text()
        api_key = self.text2.text()
        ip = self.text13.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")

        else:
            res = self.__query(hostname, ip, api_key_)
            if res:
                self.label2.setText("Longitude : %s \n Latitude: %s" % (res["Longitude"], res["Latitude"]))

                self.label2.adjustSize()
                self.show()
                 url1 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"], res["Longitude"])
                webbrowser.open_new_tab(url1)

    def __query(self, hostname):
        url = "http://%s/ip/%s?key=%s" % (hostname, ip, api_key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()

    # end :)
