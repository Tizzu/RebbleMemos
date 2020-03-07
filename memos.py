# -*- coding: utf-8 -*-

# This file was generated with Qt Designer (or "pyuic5 -x interface.ui -o memos.py")
# sendToTest() and resource_path() are the only ones that are added after UI generation, and
# all "QPixmap" images have been manually changed to resource_path(image) - look for "note" comments inside UI_MainWindow()
# It's advised, in case of UI update, to generate a second .py file and merge/update the changes

# Using PyQt5 as UI engine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox

# importing functions from another file so it's easier to get the program working in case of UI update
import functions
import os

iconsList = [
    "NOTIFICATION_REMINDER",
    "ALARM_CLOCK",
    "AMERICAN_FOOTBALL",
    "AUDIO_CASSETTE",
    "BASKETBALL",
    "BIRTHDAY_EVENT",
    "CAR_RENTAL",
    "CHECK_INTERNET_CONNECTION",
    "CLOUDY_DAY",
    "CRICKET_GAME",
    "DAY_SEPARATOR",
    "DINNER_RESERVATION",
    "DISMISSED_PHONE_CALL",
    "DURING_PHONE_CALL",
    "DURING_PHONE_CALL_CENTERED",
    "GENERIC_CONFIRMATION",
    "GENERIC_EMAIL",
    "GENERIC_QUESTION",
    "GENERIC_SMS",
    "GENERIC_WARNING",
    "GLUCOSE_MONITOR",
    "HEAVY_RAIN",
    "HEAVY_SNOW",
    "HOCKEY_GAME",
    "HOTEL_RESERVATION",
    "INCOMING_PHONE_CALL",
    "LIGHT_RAIN",
    "LIGHT_SNOW",
    "LOCATION",
    "MOVIE_EVENT",
    "MUSIC_EVENT",
    "NEWS_EVENT",
    "NOTIFICATION_FLAG",
    "NOTIFICATION_GENERIC",
    "NOTIFICATION_LIGHTHOUSE",
    "NO_EVENTS",
    "PARTLY_CLOUDY",
    "PAY_BILL",
    "RADIO_SHOW",
    "RAINING_AND_SNOWING",
    "REACHED_FITNESS_GOAL",
    "RESULT_DELETED",
    "RESULT_DISMISSED",
    "RESULT_FAILED",
    "RESULT_MUTE",
    "RESULT_SENT",
    "SCHEDULED_EVENT",
    "SCHEDULED_FLIGHT",
    "SETTINGS",
    "SOCCER_GAME",
    "STOCKS_EVENT",
    "SUNRISE",
    "SUNSET",
    "TIDE_IS_HIGH",
    "TIMELINE_BASEBALL",
    "TIMELINE_CALENDAR",
    "TIMELINE_MISSED_CALL",
    "TIMELINE_SPORTS",
    "TIMELINE_SUN",
    "TIMELINE_WEATHER",
    "TV_SHOW",
    "WATCH_DISCONNECTED"
]


# This function is needed in order to display images inside the application once it's packaged into an executable
# Unfortunately this means losing the ability to display images if it's not (as far as I've tested)
# Thanks Internet for this snippet! (Multiple sites showed this function so I don't know who's the first)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 465)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        # NOTE: Manually changed to resource_path()
        icon.addPixmap(QtGui.QPixmap(resource_path("memo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 380, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendToTest)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(110, 30, 321, 20))
        self.titleEdit.setObjectName("titleEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(440, 30, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.subtitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.subtitleLabel.setGeometry(QtCore.QRect(10, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitleLabel.setWordWrap(True)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.subtitleEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.subtitleEdit.setGeometry(QtCore.QRect(110, 60, 321, 51))
        self.subtitleEdit.setObjectName("subtitleEdit")
        self.bodyLabel = QtWidgets.QLabel(self.centralwidget)
        self.bodyLabel.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bodyLabel.setFont(font)
        self.bodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bodyLabel.setWordWrap(True)
        self.bodyLabel.setObjectName("bodyLabel")
        self.bodyEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bodyEdit.setGeometry(QtCore.QRect(110, 120, 321, 61))
        self.bodyEdit.setObjectName("bodyEdit")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(20, 240, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(110, 240, 321, 22))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.OffsetFromUTC)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-2))
        self.dateTimeEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.comingSoon = QtWidgets.QLabel(self.centralwidget)
        self.comingSoon.setGeometry(QtCore.QRect(450, 149, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.comingSoon.setFont(font)
        self.comingSoon.setAlignment(QtCore.Qt.AlignCenter)
        self.comingSoon.setObjectName("comingSoon")
        self.iconLabel = QtWidgets.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(20, 290, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.iconLabel.setFont(font)
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.comingSoonSub = QtWidgets.QLabel(self.centralwidget)
        self.comingSoonSub.setGeometry(QtCore.QRect(450, 244, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comingSoonSub.setFont(font)
        self.comingSoonSub.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.comingSoonSub.setWordWrap(True)
        self.comingSoonSub.setObjectName("comingSoonSub")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 290, 321, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.iconBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.iconBox.setContentsMargins(0, 0, 0, 0)
        self.iconBox.setObjectName("iconBox")
        self.iconSelector = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.iconSelector.setEditable(True)
        self.iconSelector.setObjectName("iconSelector")
        self.iconSelector.addItems(iconsList)
        self.iconSelector.currentIndexChanged.connect(self.changeIconShow)
        self.iconBox.addWidget(self.iconSelector)
        self.iconShow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.iconShow.setMaximumSize(QtCore.QSize(25, 25))
        self.iconShow.setText("")
        self.iconShow.setPixmap(QtGui.QPixmap(resource_path("NOTIFICATION_REMINDER.png")))
        self.iconShow.setObjectName("iconShow")
        self.iconBox.addWidget(self.iconShow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeIconShow(self):
        self.iconShow.setPixmap(QtGui.QPixmap(resource_path(self.iconSelector.currentText() + ".png")))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rebble Memos"))
        self.pushButton.setText(_translate("MainWindow", "Send to Timeline!"))
        self.titleLabel.setText(_translate("MainWindow", "Memo Title"))
        self.subtitleLabel.setText(_translate("MainWindow", "Memo Subtitle (optional)"))
        self.bodyLabel.setText(_translate("MainWindow", "Memo Body (optional)"))
        self.timeLabel.setText(_translate("MainWindow", "Memo Time"))
        self.comingSoon.setText(_translate("MainWindow", "Pin History\nComing Soon"))
        self.iconLabel.setText(_translate("MainWindow", "Memo Icon"))
        self.comingSoonSub.setText(
            _translate("MainWindow", "You\'ll be able to modify already sent memos directly from here!"))

    # This function checks if the title is not empty (since it's the only one required that can be empty at runtime -
    # the other mandatory field, time, is already set to CurrentTime)
    # if so it invokes functions(sendToTimeline) with data taken from the form
    def sendToTest(self):
        if self.titleEdit.text() == "":
            alert = QMessageBox()
            alert.setWindowTitle('Rebble Memos')
            icon = QtGui.QIcon()
            # NOTE: Manually changed to resource_path()
            icon.addPixmap(QtGui.QPixmap(resource_path("memo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            alert.setWindowIcon(icon)
            alert.setText("Title required. \nPlease insert one and try again")
            alert.setMinimumWidth(500)
            alert.exec_()
        else:
            # For some reason the Timeline servers don't accept ISO time with an offset different from "Z", so you need
            # to convert it to ISO time at UTC+0
            now = QDateTime.currentDateTime()
            offset = now.offsetFromUtc()
            expected = self.dateTimeEdit.dateTime()
            expected.setOffsetFromUtc(offset)

            functions.sendToTimeline(self.titleEdit.text(),
                           self.subtitleEdit.toPlainText(),
                           self.bodyEdit.toPlainText(),
                           expected.toTimeSpec(Qt.OffsetFromUTC),
                           self.iconSelector.currentText())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
