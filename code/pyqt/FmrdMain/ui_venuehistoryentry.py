# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/venuehistory_entry.ui'
#
# Created: Fri Aug 26 15:09:20 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_VenueHistoryDlg(object):
    def setupUi(self, VenueHistoryDlg):
        VenueHistoryDlg.setObjectName("VenueHistoryDlg")
        VenueHistoryDlg.resize(720, 380)
        VenueHistoryDlg.setMinimumSize(QtCore.QSize(720, 380))
        VenueHistoryDlg.setMaximumSize(QtCore.QSize(720, 380))
        self.venueHistory = QtGui.QTableView(VenueHistoryDlg)
        self.venueHistory.setGeometry(QtCore.QRect(20, 50, 681, 261))
        self.venueHistory.setObjectName("venueHistory")
        self.frame = QtGui.QFrame(VenueHistoryDlg)
        self.frame.setGeometry(QtCore.QRect(20, 320, 681, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addEntry = QtGui.QPushButton(self.frame)
        self.addEntry.setGeometry(QtCore.QRect(10, 10, 80, 33))
        self.addEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.addEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon)
        self.addEntry.setObjectName("addEntry")
        self.deleteEntry = QtGui.QPushButton(self.frame)
        self.deleteEntry.setGeometry(QtCore.QRect(100, 10, 80, 33))
        self.deleteEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.deleteEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon1)
        self.deleteEntry.setObjectName("deleteEntry")
        self.closeButton = QtGui.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(590, 10, 80, 33))
        self.closeButton.setMinimumSize(QtCore.QSize(80, 33))
        self.closeButton.setMaximumSize(QtCore.QSize(80, 33))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(16, 16))
        self.closeButton.setObjectName("closeButton")
        self.layoutWidget = QtGui.QWidget(VenueHistoryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 0, 381, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(60, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.venueName_display = QtGui.QLineEdit(self.layoutWidget)
        self.venueName_display.setMinimumSize(QtCore.QSize(300, 30))
        self.venueName_display.setMaximumSize(QtCore.QSize(300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.venueName_display.setPalette(palette)
        self.venueName_display.setReadOnly(True)
        self.venueName_display.setObjectName("venueName_display")
        self.horizontalLayout.addWidget(self.venueName_display)

        self.retranslateUi(VenueHistoryDlg)
        QtCore.QMetaObject.connectSlotsByName(VenueHistoryDlg)

    def retranslateUi(self, VenueHistoryDlg):
        VenueHistoryDlg.setWindowTitle(QtGui.QApplication.translate("VenueHistoryDlg", "Surface/Capacity History", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("VenueHistoryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("VenueHistoryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("VenueHistoryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("VenueHistoryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("VenueHistoryDlg", "Close Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("VenueHistoryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VenueHistoryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Venue</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.venueName_display.setToolTip(QtGui.QApplication.translate("VenueHistoryDlg", "Venue name", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
