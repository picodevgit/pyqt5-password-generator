from login import Ui_MainWindow
from panel import Ui_panel
import databaseManagement
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtCore import*
from PyQt5 import QtGui
from PyQt5.QtGui import*
from generator import Generate
from messagebox import Messages


class Panel_opener(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.ui = Ui_panel()

        self.ui.setupUi(self)
        # print("before")
        self.accountList = databaseManagement.Database().get_account()
        self.username = self.accountList[0]
        self.password = self.accountList[1]
        self.generated_password = ""
        # print("after")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.generator_button.clicked.connect(self.output)

        self.ui.gray_heart.clicked.connect(self.add_data)
        # self.ui.red_heart.clicked.connect(self.remove_data)

        self.ui.data.clicked.connect(self.show_data)

        self.ui.home.clicked.connect(self.backHome)

        self.ui.trash.clicked.connect(self.trash_data)


        self.oldPos = ""


    def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
        # print("come")
        self.oldPos = evt.globalPos()
        # self.mouseMoveEvent(self.oldPos)

    def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
        # print("move")
        delta = QPoint(evt.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())

        self.oldPos = evt.globalPos()

    def output(self):
        try:
            length = int(self.ui.password_length.text())
            # print(self.ui.letter.isChecked())
            clipboard = QGuiApplication.clipboard()
            if self.ui.letter.isChecked() == True:
                # print("letters")
                self.generated_password = Generate(length).word_maker()
                self.ui.password.setText(self.generated_password)
                clipboard.setText(self.generated_password)

            elif self.ui.number.isChecked() == True:
                # print("number")
                self.generated_password = Generate(length).number_maker()
                self.ui.password.setText(self.generated_password)
                clipboard.setText(self.generated_password)

            elif self.ui.letter_number.isChecked() == True:
                # print("letter_number")
                self.generated_password = Generate(length).letter_number_maker()
                self.ui.password.setText(self.generated_password)
                clipboard.setText(self.generated_password)

            else:
                print("error")
        except:
            text = "لطفا به عنوان طول کد یک عدد را به درستی وارد کنید.\n" \
                   "و نوع کد خروجی را با زدن یکی از گزینه ها مشخص کنید."
            self.ui.password_length.setText("")
            self.ui.password.setText("")
            return Messages(text).critical()

    def add_data(self):
        return databaseManagement.Database().add_password_data(self.generated_password) # QGuiApplication.clipboard().text()

    def backHome(self):
        # print("come")
        return self.ui.pageFrame2.hide()

    def show_data(self):
        self.ui.pageFrame2.show()
        # print("database show come")
        return self.ui.show_data_textEdit.setText(databaseManagement.Database().show_data())

    def trash_data(self):
        try:
            databaseManagement.Database().trash()
            text = "%s عزیز کل حافظه ی مربوط به حساب کاربری شما و پسورد های قبلی پاک شده است"%self.username
            self.ui.password_length.setText("")
            self.ui.password.setText("")
            Messages(text).critical()
        except:
            text = "%s عزیز متاسفانه هیچ حافظه ای در حساب کاربری شما برای پاک کردن یافت نشد "%self.username
            self.ui.password_length.setText("")
            self.ui.password.setText("")
            Messages(text).critical()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.login_button.clicked.connect(self.panelOpener)
            
        self.show()
        self.oldPos = ""

    def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
        # print("come")
        self.oldPos = evt.globalPos()
        # self.mouseMoveEvent(self.oldPos)

    def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
        # print("move")
        delta = QPoint(evt.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())

        self.oldPos = evt.globalPos()


    def panelOpener(self):
        try:
            import sys
            # print("come")
            username = self.ui.username_line.text()
            password = self.ui.password_line.text()
            if len(password) >= 4 and len(username) >=4 :
                password = int(password)
                # print(type(password))
            else:
                text = "نام کاربری و رمز ورودی نادرست است." \
                       "لطفا دوباره انتحان کنید.\nتوجه شود که رمز عبور و نام کاربری باید حداقل دارای چهار حرف بدون فاصله باشد."
                self.ui.username_line.setText("")
                self.ui.password_line.setText("")
                return Messages(text).critical()

            solution = ""

            validate = databaseManagement.Database(username, password, solution).validate()
            if validate == "correct":
                # print("go to open panel")
                self.panel = Panel_opener()
                self.panel.show()
                return self.close()

            elif validate == "new":
                self.panel = Panel_opener()
                self.panel.show()
                return self.close()

            elif validate == "name":
                text = "نام کاربری نادرست است." \
                       "لطفا دوباره انتحان کنید.\nتوجه شود که نام کاربری باید حداقل دارای چهار حرف باشد"
                self.ui.username_line.setText("")
                self.ui.password_line.setText("")
                return Messages(text).critical()

            elif validate == "password":
                text = "رمز ورودی نادرست است." \
                       "لطفا دوباره انتحان کنید.\nتوجه شود که رمز عبور باید حداقل دارای چهار حرف باشد"
                self.ui.username_line.setText("")
                self.ui.password_line.setText("")
                return Messages(text).critical()

            elif validate == "both":
                text = "نام کاربری و رمز ورودی نادرست است." \
                       "لطفا دوباره انتحان کنید.\nتوجه شود که رمز عبور و نام کاربری باید حداقل دارای چهار حرف بدون فاصله باشد."
                self.ui.username_line.setText("")
                self.ui.password_line.setText("")
                return Messages(text).critical()
        except:
            text = "نام کاربری و رمز ورودی نادرست است." \
                   "لطفا دوباره انتحان کنید.\nتوجه شود که رمز عبور و نام کاربری باید حداقل دارای چهار حرف بدون فاصله باشد."
            self.ui.username_line.setText("")
            self.ui.password_line.setText("")
            return Messages(text).critical()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    root = RootMain()

    sys.exit(app.exec_())