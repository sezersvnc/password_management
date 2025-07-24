
import sys
from PyQt5.QtWidgets import(QPushButton, QLabel, QVBoxLayout, QWidget, QApplication, QInputDialog, QLineEdit,QMessageBox)
from PyQt5.QtGui import QIcon,QPalette,QImage,QBrush
from PyQt5.QtCore import Qt
from operation import veri_yukle, sifre_arama, sifre_uretim, sifre_onerisi

file_path="kayit2.json"
class MainWindow(QWidget):
    belge = veri_yukle()
    def __init__(self):
        super().__init__()
        self.password_suggestion=QPushButton("🔥 password_suggestion",self)
        self.search_password=QPushButton("🔎 Search password",self)
        self.add_new_password=QPushButton("➕ Add new password",self)
        self.quit=QPushButton("🚪 Quit",self)
        self.icon=QIcon()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Management")
        self.setGeometry(300, 300, 450, 250)
        vbox = QVBoxLayout()
        vbox.addWidget(self.search_password)
        vbox.addWidget(self.add_new_password)
        vbox.addWidget(self.password_suggestion)
        vbox.addWidget(self.quit)
        self.setLayout(vbox)
        self.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                font-family: calibri;
                margin: 30px;
                
            }
            QPushButton:hover {
                background-color: hsl(177, 100%, 48%);
            }
            QMessageBox {
                font-size: 30px;
                font-family: calibri;
                
            }
        """)
        self.search_password.clicked.connect(self.searchpassword)
        self.add_new_password.clicked.connect(self.addnewpassword)
        self.password_suggestion.clicked.connect(self.passwordsuggestion)
        self.quit.clicked.connect(self.quit1)
    def searchpassword(self):
        uygulama,ok=QInputDialog.getText(self,"Search application","please enter your the name of the app")
        sonuc = sifre_arama(MainWindow.belge,uygulama)
        if uygulama and ok:
            sonuc = sifre_arama(MainWindow.belge, uygulama)
            if sonuc:
                QMessageBox.information(self, "Sonuç", f"{uygulama} = username and password:{sonuc}")
            else:
                QMessageBox.warning(self, "Bulunamadı", f"No record found about {uygulama} .")
    def addnewpassword(self):
        uygulama,enter = QInputDialog.getText(self,"add application","please enter new application name")
        if uygulama and enter:
            username,enter2 = QInputDialog.getText(self,"username","please enter new username")
            if username and enter2:
                password,enter3 = QInputDialog.getText(self,"password","please enter new password")
                if password and enter3:
                    sonuc = sifre_uretim(MainWindow.belge,uygulama,username,password)
    def passwordsuggestion(self):
        sonuc= sifre_onerisi(uzunluk=9)
        QMessageBox.information(self,f"password",f"onerilen sifre= {sonuc}")

    def quit1(self):
        exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())