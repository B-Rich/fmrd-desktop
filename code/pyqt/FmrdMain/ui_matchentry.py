# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/match_entry.ui'
#
# Created: Mon Sep 12 22:19:36 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MatchEntryDlg(object):
    def setupUi(self, MatchEntryDlg):
        MatchEntryDlg.setObjectName("MatchEntryDlg")
        MatchEntryDlg.resize(960, 480)
        MatchEntryDlg.setMinimumSize(QtCore.QSize(960, 480))
        MatchEntryDlg.setMaximumSize(QtCore.QSize(960, 480))
        self.line = QtGui.QFrame(MatchEntryDlg)
        self.line.setGeometry(QtCore.QRect(9, 42, 911, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(MatchEntryDlg)
        self.line_2.setGeometry(QtCore.QRect(510, 50, 16, 351))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.overviewBox = QtGui.QGroupBox(MatchEntryDlg)
        self.overviewBox.setGeometry(QtCore.QRect(10, 60, 501, 214))
        self.overviewBox.setObjectName("overviewBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.overviewBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtGui.QLabel(self.overviewBox)
        self.label_2.setMinimumSize(QtCore.QSize(105, 30))
        self.label_2.setMaximumSize(QtCore.QSize(105, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.matchCompSelect = QtGui.QComboBox(self.overviewBox)
        self.matchCompSelect.setMinimumSize(QtCore.QSize(360, 30))
        self.matchCompSelect.setMaximumSize(QtCore.QSize(360, 30))
        self.matchCompSelect.setObjectName("matchCompSelect")
        self.gridLayout_3.addWidget(self.matchCompSelect, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.overviewBox)
        self.label_3.setMinimumSize(QtCore.QSize(105, 30))
        self.label_3.setMaximumSize(QtCore.QSize(105, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.matchRoundSelect = QtGui.QComboBox(self.overviewBox)
        self.matchRoundSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.matchRoundSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.matchRoundSelect.setObjectName("matchRoundSelect")
        self.gridLayout_3.addWidget(self.matchRoundSelect, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.overviewBox)
        self.label_5.setMinimumSize(QtCore.QSize(105, 30))
        self.label_5.setMaximumSize(QtCore.QSize(105, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.matchVenueSelect = QtGui.QComboBox(self.overviewBox)
        self.matchVenueSelect.setMinimumSize(QtCore.QSize(360, 30))
        self.matchVenueSelect.setMaximumSize(QtCore.QSize(360, 30))
        self.matchVenueSelect.setObjectName("matchVenueSelect")
        self.gridLayout_3.addWidget(self.matchVenueSelect, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.overviewBox)
        self.label_6.setMinimumSize(QtCore.QSize(105, 30))
        self.label_6.setMaximumSize(QtCore.QSize(105, 30))
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.matchRefSelect = QtGui.QComboBox(self.overviewBox)
        self.matchRefSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.matchRefSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.matchRefSelect.setObjectName("matchRefSelect")
        self.gridLayout_3.addWidget(self.matchRefSelect, 4, 1, 1, 1)
        self.line_3 = QtGui.QFrame(MatchEntryDlg)
        self.line_3.setGeometry(QtCore.QRect(0, 400, 941, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutWidget = QtGui.QWidget(MatchEntryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 270, 332, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.timeBox = QtGui.QGroupBox(self.layoutWidget)
        self.timeBox.setMinimumSize(QtCore.QSize(267, 63))
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.timeBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtGui.QLabel(self.timeBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.firstHalfLengthEdit = QtGui.QLineEdit(self.timeBox)
        self.firstHalfLengthEdit.setMinimumSize(QtCore.QSize(50, 30))
        self.firstHalfLengthEdit.setMaximumSize(QtCore.QSize(50, 30))
        self.firstHalfLengthEdit.setMaxLength(2)
        self.firstHalfLengthEdit.setObjectName("firstHalfLengthEdit")
        self.horizontalLayout.addWidget(self.firstHalfLengthEdit)
        self.label_12 = QtGui.QLabel(self.timeBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.secondHalfLengthEdit = QtGui.QLineEdit(self.timeBox)
        self.secondHalfLengthEdit.setMinimumSize(QtCore.QSize(50, 30))
        self.secondHalfLengthEdit.setMaximumSize(QtCore.QSize(50, 30))
        self.secondHalfLengthEdit.setMaxLength(2)
        self.secondHalfLengthEdit.setObjectName("secondHalfLengthEdit")
        self.horizontalLayout.addWidget(self.secondHalfLengthEdit)
        self.horizontalLayout_5.addWidget(self.timeBox)
        spacerItem1 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.attendanceBox = QtGui.QGroupBox(MatchEntryDlg)
        self.attendanceBox.setGeometry(QtCore.QRect(10, 340, 141, 63))
        self.attendanceBox.setMinimumSize(QtCore.QSize(141, 63))
        self.attendanceBox.setMaximumSize(QtCore.QSize(141, 63))
        self.attendanceBox.setFlat(False)
        self.attendanceBox.setObjectName("attendanceBox")
        self.attendanceEdit = QtGui.QLineEdit(self.attendanceBox)
        self.attendanceEdit.setGeometry(QtCore.QRect(10, 25, 90, 30))
        self.attendanceEdit.setMinimumSize(QtCore.QSize(90, 30))
        self.attendanceEdit.setMaximumSize(QtCore.QSize(90, 30))
        self.attendanceEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.attendanceEdit.setObjectName("attendanceEdit")
        self.hometeamBox = QtGui.QGroupBox(MatchEntryDlg)
        self.hometeamBox.setGeometry(QtCore.QRect(530, 60, 420, 150))
        self.hometeamBox.setMinimumSize(QtCore.QSize(420, 150))
        self.hometeamBox.setMaximumSize(QtCore.QSize(420, 150))
        self.hometeamBox.setObjectName("hometeamBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.hometeamBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtGui.QLabel(self.hometeamBox)
        self.label_8.setMinimumSize(QtCore.QSize(120, 30))
        self.label_8.setMaximumSize(QtCore.QSize(120, 30))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.homemgrSelect = QtGui.QComboBox(self.hometeamBox)
        self.homemgrSelect.setEnabled(True)
        self.homemgrSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.homemgrSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.homemgrSelect.setObjectName("homemgrSelect")
        self.gridLayout_2.addWidget(self.homemgrSelect, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.hometeamBox)
        self.label_7.setMinimumSize(QtCore.QSize(120, 30))
        self.label_7.setMaximumSize(QtCore.QSize(120, 30))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.hometeamSelect = QtGui.QComboBox(self.hometeamBox)
        self.hometeamSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.hometeamSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.hometeamSelect.setObjectName("hometeamSelect")
        self.gridLayout_2.addWidget(self.hometeamSelect, 1, 1, 1, 1)
        self.homeconfedSelect = QtGui.QComboBox(self.hometeamBox)
        self.homeconfedSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.homeconfedSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.homeconfedSelect.setObjectName("homeconfedSelect")
        self.gridLayout_2.addWidget(self.homeconfedSelect, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.hometeamBox)
        self.label_13.setMinimumSize(QtCore.QSize(120, 30))
        self.label_13.setMaximumSize(QtCore.QSize(120, 30))
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.awayteamBox = QtGui.QGroupBox(MatchEntryDlg)
        self.awayteamBox.setGeometry(QtCore.QRect(530, 213, 411, 131))
        self.awayteamBox.setMaximumSize(QtCore.QSize(420, 150))
        self.awayteamBox.setObjectName("awayteamBox")
        self.gridLayout = QtGui.QGridLayout(self.awayteamBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtGui.QLabel(self.awayteamBox)
        self.label_9.setMinimumSize(QtCore.QSize(120, 30))
        self.label_9.setMaximumSize(QtCore.QSize(120, 30))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.awayteamSelect = QtGui.QComboBox(self.awayteamBox)
        self.awayteamSelect.setEnabled(True)
        self.awayteamSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.awayteamSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.awayteamSelect.setObjectName("awayteamSelect")
        self.gridLayout.addWidget(self.awayteamSelect, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.awayteamBox)
        self.label_10.setMinimumSize(QtCore.QSize(120, 30))
        self.label_10.setMaximumSize(QtCore.QSize(120, 30))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.awaymgrSelect = QtGui.QComboBox(self.awayteamBox)
        self.awaymgrSelect.setEnabled(True)
        self.awaymgrSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.awaymgrSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.awaymgrSelect.setObjectName("awaymgrSelect")
        self.gridLayout.addWidget(self.awaymgrSelect, 2, 1, 1, 1)
        self.awayconfedSelect = QtGui.QComboBox(self.awayteamBox)
        self.awayconfedSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.awayconfedSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.awayconfedSelect.setObjectName("awayconfedSelect")
        self.gridLayout.addWidget(self.awayconfedSelect, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.awayteamBox)
        self.label_14.setMinimumSize(QtCore.QSize(120, 30))
        self.label_14.setMaximumSize(QtCore.QSize(120, 30))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.matchFrame = QtGui.QFrame(MatchEntryDlg)
        self.matchFrame.setGeometry(QtCore.QRect(530, 350, 401, 51))
        self.matchFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.matchFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.matchFrame.setObjectName("matchFrame")
        self.enviroButton = QtGui.QPushButton(self.matchFrame)
        self.enviroButton.setGeometry(QtCore.QRect(270, 10, 120, 30))
        self.enviroButton.setMinimumSize(QtCore.QSize(120, 30))
        self.enviroButton.setMaximumSize(QtCore.QSize(120, 30))
        self.enviroButton.setDefault(False)
        self.enviroButton.setObjectName("enviroButton")
        self.awayLineupButton = QtGui.QPushButton(self.matchFrame)
        self.awayLineupButton.setEnabled(True)
        self.awayLineupButton.setGeometry(QtCore.QRect(140, 10, 120, 30))
        self.awayLineupButton.setMinimumSize(QtCore.QSize(120, 30))
        self.awayLineupButton.setMaximumSize(QtCore.QSize(120, 30))
        self.awayLineupButton.setObjectName("awayLineupButton")
        self.homeLineupButton = QtGui.QPushButton(self.matchFrame)
        self.homeLineupButton.setEnabled(True)
        self.homeLineupButton.setGeometry(QtCore.QRect(10, 10, 120, 30))
        self.homeLineupButton.setMinimumSize(QtCore.QSize(120, 30))
        self.homeLineupButton.setMaximumSize(QtCore.QSize(120, 30))
        self.homeLineupButton.setObjectName("homeLineupButton")
        self.controlFrame = QtGui.QFrame(MatchEntryDlg)
        self.controlFrame.setGeometry(QtCore.QRect(530, 420, 411, 51))
        self.controlFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.controlFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.controlFrame.setObjectName("controlFrame")
        self.closeButton = QtGui.QPushButton(self.controlFrame)
        self.closeButton.setGeometry(QtCore.QRect(310, 10, 90, 30))
        self.closeButton.setMinimumSize(QtCore.QSize(90, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(90, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setObjectName("closeButton")
        self.deleteEntry = QtGui.QPushButton(self.controlFrame)
        self.deleteEntry.setGeometry(QtCore.QRect(210, 10, 90, 30))
        self.deleteEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.deleteEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon1)
        self.deleteEntry.setObjectName("deleteEntry")
        self.saveEntry = QtGui.QPushButton(self.controlFrame)
        self.saveEntry.setGeometry(QtCore.QRect(110, 10, 90, 30))
        self.saveEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.saveEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon2)
        self.saveEntry.setObjectName("saveEntry")
        self.addEntry = QtGui.QPushButton(self.controlFrame)
        self.addEntry.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.addEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.addEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon3)
        self.addEntry.setObjectName("addEntry")
        self.frame = QtGui.QFrame(MatchEntryDlg)
        self.frame.setGeometry(QtCore.QRect(80, 420, 371, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstEntry = QtGui.QPushButton(self.frame)
        self.firstEntry.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.firstEntry.setMinimumSize(QtCore.QSize(80, 30))
        self.firstEntry.setMaximumSize(QtCore.QSize(80, 30))
        self.firstEntry.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon4)
        self.firstEntry.setObjectName("firstEntry")
        self.prevEntry = QtGui.QPushButton(self.frame)
        self.prevEntry.setGeometry(QtCore.QRect(100, 10, 80, 30))
        self.prevEntry.setMinimumSize(QtCore.QSize(80, 30))
        self.prevEntry.setMaximumSize(QtCore.QSize(80, 30))
        self.prevEntry.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon5)
        self.prevEntry.setObjectName("prevEntry")
        self.nextEntry = QtGui.QPushButton(self.frame)
        self.nextEntry.setGeometry(QtCore.QRect(190, 10, 80, 30))
        self.nextEntry.setMinimumSize(QtCore.QSize(80, 30))
        self.nextEntry.setMaximumSize(QtCore.QSize(80, 30))
        self.nextEntry.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon6)
        self.nextEntry.setObjectName("nextEntry")
        self.lastEntry = QtGui.QPushButton(self.frame)
        self.lastEntry.setGeometry(QtCore.QRect(280, 10, 80, 30))
        self.lastEntry.setMinimumSize(QtCore.QSize(80, 30))
        self.lastEntry.setMaximumSize(QtCore.QSize(80, 30))
        self.lastEntry.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon7)
        self.lastEntry.setObjectName("lastEntry")
        self.widget = QtGui.QWidget(MatchEntryDlg)
        self.widget.setGeometry(QtCore.QRect(9, 9, 399, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(70, 20))
        self.label.setMaximumSize(QtCore.QSize(70, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.matchID_display = QtGui.QLineEdit(self.widget)
        self.matchID_display.setMinimumSize(QtCore.QSize(120, 30))
        self.matchID_display.setMaximumSize(QtCore.QSize(120, 30))
        self.matchID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.matchID_display.setMaxLength(7)
        self.matchID_display.setReadOnly(True)
        self.matchID_display.setObjectName("matchID_display")
        self.horizontalLayout_2.addWidget(self.matchID_display)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 20))
        self.label_4.setMaximumSize(QtCore.QSize(50, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.matchDateEdit = QtGui.QDateEdit(self.widget)
        self.matchDateEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.matchDateEdit.setMaximumSize(QtCore.QSize(120, 30))
        self.matchDateEdit.setMinimumDate(QtCore.QDate(1856, 1, 1))
        self.matchDateEdit.setObjectName("matchDateEdit")
        self.horizontalLayout_2.addWidget(self.matchDateEdit)
        self.label_2.setBuddy(self.matchCompSelect)
        self.label_3.setBuddy(self.matchRoundSelect)
        self.label_5.setBuddy(self.matchVenueSelect)
        self.label_6.setBuddy(self.matchRefSelect)
        self.label_11.setBuddy(self.firstHalfLengthEdit)
        self.label_12.setBuddy(self.secondHalfLengthEdit)
        self.label_8.setBuddy(self.homemgrSelect)
        self.label_7.setBuddy(self.hometeamSelect)
        self.label_13.setBuddy(self.hometeamSelect)
        self.label_9.setBuddy(self.awayteamSelect)
        self.label_10.setBuddy(self.awaymgrSelect)
        self.label_14.setBuddy(self.hometeamSelect)
        self.label.setBuddy(self.matchID_display)

        self.retranslateUi(MatchEntryDlg)
        QtCore.QMetaObject.connectSlotsByName(MatchEntryDlg)

    def retranslateUi(self, MatchEntryDlg):
        MatchEntryDlg.setWindowTitle(QtGui.QApplication.translate("MatchEntryDlg", "Match Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.overviewBox.setTitle(QtGui.QApplication.translate("MatchEntryDlg", "Match Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Competition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matchCompSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Football competition", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matchRoundSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Competition phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Venue</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matchVenueSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Match venue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Referee</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matchRefSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Match referee", None, QtGui.QApplication.UnicodeUTF8))
        self.timeBox.setTitle(QtGui.QApplication.translate("MatchEntryDlg", "Match Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1st half</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.firstHalfLengthEdit.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Total playing time of first half", None, QtGui.QApplication.UnicodeUTF8))
        self.firstHalfLengthEdit.setInputMask(QtGui.QApplication.translate("MatchEntryDlg", "99; ", None, QtGui.QApplication.UnicodeUTF8))
        self.firstHalfLengthEdit.setText(QtGui.QApplication.translate("MatchEntryDlg", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2nd half</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.secondHalfLengthEdit.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Total playing time of second half", None, QtGui.QApplication.UnicodeUTF8))
        self.secondHalfLengthEdit.setInputMask(QtGui.QApplication.translate("MatchEntryDlg", "99; ", None, QtGui.QApplication.UnicodeUTF8))
        self.secondHalfLengthEdit.setText(QtGui.QApplication.translate("MatchEntryDlg", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.attendanceBox.setTitle(QtGui.QApplication.translate("MatchEntryDlg", "Attendance", None, QtGui.QApplication.UnicodeUTF8))
        self.attendanceEdit.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Match attendance", None, QtGui.QApplication.UnicodeUTF8))
        self.attendanceEdit.setInputMask(QtGui.QApplication.translate("MatchEntryDlg", "999999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.attendanceEdit.setText(QtGui.QApplication.translate("MatchEntryDlg", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.hometeamBox.setTitle(QtGui.QApplication.translate("MatchEntryDlg", "Home Team", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Manager</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.homemgrSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Home team manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.hometeamSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Home team name", None, QtGui.QApplication.UnicodeUTF8))
        self.homeconfedSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Home team name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Confederation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awayteamBox.setTitle(QtGui.QApplication.translate("MatchEntryDlg", "Away Team", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awayteamSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Away team name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Manager</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awaymgrSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Away team manager", None, QtGui.QApplication.UnicodeUTF8))
        self.awayconfedSelect.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Home team name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Confederation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.enviroButton.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Environmental conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.enviroButton.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Environments", None, QtGui.QApplication.UnicodeUTF8))
        self.awayLineupButton.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Away team match lineups", None, QtGui.QApplication.UnicodeUTF8))
        self.awayLineupButton.setText(QtGui.QApplication.translate("MatchEntryDlg", "A&way Lineup", None, QtGui.QApplication.UnicodeUTF8))
        self.homeLineupButton.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Home team match lineups", None, QtGui.QApplication.UnicodeUTF8))
        self.homeLineupButton.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Home Lineup", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("MatchEntryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("MatchEntryDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">Match &amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MatchEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Date</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matchDateEdit.setDisplayFormat(QtGui.QApplication.translate("MatchEntryDlg", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
