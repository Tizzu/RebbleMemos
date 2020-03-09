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

# Commented entries aren't showing the same icon as displayed in the Wiki so they can't be displayed here
# I'm leaving them here for code completeness but they haven't an icon in the assets anymore
iconsList = [
    "NOTIFICATION_REMINDER",
    "ALARM_CLOCK",
    "AMERICAN_FOOTBALL",
    "AUDIO_CASSETTE",
    "BASKETBALL",
    "BIRTHDAY_EVENT",
    "CAR_RENTAL",
    # "CHECK_INTERNET_CONNECTION",
    "CLOUDY_DAY",
    "CRICKET_GAME",
    # "DAY_SEPARATOR",
    "DINNER_RESERVATION",
    "DISMISSED_PHONE_CALL",
    # "DURING_PHONE_CALL",
    # "DURING_PHONE_CALL_CENTERED",
    "GENERIC_CONFIRMATION",
    "GENERIC_EMAIL",
    "GENERIC_QUESTION",
    # "GENERIC_SMS",
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
    # "NO_EVENTS",
    "PARTLY_CLOUDY",
    "PAY_BILL",
    "RADIO_SHOW",
    "RAINING_AND_SNOWING",
    "REACHED_FITNESS_GOAL",
    # "RESULT_DELETED",
    "RESULT_DISMISSED",
    "RESULT_FAILED",
    # "RESULT_MUTE",
    # "RESULT_SENT",
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
    # "WATCH_DISCONNECTED"
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
        self.comingSoon = QtWidgets.QLabel(self.centralwidget)
        self.comingSoon.setGeometry(QtCore.QRect(450, 149, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.comingSoon.setFont(font)
        self.comingSoon.setAlignment(QtCore.Qt.AlignCenter)
        self.comingSoon.setObjectName("comingSoon")
        self.comingSoonSub = QtWidgets.QLabel(self.centralwidget)
        self.comingSoonSub.setGeometry(QtCore.QRect(450, 244, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comingSoonSub.setFont(font)
        self.comingSoonSub.setAlignment(QtCore.Qt.AlignCenter)
        self.comingSoonSub.setWordWrap(True)
        self.comingSoonSub.setObjectName("comingSoonSub")
        self.calendarPin = QtWidgets.QTabWidget(self.centralwidget)
        self.calendarPin.setGeometry(QtCore.QRect(20, 10, 421, 361))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.calendarPin.setPalette(palette)
        self.calendarPin.setAutoFillBackground(True)
        self.calendarPin.setTabPosition(QtWidgets.QTabWidget.North)
        self.calendarPin.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.calendarPin.setUsesScrollButtons(True)
        self.calendarPin.setDocumentMode(True)
        self.calendarPin.setObjectName("calendarPin")
        self.genericPin = QtWidgets.QWidget()
        self.genericPin.setObjectName("genericPin")
        self.formLayoutWidget = QtWidgets.QWidget(self.genericPin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.genericPinLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.genericPinLayout.setContentsMargins(0, 0, 0, 0)
        self.genericPinLayout.setObjectName("genericPinLayout")
        self.titleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QtCore.QSize(82, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.genericPinLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleEdit.setObjectName("titleEdit")
        self.genericPinLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.subtitleEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.subtitleEdit.setObjectName("subtitleEdit")
        self.genericPinLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subtitleEdit)
        self.bodyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.bodyLabel.setMinimumSize(QtCore.QSize(82, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bodyLabel.setFont(font)
        self.bodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bodyLabel.setWordWrap(True)
        self.bodyLabel.setObjectName("bodyLabel")
        self.genericPinLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bodyLabel)
        self.bodyEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyEdit.setObjectName("bodyEdit")
        self.genericPinLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bodyEdit)
        self.timeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(82, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.genericPinLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timeLabel)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.OffsetFromUTC)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.genericPinLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        self.iconLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iconLabel.setMinimumSize(QtCore.QSize(82, 0))
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
        self.genericPinLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.iconLabel)
        self.iconBox = QtWidgets.QHBoxLayout()
        self.iconBox.setObjectName("iconBox")
        self.iconSelector = QtWidgets.QComboBox(self.formLayoutWidget)
        self.iconSelector.setEditable(True)
        self.iconSelector.setObjectName("iconSelector")
        self.iconSelector.addItems(iconsList)
        self.iconSelector.currentIndexChanged.connect(self.changeIconShow)
        self.iconBox.addWidget(self.iconSelector)
        self.iconShow = QtWidgets.QLabel(self.formLayoutWidget)
        self.iconShow.setMaximumSize(QtCore.QSize(25, 25))
        self.iconShow.setText("")
        # NOTE: Manually changed to resource_path()
        self.iconShow.setPixmap(QtGui.QPixmap(resource_path("NOTIFICATION_REMINDER.png")))
        self.iconShow.setObjectName("iconShow")
        self.iconBox.addWidget(self.iconShow)
        self.genericPinLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.iconBox)
        self.subtitleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.subtitleLabel.setMinimumSize(QtCore.QSize(82, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitleLabel.setWordWrap(True)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.genericPinLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subtitleLabel)
        icon1 = QtGui.QIcon()
        # NOTE: Manually changed to resource_path()
        icon1.addPixmap(QtGui.QPixmap(resource_path("NOTIFICATION_REMINDER.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendarPin.addTab(self.genericPin, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(90, 110, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        icon2 = QtGui.QIcon()
        # NOTE: Manually changed to resource_path()
        icon2.addPixmap(QtGui.QPixmap(resource_path("TIMELINE_CALENDAR.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendarPin.addTab(self.tab_2, icon2, "")
        self.calendarPin.raise_()
        self.pushButton.raise_()
        self.line.raise_()
        self.comingSoon.raise_()
        self.comingSoonSub.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.calendarPin.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeIconShow(self):
        self.iconShow.setPixmap(QtGui.QPixmap(resource_path(self.iconSelector.currentText() + ".png")))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rebble Memos"))
        self.pushButton.setText(_translate("MainWindow", "Send to Timeline!"))
        self.comingSoon.setText(_translate("MainWindow", "Pin History\n"
                                                         "Coming Soon"))
        self.comingSoonSub.setText(
            _translate("MainWindow", "You\'ll be able to modify already sent memos directly from here!"))
        self.titleLabel.setText(_translate("MainWindow", "Memo Title"))
        self.subtitleLabel.setText(_translate("MainWindow", "Memo Subtitle (optional)"))
        self.bodyLabel.setText(_translate("MainWindow", "Memo Body (optional)"))
        self.timeLabel.setText(_translate("MainWindow", "Memo Time"))
        self.comingSoon.setText(_translate("MainWindow", "Pin History\nComing Soon"))
        self.iconLabel.setText(_translate("MainWindow", "Memo Icon"))
        self.comingSoonSub.setText(
            _translate("MainWindow", "You\'ll be able to modify already sent memos directly from here!"))
        self.subtitleLabel.setText(_translate("MainWindow", "Memo Subtitle (optional)"))
        self.calendarPin.setTabText(self.calendarPin.indexOf(self.genericPin), _translate("MainWindow", "Generic Pin"))
        self.label.setText(_translate("MainWindow", "Coming Soon"))
        self.calendarPin.setTabText(self.calendarPin.indexOf(self.tab_2), _translate("MainWindow", "Calendar Pin"))

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

            functions.test(self.titleEdit.text(),
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
