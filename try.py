
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QClipboard
import sys


class Main(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        #
        # self.mainFrame = QFrame()
        # self.mainFrame.setGeometry(0, 0, 50, 50)

        self.radio1 = QRadioButton()
        self.radio1.setText("amir")


        self.radio2 = QRadioButton()
        self.radio2.setText("hosein")

        self.btn = QPushButton()
        self.btn.clicked.connect(self.printer)

        # self.setCentralWidget(self.mainFrame)

        self.radio2.clicked.connect(self.printer)

        qvb = QVBoxLayout()
        qvb.addWidget(self.radio1)
        qvb.addWidget(self.radio2)
        qvb.addWidget(self.btn)

        self.setLayout(qvb)
        self.show()

    def printer(self):
        value = self.radio2.isChecked()
        # print(QClipboard.setText("amir"))
        clipboard = QGuiApplication.clipboard()
        msg = QMessageBox()
        msg.setText("hello")
        msg.setIcon(0)
        retval = msg.exec_()
        msg = QMessageBox()
        msg.setText("hello")
        msg.setIcon(2)
        retval = msg.exec_()
        msg = QMessageBox()
        msg.setText("hello")
        msg.setIcon(3)
        retval = msg.exec_()
        msg = QMessageBox()
        msg.setText("hello")
        msg.setIcon(4)
        retval = msg.exec_()
        msg = QMessageBox()
        msg.setText("hello")
        msg.setIcon(5)
        retval = msg.exec_()
        retval = msg.exec_()
        # clipboard.setText("amir")
        return print(self.radio2.isChecked(), clipboard.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()

    sys.exit(app.exec_())


# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QVBoxLayout()
#         self.edit1 = QTextEdit()
#         hbox.addWidget(self.edit1)
#         self.btn1 = QPushButton("Copy")
#         hbox.addWidget(self.btn1)
#         self.edit2 = QTextEdit()
#         self.btn2 = QPushButton("Paste")
#         hbox.addWidget(self.edit2)
#         hbox.addWidget(self.btn2)
#         self.btn1.clicked.connect(self.copytext)
#         self.btn2.clicked.connect(self.pastetext)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Clipboard')
#         self.show()
#
#     def copytext(self):
#         # clipboard.setText(self.edit1.copy())
#         self.edit1.copy()
#         print(clipboard.text())
#
#         msg = QMessageBox()
#         msg.setText(clipboard.text() + " copied on clipboard")
#         msg.exec_()
#
#     def pastetext(self):
#         self.edit2.setText(clipboard.text())
#
#
# app = QApplication(sys.argv)
# clipboard = app.clipboard()
# ex = Example()
# ex.setWindowTitle("clipboard Example")
# sys.exit(app.exec_())
