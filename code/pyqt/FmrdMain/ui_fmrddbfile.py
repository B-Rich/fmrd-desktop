# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/fmrd_dbfile.ui'
#
# Created: Sun Dec 18 17:05:11 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DBFileLoadDlg(object):
    def setupUi(self, DBFileLoadDlg):
        DBFileLoadDlg.setObjectName("DBFileLoadDlg")
        DBFileLoadDlg.resize(240, 120)
        DBFileLoadDlg.setMinimumSize(QtCore.QSize(240, 120))
        DBFileLoadDlg.setMaximumSize(QtCore.QSize(240, 120))
        self.widget = QtGui.QWidget(DBFileLoadDlg)
        self.widget.setGeometry(QtCore.QRect(30, -3, 186, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userButton = QtGui.QRadioButton(self.widget)
        self.userButton.setMinimumSize(QtCore.QSize(60, 30))
        self.userButton.setMaximumSize(QtCore.QSize(60, 30))
        self.userButton.setChecked(True)
        self.userButton.setObjectName("userButton")
        self.horizontalLayout.addWidget(self.userButton)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.adminButton = QtGui.QRadioButton(self.widget)
        self.adminButton.setMinimumSize(QtCore.QSize(75, 30))
        self.adminButton.setMaximumSize(QtCore.QSize(75, 30))
        self.adminButton.setObjectName("adminButton")
        self.horizontalLayout.addWidget(self.adminButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.openButton = QtGui.QPushButton(self.widget)
        self.openButton.setMinimumSize(QtCore.QSize(180, 30))
        self.openButton.setMaximumSize(QtCore.QSize(180, 30))
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setMinimumSize(QtCore.QSize(90, 30))
        self.cancelButton.setMaximumSize(QtCore.QSize(90, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DBFileLoadDlg)
        QtCore.QMetaObject.connectSlotsByName(DBFileLoadDlg)

    def retranslateUi(self, DBFileLoadDlg):
        DBFileLoadDlg.setWindowTitle(QtGui.QApplication.translate("DBFileLoadDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.userButton.setToolTip(QtGui.QApplication.translate("DBFileLoadDlg", "User switchboard", None, QtGui.QApplication.UnicodeUTF8))
        self.userButton.setText(QtGui.QApplication.translate("DBFileLoadDlg", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.adminButton.setToolTip(QtGui.QApplication.translate("DBFileLoadDlg", "Administrator switchboard", None, QtGui.QApplication.UnicodeUTF8))
        self.adminButton.setText(QtGui.QApplication.translate("DBFileLoadDlg", "Admin", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("DBFileLoadDlg", "&Open Database File", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DBFileLoadDlg", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

