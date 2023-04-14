from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_panel(object):
    def setupUi(self, main):
        # print("panel1")
        main.setObjectName("main")
        main.resize(580, 470)
        main.setMinimumSize(QtCore.QSize(570, 455))
        main.setMaximumSize(QtCore.QSize(570, 455))
        self.pageFrame = QtWidgets.QWidget(main)
        self.pageFrame.setStyleSheet("")
        self.pageFrame.setObjectName("pageFrame")
        self.mainFrame = QtWidgets.QFrame(self.pageFrame)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 551, 421))
        self.mainFrame.setStyleSheet("background-color: rgb(0, 0, 89);\n"
                                     "\n"
                                     "border-radius:20px;")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.menu = QtWidgets.QFrame(self.mainFrame)
        self.menu.setGeometry(QtCore.QRect(490, 0, 61, 421))
        self.menu.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.home = QtWidgets.QPushButton(self.menu)
        self.home.setGeometry(QtCore.QRect(10, 70, 41, 41))
        self.home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home.setStyleSheet("border-style: none;\n"
                                "border-radius: 20px;\n"
                                "")
        self.home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home icon 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(45, 45))
        self.home.setObjectName("home")
        self.data = QtWidgets.QPushButton(self.menu)
        self.data.setGeometry(QtCore.QRect(10, 220, 41, 61))
        self.data.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data.setStyleSheet("border-style: none;\n"
                                "border-radius: 20px;")
        self.data.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("database_gray_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.data.setIcon(icon1)
        self.data.setIconSize(QtCore.QSize(45, 45))
        self.data.setObjectName("data")
        self.trash = QtWidgets.QPushButton(self.menu)
        self.trash.setGeometry(QtCore.QRect(0, 300, 61, 61))
        self.trash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trash.setStyleSheet("border-style: none;\n"
                                 "border-radius: 20px;\n"
                                 "filter: opacity(80%);")
        self.trash.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("trash_gray_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trash.setIcon(icon2)
        self.trash.setIconSize(QtCore.QSize(80, 80))
        self.trash.setObjectName("trash")
        self.red_heart = QtWidgets.QPushButton(self.menu)
        self.red_heart.setGeometry(QtCore.QRect(0, 150, 61, 51))
        self.red_heart.setStyleSheet("border-style: none;\n"
                                     "border-radius: 20px;")
        self.red_heart.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("heart red icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_heart.setIcon(icon3)
        self.red_heart.setIconSize(QtCore.QSize(45, 45))
        self.red_heart.setObjectName("red_heart")
        self.gray_heart = QtWidgets.QPushButton(self.menu)
        self.gray_heart.setGeometry(QtCore.QRect(10, 150, 41, 51))
        self.gray_heart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gray_heart.setStyleSheet("border-style: none;\n"
                                      "border-radius: 20px;")
        self.gray_heart.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("heart_gray_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gray_heart.setIcon(icon4)
        self.gray_heart.setIconSize(QtCore.QSize(48, 40))
        self.gray_heart.setObjectName("gray_heart")
        self.flag = QtWidgets.QFrame(self.mainFrame)
        self.flag.setGeometry(QtCore.QRect(0, 0, 551, 41))
        self.flag.setStyleSheet("\n"
                                "background-color: rgb(121, 121, 121);\n"
                                "border-left-button: 0")
        self.flag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.flag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.flag.setObjectName("flag")
        self.program_icon_button = QtWidgets.QPushButton(self.flag)
        self.program_icon_button.setGeometry(QtCore.QRect(3, 0, 41, 41))
        self.program_icon_button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.272727, y2:0.972, stop:0.647727 rgba(255, 255, 255, 0), stop:0.982955 rgba(255, 255, 255, 0));\n"
            "border-style: none;\n"
            "border-radius: 20px;\n"
            "/*background-color: red")
        self.program_icon_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("password_page_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.program_icon_button.setIcon(icon5)
        self.program_icon_button.setIconSize(QtCore.QSize(42, 45))
        self.program_icon_button.setObjectName("program_icon_button")
        self.frame_4 = QtWidgets.QFrame(self.flag)
        self.frame_4.setGeometry(QtCore.QRect(420, 0, 131, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.window_closer = QtWidgets.QPushButton(self.frame_4)
        self.window_closer.setGeometry(QtCore.QRect(100, 10, 21, 23))
        self.window_closer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.window_closer.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: red")
        self.window_closer.setText("")
        self.window_closer.setObjectName("window_closer")
        self.window_minimize = QtWidgets.QPushButton(self.frame_4)
        self.window_minimize.setGeometry(QtCore.QRect(70, 10, 21, 23))
        self.window_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.window_minimize.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                           "border-radius: 10px;")
        self.window_minimize.setText("")
        self.window_minimize.setObjectName("window_minimize")
        self.window_maximize = QtWidgets.QPushButton(self.frame_4)
        self.window_maximize.setGeometry(QtCore.QRect(40, 10, 21, 23))
        self.window_maximize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.window_maximize.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: rgb(0, 255, 0);")
        self.window_maximize.setText("")
        self.window_maximize.setObjectName("window_maximize")
        self.title = QtWidgets.QLabel(self.flag)
        self.title.setGeometry(QtCore.QRect(60, 10, 101, 16))
        self.title.setObjectName("title")
        self.password_label = QtWidgets.QLabel(self.mainFrame)
        self.password_label.setGeometry(QtCore.QRect(410, 340, 51, 41))
        self.password_label.setText("")
        self.password_label.setPixmap(QtGui.QPixmap("key_icon-removebg.png"))
        self.password_label.setScaledContents(True)
        self.password_label.setObjectName("password_label")
        self.length_label = QtWidgets.QLabel(self.mainFrame)
        self.length_label.setGeometry(QtCore.QRect(400, 210, 51, 41))
        self.length_label.setText("")
        self.length_label.setPixmap(QtGui.QPixmap("ruler icon2.png"))
        self.length_label.setScaledContents(True)
        self.length_label.setObjectName("length_label")
        self.generator_button = QtWidgets.QPushButton(self.mainFrame)
        self.generator_button.setGeometry(QtCore.QRect(150, 270, 51, 51))
        self.generator_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generator_button.setStyleSheet("\n"
                                            "border-radius: 25px;")
        self.generator_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("generator button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generator_button.setIcon(icon6)
        self.generator_button.setIconSize(QtCore.QSize(50, 50))
        self.generator_button.setObjectName("generator_button")
        self.password_length = QtWidgets.QLineEdit(self.mainFrame)
        self.password_length.setGeometry(QtCore.QRect(120, 220, 241, 31))
        self.password_length.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                           "border-radius: 15px\n"
                                           "")
        self.password_length.setObjectName("password_length")
        self.password = QtWidgets.QLineEdit(self.mainFrame)
        self.password.textChanged[str].connect(self.onChanged)
        self.password.textEdited[str].connect(self.onChanged)
        # self.password.setText("amir")
        self.password.setGeometry(QtCore.QRect(120, 350, 241, 31))
        self.password.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "border-radius: 15px;")
        self.password.setObjectName("password")
        self.letter = QtWidgets.QRadioButton(self.mainFrame)
        self.letter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letter.setGeometry(QtCore.QRect(330, 80, 16, 17))
        self.letter.setText("")
        self.letter.setObjectName("letter")
        self.number = QtWidgets.QRadioButton(self.mainFrame)
        self.number.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.number.setGeometry(QtCore.QRect(330, 120, 16, 17))
        self.number.setText("")
        self.number.setObjectName("number")
        self.letter_number = QtWidgets.QRadioButton(self.mainFrame)
        self.letter_number.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letter_number.setGeometry(QtCore.QRect(330, 160, 16, 17))
        self.letter_number.setText("")
        self.letter_number.setObjectName("letter_number")
        self.letter_label = QtWidgets.QLabel(self.mainFrame)
        self.letter_label.setGeometry(QtCore.QRect(410, 70, 47, 31))
        self.letter_label.setStyleSheet("color: rgb(12, 255, 12);\n"
                                        "font: 87 12pt \"Arial Black\";")
        self.letter_label.setObjectName("letter_label")
        self.number_label = QtWidgets.QLabel(self.mainFrame)
        self.number_label.setGeometry(QtCore.QRect(410, 120, 47, 13))
        self.number_label.setStyleSheet("color: rgb(12, 255, 12);\n"
                                        "font: 87 12pt \"Arial Black\";")
        self.number_label.setObjectName("number_label")
        self.letter_number_label = QtWidgets.QLabel(self.mainFrame)
        self.letter_number_label.setGeometry(QtCore.QRect(370, 150, 91, 31))
        self.letter_number_label.setStyleSheet("color: rgb(12, 255, 12);\n"
                                               "font: 87 12pt \"Arial Black\";")
        self.letter_number_label.setObjectName("letter_number_label")
        self.background_photo = QtWidgets.QLabel(self.mainFrame)
        self.background_photo.setGeometry(QtCore.QRect(20, 40, 201, 171))
        self.background_photo.setText("")
        self.background_photo.setPixmap(QtGui.QPixmap("background photo.png"))
        self.background_photo.setScaledContents(True)
        self.background_photo.setObjectName("background_photo")
        main.setCentralWidget(self.pageFrame)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        self.gray_heart.clicked.connect(self.gray_heart.hide)
        self.red_heart.clicked.connect(self.gray_heart.show)
        self.window_minimize.clicked.connect(main.showMinimized)
        self.window_closer.clicked.connect(main.close)
        self.window_maximize.clicked.connect(main.showFullScreen)
        QtCore.QMetaObject.connectSlotsByName(main)

        # start

        self.pageFrame2 = QtWidgets.QWidget(self.pageFrame)
        self.pageFrame2.hide()
        self.pageFrame2.setGeometry(-60, 40, 550, 450)
        self.pageFrame2.setStyleSheet("border-radius: 30px")
        self.pageFrame2.setObjectName("pageFrame")
        self.show_data_frame = QtWidgets.QFrame(self.pageFrame2)
        self.show_data_frame.setGeometry(QtCore.QRect(70, 30, 471, 361))
        self.show_data_frame.setStyleSheet("border-radius: 30px;\n"
                                           "background-color: rgb(0, 0, 89);")
        self.show_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_data_frame.setObjectName("show_data_frame")
        self.scrollArea = QtWidgets.QScrollArea(self.show_data_frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 241, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 241, 361))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.show_data_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.show_data_textEdit.setGeometry(QtCore.QRect(0, 0, 241, 361))
        self.show_data_textEdit.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
                                              "font: 87 10pt \"Arial Black\";\n"
                                              "font: 87 12pt \"Arial Black\";\n"
                                              "border-radius: 50px;\n"
                                              "color: rgb(12, 255, 12);\n"
                                              "background-color: rgb(0, 0, 89);")
        self.show_data_textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.show_data_textEdit.setOverwriteMode(False)
        self.show_data_textEdit.setObjectName("show_data_textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.show_data_image = QtWidgets.QLabel(self.show_data_frame)
        self.show_data_image.setGeometry(QtCore.QRect(280, 20, 171, 211))
        self.show_data_image.setText("")
        self.show_data_image.setPixmap(QtGui.QPixmap("show from database.png"))
        self.show_data_image.setScaledContents(True)
        self.show_data_image.setObjectName("show_data_image")
        main.setCentralWidget(self.pageFrame)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi2(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi2(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.show_data_textEdit.setHtml(_translate("main",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial Black\'; font-size:12pt; font-weight:80; font-style:normal;\">\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.show_data_textEdit.setPlaceholderText(_translate("main", "اطلاعاتی جهت چاپ یا نمایش موجود نمی باشد"))


    def onChanged(self, text):
        return self.gray_heart.show()

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("Password Generator", "MainWindow"))
        self.title.setText(_translate("main", "Password Generator"))
        self.letter_label.setText(_translate("main", "حروف:"))
        self.number_label.setText(_translate("main", "عدد:"))
        self.letter_number_label.setText(_translate("main", "حروف و عدد:"))


# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5 import QtGui
# from PyQt5 import QtWidgets, QtCore
#
#
# # from progectFile import progectClass
# # from login import Ui_MainWindow
#
# class RootMain(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#
#         self.ui = Ui_panel()
#
#         self.ui.setupUi(self)
#
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         self.show()
#         # self.oldPos = ""
#
#     def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
#         # print("come")
#         self.oldPos = evt.globalPos()
#         # self.mouseMoveEvent(self.oldPos)
#
#     def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
#         # print("move")
#         delta = QPoint(evt.globalPos() - self.oldPos)
#
#         self.move(self.x() + delta.x(), self.y() + delta.y())
#
#         self.oldPos = evt.globalPos()
#
#
# #
# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#
#     root = RootMain()
#
#     sys.exit(app.exec_())
