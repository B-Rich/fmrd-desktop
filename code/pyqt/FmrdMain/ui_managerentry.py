# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_entry.ui'
#
# Created: Thu Jan 27 00:13:05 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_managerEntryDlg(object):
    def setupUi(self, managerEntryDlg):
        managerEntryDlg.setObjectName("managerEntryDlg")
        managerEntryDlg.resize(800, 250)
        managerEntryDlg.setMinimumSize(QtCore.QSize(800, 250))
        managerEntryDlg.setMaximumSize(QtCore.QSize(800, 250))
        self.frame_2 = QtGui.QFrame(managerEntryDlg)
        self.frame_2.setGeometry(QtCore.QRect(30, 170, 331, 51))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.firstEntry = QtGui.QPushButton(self.frame_2)
        self.firstEntry.setGeometry(QtCore.QRect(10, 10, 71, 33))
        self.firstEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.firstEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.firstEntry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon)
        self.firstEntry.setObjectName("firstEntry")
        self.prevEntry = QtGui.QPushButton(self.frame_2)
        self.prevEntry.setGeometry(QtCore.QRect(90, 10, 71, 33))
        self.prevEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.prevEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.prevEntry.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon1)
        self.prevEntry.setObjectName("prevEntry")
        self.nextEntry = QtGui.QPushButton(self.frame_2)
        self.nextEntry.setGeometry(QtCore.QRect(170, 10, 71, 33))
        self.nextEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.nextEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.nextEntry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon2)
        self.nextEntry.setObjectName("nextEntry")
        self.lastEntry = QtGui.QPushButton(self.frame_2)
        self.lastEntry.setGeometry(QtCore.QRect(250, 10, 71, 33))
        self.lastEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.lastEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.lastEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon3)
        self.lastEntry.setObjectName("lastEntry")
        self.frame = QtGui.QFrame(managerEntryDlg)
        self.frame.setGeometry(QtCore.QRect(460, 170, 281, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addEntry = QtGui.QPushButton(self.frame)
        self.addEntry.setGeometry(QtCore.QRect(10, 10, 80, 33))
        self.addEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.addEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon4)
        self.addEntry.setObjectName("addEntry")
        self.deleteEntry = QtGui.QPushButton(self.frame)
        self.deleteEntry.setGeometry(QtCore.QRect(100, 10, 80, 33))
        self.deleteEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.deleteEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon5)
        self.deleteEntry.setObjectName("deleteEntry")
        self.closeButton = QtGui.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(190, 10, 80, 33))
        self.closeButton.setMinimumSize(QtCore.QSize(80, 33))
        self.closeButton.setMaximumSize(QtCore.QSize(80, 33))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon6)
        self.closeButton.setObjectName("closeButton")
        self.line = QtGui.QFrame(managerEntryDlg)
        self.line.setGeometry(QtCore.QRect(390, 10, 20, 151))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtGui.QWidget(managerEntryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.mgrID_display = QtGui.QLineEdit(self.layoutWidget)
        self.mgrID_display.setMaximumSize(QtCore.QSize(81, 27))
        self.mgrID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.mgrID_display.setReadOnly(True)
        self.mgrID_display.setObjectName("mgrID_display")
        self.gridLayout.addWidget(self.mgrID_display, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.mgrFirstNameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.mgrFirstNameEdit.setMinimumSize(QtCore.QSize(219, 27))
        self.mgrFirstNameEdit.setMaximumSize(QtCore.QSize(219, 27))
        self.mgrFirstNameEdit.setObjectName("mgrFirstNameEdit")
        self.gridLayout.addWidget(self.mgrFirstNameEdit, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.mgrLastNameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.mgrLastNameEdit.setMinimumSize(QtCore.QSize(219, 27))
        self.mgrLastNameEdit.setMaximumSize(QtCore.QSize(219, 27))
        self.mgrLastNameEdit.setObjectName("mgrLastNameEdit")
        self.gridLayout.addWidget(self.mgrLastNameEdit, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.mgrNicknameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.mgrNicknameEdit.setMinimumSize(QtCore.QSize(219, 27))
        self.mgrNicknameEdit.setMaximumSize(QtCore.QSize(219, 27))
        self.mgrNicknameEdit.setObjectName("mgrNicknameEdit")
        self.gridLayout.addWidget(self.mgrNicknameEdit, 3, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(managerEntryDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(420, 10, 361, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.mgrDOBEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.mgrDOBEdit.setMinimumSize(QtCore.QSize(91, 27))
        self.mgrDOBEdit.setMaximumSize(QtCore.QSize(91, 27))
        self.mgrDOBEdit.setObjectName("mgrDOBEdit")
        self.gridLayout_2.addWidget(self.mgrDOBEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.mgrConfedSelect = QtGui.QComboBox(self.layoutWidget1)
        self.mgrConfedSelect.setMinimumSize(QtCore.QSize(241, 31))
        self.mgrConfedSelect.setMaximumSize(QtCore.QSize(241, 31))
        self.mgrConfedSelect.setObjectName("mgrConfedSelect")
        self.gridLayout_2.addWidget(self.mgrConfedSelect, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.mgrCountrySelect = QtGui.QComboBox(self.layoutWidget1)
        self.mgrCountrySelect.setMinimumSize(QtCore.QSize(241, 31))
        self.mgrCountrySelect.setMaximumSize(QtCore.QSize(241, 31))
        self.mgrCountrySelect.setObjectName("mgrCountrySelect")
        self.gridLayout_2.addWidget(self.mgrCountrySelect, 2, 1, 1, 1)
        self.label.setBuddy(self.mgrID_display)
        self.label_4.setBuddy(self.mgrFirstNameEdit)
        self.label_5.setBuddy(self.mgrLastNameEdit)
        self.label_6.setBuddy(self.mgrNicknameEdit)
        self.label_7.setBuddy(self.mgrDOBEdit)
        self.label_2.setBuddy(self.mgrConfedSelect)
        self.label_3.setBuddy(self.mgrCountrySelect)

        self.retranslateUi(managerEntryDlg)
        QtCore.QMetaObject.connectSlotsByName(managerEntryDlg)

    def retranslateUi(self, managerEntryDlg):
        managerEntryDlg.setWindowTitle(QtGui.QApplication.translate("managerEntryDlg", "Manager Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("managerEntryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("managerEntryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Close Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("managerEntryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;First Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrFirstNameEdit.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Manager first name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;Last Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrLastNameEdit.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Manager surname", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nic&amp;kname</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrNicknameEdit.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Nickname of manager, if applicable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Date of &amp;Birth</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrDOBEdit.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Birthdate (YYYY-MM-DD)", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrDOBEdit.setInputMask(QtGui.QApplication.translate("managerEntryDlg", "9999-99-99; ", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrDOBEdit.setText(QtGui.QApplication.translate("managerEntryDlg", "1901-01-01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;Region</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrConfedSelect.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Football confederation of manager\'s country", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("managerEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Cou&amp;ntry</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mgrCountrySelect.setToolTip(QtGui.QApplication.translate("managerEntryDlg", "Manager\'s country", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
