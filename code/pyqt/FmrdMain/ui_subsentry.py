# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/subs_entry.ui'
#
# Created: Wed Dec  7 22:20:31 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SubsEntryDlg(object):
    def setupUi(self, SubsEntryDlg):
        SubsEntryDlg.setObjectName("SubsEntryDlg")
        SubsEntryDlg.resize(920, 460)
        SubsEntryDlg.setMinimumSize(QtCore.QSize(920, 460))
        SubsEntryDlg.setMaximumSize(QtCore.QSize(920, 460))
        self.line_2 = QtGui.QFrame(SubsEntryDlg)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 921, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtGui.QWidget(SubsEntryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 851, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(105, 30))
        self.label.setMaximumSize(QtCore.QSize(105, 30))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.compSelect = QtGui.QComboBox(self.layoutWidget)
        self.compSelect.setMinimumSize(QtCore.QSize(330, 30))
        self.compSelect.setMaximumSize(QtCore.QSize(330, 30))
        self.compSelect.setObjectName("compSelect")
        self.horizontalLayout_3.addWidget(self.compSelect)
        spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(50, 30))
        self.label_11.setMaximumSize(QtCore.QSize(50, 30))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.phaseSelect = QtGui.QComboBox(self.layoutWidget)
        self.phaseSelect.setMinimumSize(QtCore.QSize(180, 30))
        self.phaseSelect.setMaximumSize(QtCore.QSize(180, 30))
        self.phaseSelect.setObjectName("phaseSelect")
        self.horizontalLayout_3.addWidget(self.phaseSelect)
        self.line = QtGui.QFrame(SubsEntryDlg)
        self.line.setGeometry(QtCore.QRect(0, 50, 921, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_2 = QtGui.QFrame(SubsEntryDlg)
        self.frame_2.setGeometry(QtCore.QRect(500, 400, 411, 51))
        self.frame_2.setMinimumSize(QtCore.QSize(411, 51))
        self.frame_2.setMaximumSize(QtCore.QSize(411, 51))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addEntry = QtGui.QPushButton(self.frame_2)
        self.addEntry.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.addEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.addEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon)
        self.addEntry.setObjectName("addEntry")
        self.deleteEntry = QtGui.QPushButton(self.frame_2)
        self.deleteEntry.setGeometry(QtCore.QRect(110, 10, 90, 30))
        self.deleteEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.deleteEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon1)
        self.deleteEntry.setObjectName("deleteEntry")
        self.saveEntry = QtGui.QPushButton(self.frame_2)
        self.saveEntry.setGeometry(QtCore.QRect(210, 10, 90, 30))
        self.saveEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.saveEntry.setMaximumSize(QtCore.QSize(90, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon2)
        self.saveEntry.setObjectName("saveEntry")
        self.closeButton = QtGui.QPushButton(self.frame_2)
        self.closeButton.setGeometry(QtCore.QRect(310, 10, 90, 30))
        self.closeButton.setMinimumSize(QtCore.QSize(90, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(90, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setObjectName("closeButton")
        self.frame = QtGui.QFrame(SubsEntryDlg)
        self.frame.setGeometry(QtCore.QRect(10, 400, 411, 51))
        self.frame.setMinimumSize(QtCore.QSize(411, 51))
        self.frame.setMaximumSize(QtCore.QSize(411, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstEntry = QtGui.QPushButton(self.frame)
        self.firstEntry.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.firstEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.firstEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.firstEntry.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon4)
        self.firstEntry.setObjectName("firstEntry")
        self.prevEntry = QtGui.QPushButton(self.frame)
        self.prevEntry.setGeometry(QtCore.QRect(110, 10, 90, 30))
        self.prevEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.prevEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.prevEntry.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon5)
        self.prevEntry.setObjectName("prevEntry")
        self.nextEntry = QtGui.QPushButton(self.frame)
        self.nextEntry.setGeometry(QtCore.QRect(210, 10, 90, 30))
        self.nextEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.nextEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.nextEntry.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon6)
        self.nextEntry.setObjectName("nextEntry")
        self.lastEntry = QtGui.QPushButton(self.frame)
        self.lastEntry.setGeometry(QtCore.QRect(310, 10, 90, 30))
        self.lastEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.lastEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.lastEntry.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon7)
        self.lastEntry.setObjectName("lastEntry")
        self.line_3 = QtGui.QFrame(SubsEntryDlg)
        self.line_3.setGeometry(QtCore.QRect(0, 380, 921, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtGui.QLabel(SubsEntryDlg)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 105, 30))
        self.label_3.setMinimumSize(QtCore.QSize(105, 30))
        self.label_3.setMaximumSize(QtCore.QSize(105, 30))
        self.label_3.setObjectName("label_3")
        self.matchSelect = QtGui.QComboBox(SubsEntryDlg)
        self.matchSelect.setGeometry(QtCore.QRect(120, 200, 330, 30))
        self.matchSelect.setMinimumSize(QtCore.QSize(330, 30))
        self.matchSelect.setMaximumSize(QtCore.QSize(330, 30))
        self.matchSelect.setObjectName("matchSelect")
        self.layoutWidget1 = QtGui.QWidget(SubsEntryDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 240, 891, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setMinimumSize(QtCore.QSize(105, 30))
        self.label_4.setMaximumSize(QtCore.QSize(105, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.subsID_display = QtGui.QLineEdit(self.layoutWidget1)
        self.subsID_display.setMinimumSize(QtCore.QSize(120, 30))
        self.subsID_display.setMaximumSize(QtCore.QSize(120, 30))
        self.subsID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.subsID_display.setMaxLength(7)
        self.subsID_display.setReadOnly(True)
        self.subsID_display.setObjectName("subsID_display")
        self.gridLayout.addWidget(self.subsID_display, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setMinimumSize(QtCore.QSize(105, 30))
        self.label_5.setMaximumSize(QtCore.QSize(105, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.teamSelect = QtGui.QComboBox(self.layoutWidget1)
        self.teamSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.teamSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.teamSelect.setObjectName("teamSelect")
        self.gridLayout.addWidget(self.teamSelect, 0, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setMinimumSize(QtCore.QSize(105, 30))
        self.label_10.setMaximumSize(QtCore.QSize(105, 30))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.outplayerSelect = QtGui.QComboBox(self.layoutWidget1)
        self.outplayerSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.outplayerSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.outplayerSelect.setObjectName("outplayerSelect")
        self.gridLayout.addWidget(self.outplayerSelect, 1, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setMinimumSize(QtCore.QSize(105, 30))
        self.label_7.setMaximumSize(QtCore.QSize(105, 30))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.inplayerSelect = QtGui.QComboBox(self.layoutWidget1)
        self.inplayerSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.inplayerSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.inplayerSelect.setObjectName("inplayerSelect")
        self.gridLayout.addWidget(self.inplayerSelect, 1, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setMinimumSize(QtCore.QSize(105, 30))
        self.label_8.setMaximumSize(QtCore.QSize(105, 30))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subtimeEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.subtimeEdit.setMinimumSize(QtCore.QSize(45, 30))
        self.subtimeEdit.setMaximumSize(QtCore.QSize(45, 30))
        self.subtimeEdit.setMaxLength(2)
        self.subtimeEdit.setObjectName("subtimeEdit")
        self.horizontalLayout.addWidget(self.subtimeEdit)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.stoppageEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.stoppageEdit.setMinimumSize(QtCore.QSize(45, 30))
        self.stoppageEdit.setMaximumSize(QtCore.QSize(45, 30))
        self.stoppageEdit.setMaxLength(2)
        self.stoppageEdit.setObjectName("stoppageEdit")
        self.horizontalLayout.addWidget(self.stoppageEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 2)
        self.layoutWidget_2 = QtGui.QWidget(SubsEntryDlg)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 60, 871, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leagueBox = QtGui.QGroupBox(self.layoutWidget_2)
        self.leagueBox.setMinimumSize(QtCore.QSize(270, 60))
        self.leagueBox.setMaximumSize(QtCore.QSize(270, 60))
        self.leagueBox.setObjectName("leagueBox")
        self.label_2 = QtGui.QLabel(self.leagueBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 50, 30))
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setObjectName("label_2")
        self.lgRoundSelect = QtGui.QComboBox(self.leagueBox)
        self.lgRoundSelect.setGeometry(QtCore.QRect(80, 20, 180, 30))
        self.lgRoundSelect.setMinimumSize(QtCore.QSize(180, 30))
        self.lgRoundSelect.setMaximumSize(QtCore.QSize(180, 30))
        self.lgRoundSelect.setObjectName("lgRoundSelect")
        self.gridLayout_2.addWidget(self.leagueBox, 0, 0, 1, 1)
        self.knockoutBox = QtGui.QGroupBox(self.layoutWidget_2)
        self.knockoutBox.setMinimumSize(QtCore.QSize(330, 60))
        self.knockoutBox.setMaximumSize(QtCore.QSize(585, 100))
        self.knockoutBox.setObjectName("knockoutBox")
        self.label_12 = QtGui.QLabel(self.knockoutBox)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 50, 30))
        self.label_12.setMinimumSize(QtCore.QSize(50, 30))
        self.label_12.setMaximumSize(QtCore.QSize(50, 30))
        self.label_12.setObjectName("label_12")
        self.koRoundSelect = QtGui.QComboBox(self.knockoutBox)
        self.koRoundSelect.setGeometry(QtCore.QRect(60, 20, 240, 30))
        self.koRoundSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.koRoundSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.koRoundSelect.setObjectName("koRoundSelect")
        self.koMatchdaySelect = QtGui.QComboBox(self.knockoutBox)
        self.koMatchdaySelect.setGeometry(QtCore.QRect(390, 20, 180, 30))
        self.koMatchdaySelect.setMinimumSize(QtCore.QSize(180, 30))
        self.koMatchdaySelect.setMaximumSize(QtCore.QSize(180, 30))
        self.koMatchdaySelect.setObjectName("koMatchdaySelect")
        self.label_13 = QtGui.QLabel(self.knockoutBox)
        self.label_13.setGeometry(QtCore.QRect(310, 20, 75, 30))
        self.label_13.setMinimumSize(QtCore.QSize(75, 30))
        self.label_13.setMaximumSize(QtCore.QSize(75, 30))
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.knockoutBox, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget_2)
        self.groupBox.setMinimumSize(QtCore.QSize(280, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(940, 100))
        self.groupBox.setObjectName("groupBox")
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(290, 20, 50, 30))
        self.label_14.setMinimumSize(QtCore.QSize(50, 30))
        self.label_14.setMaximumSize(QtCore.QSize(50, 30))
        self.label_14.setObjectName("label_14")
        self.grpRoundSelect = QtGui.QComboBox(self.groupBox)
        self.grpRoundSelect.setGeometry(QtCore.QRect(340, 20, 240, 30))
        self.grpRoundSelect.setMinimumSize(QtCore.QSize(240, 30))
        self.grpRoundSelect.setMaximumSize(QtCore.QSize(240, 30))
        self.grpRoundSelect.setObjectName("grpRoundSelect")
        self.groupSelect = QtGui.QComboBox(self.groupBox)
        self.groupSelect.setGeometry(QtCore.QRect(80, 20, 60, 30))
        self.groupSelect.setMinimumSize(QtCore.QSize(60, 30))
        self.groupSelect.setMaximumSize(QtCore.QSize(60, 30))
        self.groupSelect.setObjectName("groupSelect")
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 50, 30))
        self.label_15.setMinimumSize(QtCore.QSize(50, 30))
        self.label_15.setMaximumSize(QtCore.QSize(50, 30))
        self.label_15.setObjectName("label_15")
        self.grpMatchdaySelect = QtGui.QComboBox(self.groupBox)
        self.grpMatchdaySelect.setGeometry(QtCore.QRect(670, 20, 180, 30))
        self.grpMatchdaySelect.setMinimumSize(QtCore.QSize(180, 30))
        self.grpMatchdaySelect.setMaximumSize(QtCore.QSize(180, 30))
        self.grpMatchdaySelect.setObjectName("grpMatchdaySelect")
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(590, 20, 75, 30))
        self.label_16.setMinimumSize(QtCore.QSize(75, 30))
        self.label_16.setMaximumSize(QtCore.QSize(75, 30))
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(SubsEntryDlg)
        QtCore.QMetaObject.connectSlotsByName(SubsEntryDlg)

    def retranslateUi(self, SubsEntryDlg):
        SubsEntryDlg.setWindowTitle(QtGui.QApplication.translate("SubsEntryDlg", "Substitution Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Competition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.compSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Competition Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Phase</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.phaseSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Competition Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("SubsEntryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("SubsEntryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Save Entry to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("SubsEntryDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("SubsEntryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Match</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Subs ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.teamSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Team of substituted players", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Player Out</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.outplayerSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Player substituted out of match", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Player In</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.inplayerSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Player substituted into match", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Match Time</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.subtimeEdit.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Match time", None, QtGui.QApplication.UnicodeUTF8))
        self.subtimeEdit.setInputMask(QtGui.QApplication.translate("SubsEntryDlg", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.stoppageEdit.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Stoppage time", None, QtGui.QApplication.UnicodeUTF8))
        self.stoppageEdit.setInputMask(QtGui.QApplication.translate("SubsEntryDlg", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.leagueBox.setTitle(QtGui.QApplication.translate("SubsEntryDlg", "League Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lgRoundSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "League Round", None, QtGui.QApplication.UnicodeUTF8))
        self.knockoutBox.setTitle(QtGui.QApplication.translate("SubsEntryDlg", "Knockout Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.koRoundSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Knockout Round", None, QtGui.QApplication.UnicodeUTF8))
        self.koMatchdaySelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Knockout Round Matchday", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Matchday</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SubsEntryDlg", "Group Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.grpRoundSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Group Phase Round", None, QtGui.QApplication.UnicodeUTF8))
        self.groupSelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Group Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Group</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.grpMatchdaySelect.setToolTip(QtGui.QApplication.translate("SubsEntryDlg", "Group Round Matchday", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("SubsEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Matchday</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
