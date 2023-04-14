from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys


from PyQt5.QtCore import*
from PyQt5 import QtGui
from PyQt5.QtGui import*

class Messages:
    def __init__(self, text):
        self.text = text

    def warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(self.text)
        send_message = msg.exec_()

    def critical(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(self.text)
        # msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setAttribute(Qt.WA_TranslucentBackground)
        msg.setStyleSheet("font: 87 12pt 'Arial Black'; border-radius: 10px; color: rgb(12, 255, 12); background-color: rgb(0, 0, 89);")
        msg.exec_()

        def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
            # print("come")
            self.oldPos = evt.globalPos()
            # self.mouseMoveEvent(self.oldPos)


        def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
            # print("move")
            delta = QPoint(evt.globalPos() - self.oldPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())

            self.oldPos = evt.globalPos()


    def information(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.information)
        msg.setText(self.text)
        # msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setAttribute(Qt.WA_TranslucentBackground)
        msg.setStyleSheet("font: 87 12pt 'Arial Black'; border-radius: 10px; color: rgb(12, 255, 12); background-color: rgb(0, 0, 89);")
        msg.exec_()

        def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
            # print("come")
            self.oldPos = evt.globalPos()
            # self.mouseMoveEvent(self.oldPos)


        def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
            # print("move")
            delta = QPoint(evt.globalPos() - self.oldPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())

            self.oldPos = evt.globalPos()

# Messages("hello").critical()
#
# def show_popup():
#     msg = QMessageBox(win)
#     msg.setWindowTitle("Message Box")
#     msg.setText("This is some random text")
#     msg.setIcon(QMessageBox.Question)
#
#     msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
#     msg.setDefaultButton(QMessageBox.Ok)
#
#     msg.setDetailedText("Extra details.....")
#     msg.setInformativeText("This is some extra informative text")
#     x = msg.exec_()
#
#
# application = QApplication(sys.argv)
# win = QMainWindow()
# win.setGeometry(400, 400, 300, 300)
# win.setWindowTitle("CodersLegacy")
#
# button = QtWidgets.QPushButton(win)
# button.setText("A Button")
# button.clicked.connect(show_popup()) # Messages("hello").critical()
# button.move(100, 100)
#
# win.show()
# sys.exit(application.exec_())