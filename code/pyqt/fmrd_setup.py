#!/usr/bin/env python
#
#    Desktop-based data entry tool for the Football Match Result Database (FMRD)
# 
#    Copyright (C) 2010-2011, Howard Hamilton
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from FmrdAdmin import *
from FmrdLib import (Constants, MsgPrompts)
from FmrdLib.CustomDelegates import *
from FmrdLib.CheckTables import *


""" 
Contains classes that implement entry forms to administrative tables of FMRD.

These tables are pre-loaded when the database is initially set up, so they do not 
need to be changed by the user.  With exception of About window, these 
modules would be incorporated only into an administration version of the tool. 

Classes:
CardSetupDlg -- data entry to Disciplinary Card table
ConfedSetupDlg -- data entry to Confederations table
CountrySetupDlg -- data entry to Countries table
FieldPosSetupDlg -- data entry to Field Positions table
FlankPosSetupDlg -- data entry to Flank Positions table
FoulSetupDlg -- data entry to Fouls table
GoalEventSetupDlg -- data entry to Goal Events table
GoalStrikeSetupDlg -- data entry to Goal Strikes table
GroupSetupDlg -- data entry to Groups table
GroupRoundSetupDlg -- data entry to Group Rounds table
KnockoutRoundSetupDlg -- data entry to Knockout Rounds table
MatchdaySetupDlg -- data entry to Matchdays table
PenSetupDlg -- data entry to Penalty Outcomes table
PhaseSetupDlg -- data entry to Competition Phases table
PosSetupDlg -- data entry to Positions table
RoundSetupDlg -- data entry to Rounds table
TimeZoneSetupDlg -- data entry to Time Zones table
VenueSurfaceSetupDlg -- data entry to Venue Surfaces table
WxCondSetupDlg -- data entry to Weather Conditions table

"""

class CardSetupDlg(QDialog, ui_cardsetup.Ui_CardSetupDlg):
    """Implements card data entry dialog, and accesses and writes to Disciplinary Card table."""

    ID,  DESC = range(2)
    
    def __init__(self, parent=None):
        """Constructor for CardSetupDlg class."""
        super(CardSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_cards")
        self.model.setSort(CardSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.cardID_display, CardSetupDlg.ID)
        self.mapper.addMapping(self.cardtypeEdit, CardSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.cardID_display.setDisabled(True)
            self.cardtypeEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
        
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window.
       
       First, tests whether a duplicate record already exists, and if not, seeks delete
       confirmation from user.
       """
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("card_type", self.model.tableName(), self.cardtypeEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.cardtypeEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form.
        
        Change is submitted only if duplicate record does not already exist in database.
        """
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("card_type", self.model.tableName(), self.cardtypeEdit.text()):        
                if not self.mapper.submit():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.cardtypeEdit.text())
                self.mapper.revert()
                return
        
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("card_type", self.model.tableName(), self.cardtypeEdit.text()):        
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                        return
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.cardtypeEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(card_id) FROM tbl_cards"))
        if query.next():
            maxCardID= query.value(0).toInt()[0]
            if not maxCardID:
                card_id = Constants.MinCardID
            else:
                card_id = QString()
                card_id.setNum(maxCardID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to cardID field
        self.cardID_display.setText(card_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.cardID_display.setEnabled(True)
        self.cardtypeEdit.setEnabled(True)
        # initialize form widgets
        self.cardtypeEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the card record is not being referenced in the Offenses table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_offenses"]
        fieldName = "card_id"
        card_id = self.cardID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, card_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, CardSetupDlg.DESC)        
            if self.cardtypeEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class FoulSetupDlg(QDialog, ui_foulsetup.Ui_FoulSetupDlg):
    """ Implements fouls data entry dialog, and accesses and writes to Fouls table. """

    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        """Constructor for FoulSetupDlg class."""
        super(FoulSetupDlg, self).__init__(parent)
        self.setupUi(self)
 
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_fouls")
        self.model.setSort(FoulSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.foulID_display, FoulSetupDlg.ID)
        self.mapper.addMapping(self.foulDescEdit, FoulSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.foulID_display.setDisabled(True)
            self.foulDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("foul_desc", self.model.tableName(), self.foulDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.foulDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("foul_desc", self.model.tableName(), self.foulDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.foulDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("foul_desc", self.model.tableName(), self.foulDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.foulDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(foul_id) FROM tbl_fouls"))
        if query.next():
            maxFoulID= query.value(0).toInt()[0]
            if not maxFoulID:
                foul_id = Constants.MinFoulID
            else:
                foul_id = QString()
                foul_id.setNum(maxFoulID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to foulID field
        self.foulID_display.setText(foul_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.foulID_display.setEnabled(True)
        self.foulDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.foulDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the foul record is not being referenced in any of the following tables:
            - Penalties table
            - Fouls table
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_penalties", "tbl_fouls"]
        fieldName = "foul_id"
        foul_id = self.foulID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, foul_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
        
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, FoulSetupDlg.DESC)        
            if self.foulDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class GroupSetupDlg(QDialog, ui_groupsetup.Ui_GroupSetupDlg):
    """Implement group name data entry dialog, and accesses and writes to Groups table."""
    
    ID,  DESC = range(2)

    def __init__(self, parent=None):
        """Constructor for GroupSetupDlg class."""
        super(GroupSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_groups")
        self.model.setSort(GroupSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.groupID_display, GroupSetupDlg.ID)
        self.mapper.addMapping(self.groupDescEdit, GroupSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.groupID_display.setDisabled(True)
            self.groupDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("group_desc", self.model.tableName(), self.groupDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.groupDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("group_desc", self.model.tableName(), self.groupDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.groupDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("group_desc", self.model.tableName(), self.groupDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.groupDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(group_id) FROM tbl_groups"))
        if query.next():
            maxGroupID = query.value(0).toInt()[0]
            if not maxGroupID:
                outcome_id = Constants.MinGroupID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxGroupID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to GroupID field
        self.groupID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.groupID_display.setEnabled(True)
        self.groupDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.groupDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the group record is not being referenced in the Group Matches table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_groupmatches"]
        fieldName = "group_id"
        group_id = self.groupID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, group_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, GroupSetupDlg.DESC)        
            if self.groupDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False
        

class MatchdaySetupDlg(QDialog, ui_matchdaysetup.Ui_MatchdaySetupDlg):
    """Implement matchday description (knockout stage) data entry dialog, and accesses and writes to Matchdays table."""
    
    ID,  DESC = range(2)

    def __init__(self, parent=None):
        """Constructor for MatchdaySetupDlg class."""
        super(MatchdaySetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_matchdays")
        self.model.setSort(MatchdaySetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.matchdayID_display, MatchdaySetupDlg.ID)
        self.mapper.addMapping(self.matchdayDescEdit, MatchdaySetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.matchdayID_display.setDisabled(True)
            self.matchdayDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("matchday_desc", self.model.tableName(), self.matchdayDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.matchdayDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("matchday_desc", self.model.tableName(), self.matchdayDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.matchdayDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("matchday_desc", self.model.tableName(), self.matchdayDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.matchdayDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(matchday_id) FROM tbl_matchdays"))
        if query.next():
            maxMatchdayID = query.value(0).toInt()[0]
            if not maxMatchdayID:
                outcome_id = Constants.MinMatchdayID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxMatchdayID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to MatchdayID field
        self.matchdayID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.matchdayID_display.setEnabled(True)
        self.matchdayDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.matchdayDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the matchday record is not being referenced in the Knockout Matches table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_knockoutmatches"]
        fieldName = "knockout_id"
        matchday_id = self.matchdayID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, matchday_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, MatchdaySetupDlg.DESC)        
            if self.matchdayDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class GroupRoundSetupDlg(QDialog, ui_grproundsetup.Ui_GroupRoundSetupDlg):
    """Implement round description (group stage) data entry dialog, and accesses and writes to Group Rounds table."""
    
    ID,  DESC = range(2)

    def __init__(self, parent=None):
        """Constructor for GroupRoundSetupDlg class."""
        super(GroupRoundSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_grouprounds")
        self.model.setSort(GroupRoundSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.grproundID_display, GroupRoundSetupDlg.ID)
        self.mapper.addMapping(self.grproundDescEdit, GroupRoundSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.grproundID_display.setDisabled(True)
            self.grproundDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("grpround_desc", self.model.tableName(), self.grproundDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.grproundDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("grpround_desc", self.model.tableName(), self.grproundDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.grproundDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("grpround_desc", self.model.tableName(), self.grproundDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.grproundDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(grpround_id) FROM tbl_grouprounds"))
        if query.next():
            maxGroupRoundID = query.value(0).toInt()[0]
            if not maxGroupRoundID:
                outcome_id = Constants.MinGroupRoundID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxGroupRoundID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to grpRoundID field
        self.grproundID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.grproundID_display.setEnabled(True)
        self.grproundDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.grproundDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the group round name record is not being referenced in the Group Matches table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_groupmatches"]
        fieldName = "grpround_id"
        grpround_id = self.grproundID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, grpround_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, GroupRoundSetupDlg.DESC)        
            if self.grproundDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class KnockoutRoundSetupDlg(QDialog, ui_koroundsetup.Ui_KnockoutRoundSetupDlg):
    """Implement knockout round name data entry dialog, and accesses and writes to Knockout Rounds table."""
    
    ID,  DESC = range(2)

    def __init__(self, parent=None):
        """Constructor for KnockoutRoundSetupDlg class."""
        super(KnockoutRoundSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_knockoutrounds")
        self.model.setSort(KnockoutRoundSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.koroundID_display, KnockoutRoundSetupDlg.ID)
        self.mapper.addMapping(self.koroundDescEdit, KnockoutRoundSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.koroundID_display.setDisabled(True)
            self.koroundDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("koround_desc", self.model.tableName(), self.koroundDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.koroundDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("koround_desc", self.model.tableName(), self.koroundDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.koroundDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("koround_desc", self.model.tableName(), self.koroundDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.koroundDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(koround_id) FROM tbl_knockoutrounds"))
        if query.next():
            maxKnockoutRoundID = query.value(0).toInt()[0]
            if not maxKnockoutRoundID:
                outcome_id = Constants.MinKnockoutRoundID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxKnockoutRoundID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to penOutcomeID field
        self.koroundID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.koroundID_display.setEnabled(True)
        self.koroundDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.koroundDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the knockout round record is not being referenced in the Knockout Matches table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_knockoutmatches"]
        fieldName = "koround_id"
        koround_id = self.koroundID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, koround_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, KnockoutRoundSetupDlg.DESC)        
            if self.koroundDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class PhaseSetupDlg(QDialog, ui_phasesetup.Ui_PhaseSetupDlg):
    """Implement phase name data entry dialog, and accesses and writes to Phases table."""
    
    ID,  DESC = range(2)

    def __init__(self, parent=None):
        """Constructor for PhaseSetupDlg class."""
        super(PhaseSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_phases")
        self.model.setSort(PhaseSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.phaseID_display, PhaseSetupDlg.ID)
        self.mapper.addMapping(self.phaseDescEdit, PhaseSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.phaseID_display.setDisabled(True)
            self.phaseDescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("phase_desc", self.model.tableName(), self.phaseDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.phaseDescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("phase_desc", self.model.tableName(), self.phaseDescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.phaseDescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("phase_desc", self.model.tableName(), self.phaseDescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.phaseDescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(phase_id) FROM tbl_phases"))
        if query.next():
            maxPhaseID = query.value(0).toInt()[0]
            if not maxPhaseID:
                outcome_id = Constants.MinPhaseID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxPhaseID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to phaseID field
        self.phaseID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.phaseID_display.setEnabled(True)
        self.phaseDescEdit.setEnabled(True)
        
        # initialize form widgets
        self.phaseDescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the phase record is not being referenced in the Matches table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_matches"]
        fieldName = "phase_id"
        phase_id = self.phaseID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, phase_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, PhaseSetupDlg.DESC)        
            if self.phaseDescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class PenSetupDlg(QDialog, ui_penoutcomesetup.Ui_PenSetupDlg):
    """ Implements penalty outcome data entry dialog, and accesses and writes to Penalty Outcomes table. """
    
    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        """Constructor for PenSetupDlg class."""
        super(PenSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_penoutcomes")
        self.model.setSort(PenSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.penoutcomeID_display, PenSetupDlg.ID)
        self.mapper.addMapping(self.penOutcomeEdit, PenSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.penoutcomeID_display.setDisabled(True)
            self.penOutcomeEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("po_desc", self.model.tableName(), self.penOutcomeEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.penOutcomeEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("po_desc", self.model.tableName(), self.penOutcomeEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.penOutcomeEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("po_desc", self.model.tableName(), self.penOutcomeEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.penOutcomeEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(penoutcome_id) FROM tbl_penoutcomes"))
        if query.next():
            maxPenOutcomeID = query.value(0).toInt()[0]
            if not maxPenOutcomeID:
                outcome_id = Constants.MinPenOutcomeID
            else:
                outcome_id = QString()
                outcome_id.setNum(maxPenOutcomeID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to penOutcomeID field
        self.penoutcomeID_display.setText(outcome_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.penoutcomeID_display.setEnabled(True)
        self.penOutcomeEdit.setEnabled(True)
        
        # initialize form widgets
        self.penOutcomeEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the penalty outcome record is not being referenced in any of the following tables:
            - Penalties table
            - PenaltyShootouts table
        If it is not being referenced in the dependent tables, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_penalties", "tbl_penaltyshootouts"]
        fieldName = "penoutcome_id"
        penoutcome_id = self.penoutcomeID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, penoutcome_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, PenSetupDlg.DESC)        
            if self.penOutcomeEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class GoalEventSetupDlg(QDialog, ui_goaleventsetup.Ui_GoalEventSetupDlg):
    """Implements goal data entry dialog, and accesses and writes to Goal Events table."""
    
    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        """Constructor for GoalEventSetupDlg class."""
        super(GoalEventSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_goalevents")
        self.model.setSort(GoalEventSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.goaleventID_display, GoalEventSetupDlg.ID)
        self.mapper.addMapping(self.goaleventEdit, GoalEventSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.goaleventID_display.setDisabled(True)
            self.goaleventEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("gte_desc", self.model.tableName(), self.goaleventEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goaleventEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("gte_desc", self.model.tableName(), self.goaleventEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goaleventEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):        
        """Adds new record at end of entry list."""                        
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("gte_desc", self.model.tableName(), self.goaleventEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goaleventEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(gtetype_id) FROM tbl_goalevents"))
        if query.next():
            maxGoalEventID= query.value(0).toInt()[0]
            if not maxGoalEventID:
                event_id = Constants.MinGoalEventID
            else:
                event_id = QString()
                event_id.setNum(maxGoalEventID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to GoalEventID field
        self.goaleventID_display.setText(event_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.goaleventID_display.setEnabled(True)
        self.goaleventEdit.setEnabled(True)
        
        # initialize form widgets
        self.goaleventEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the goal event record is not being referenced in the Goals table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_goals"]
        fieldName = "gtetype_id"
        gtetype_id = self.goaleventID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, gtetype_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, GoalEventSetupDlg.DESC)        
            if self.goaleventEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False            


class GoalStrikeSetupDlg(QDialog, ui_goalstrikesetup.Ui_GoalStrikeSetupDlg):
    """Implements goal strike data entry dialog, and accesses and writes Goal Strikes table."""
    
    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        super(GoalStrikeSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_goalstrikes")
        self.model.setSort(GoalStrikeSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.goalstrikeID_display, GoalStrikeSetupDlg.ID)
        self.mapper.addMapping(self.goalstrikeEdit, GoalStrikeSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.goalstrikeID_display.setDisabled(True)
            self.goalstrikeEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("gts_desc", self.model.tableName(), self.goalstrikeEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goalstrikeEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("gts_desc", self.model.tableName(), self.goalstrikeEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goalstrikeEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("gts_desc", self.model.tableName(), self.goalstrikeEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.goalstrikeEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(gtstype_id) FROM tbl_goalstrikes"))
        if query.next():
            maxGoalStrikeID= query.value(0).toInt()[0]
            if not maxGoalStrikeID:
                strike_id = Constants.MinGoalStrikeID
            else:
                strike_id = QString()
                strike_id.setNum(maxGoalStrikeID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to goalStrikeID field
        self.goalstrikeID_display.setText(strike_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.goalstrikeID_display.setEnabled(True)
        self.goalstrikeEdit.setEnabled(True)
        
        # initialize form widgets
        self.goalstrikeEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the goal strike record is not being referenced in the Goals table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_goals"]
        fieldName = "gtstype_id"
        gtstype_id = self.goalstrikeID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, gtstype_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
        
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, GoalStrikeSetupDlg.DESC)        
            if self.goalstrikeEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False            
        

class FieldPosSetupDlg(QDialog, ui_fieldpossetup.Ui_FieldPosSetupDlg):
    """Implements field position data entry dialog, and accesses and writes to Field Names table."""
    
    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        """Constructor for FieldPosSetupDlg class."""
        super(FieldPosSetupDlg, self).__init__(parent)
        self.setupUi(self)

        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_fieldnames")
        self.model.setSort(FieldPosSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.fieldposID_display, FieldPosSetupDlg.ID)
        self.mapper.addMapping(self.fieldposEdit, FieldPosSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.fieldposID_display.setDisabled(True)
            self.fieldposEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
            
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("posfield_name", self.model.tableName(), self.fieldposEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.fieldposEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("posfield_name", self.model.tableName(), self.fieldposEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.fieldposEdit.text())
                self.mapper.revert()
                return
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("posfield_name", self.model.tableName(), self.fieldposEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.fieldposEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(posfield_id) FROM tbl_fieldnames"))
        if query.next():
            maxFieldID= query.value(0).toInt()[0]
            if not maxFieldID:
                field_id = Constants.MinFieldID
            else:
                field_id = QString()
                field_id.setNum(maxFieldID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to fieldposID field
        self.fieldposID_display.setText(field_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.fieldposID_display.setEnabled(True)
        self.fieldposEdit.setEnabled(True)
        
        # initialize form widgets
        self.fieldposEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the field position record is not being referenced in the Positions table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_positions"]
        fieldName = "posfield_id"
        field_id = self.fieldposID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, field_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                                
        else:
            DeletionErrorPrompt(self)

    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, FieldPosSetupDlg.DESC)        
            if self.fieldposEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class FlankPosSetupDlg(QDialog, ui_flankpossetup.Ui_FlankPosSetupDlg):
    """Implements flank position data entry dialog, and accesses and writes to Flank Names table."""
    
    ID,  DESC = range(2)
 
    def __init__(self, parent=None):
        """Constructor of FlankPosSetupDlg class."""
        super(FlankPosSetupDlg, self).__init__(parent)
        self.setupUi(self)

        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_flanknames")
        self.model.setSort(FlankPosSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        localDelegate = GenericDelegate(self)
        localDelegate.insertColumnDelegate(FlankPosSetupDlg.DESC, NullLineEditDelegate())
        self.mapper.setItemDelegate(localDelegate)        
        self.mapper.addMapping(self.flankposID_display, FlankPosSetupDlg.ID)
        self.mapper.addMapping(self.flankposEdit, FlankPosSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.flankposID_display.setDisabled(True)
            self.flankposEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
            
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("posflank_name", self.model.tableName(), self.flankposEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.flankposEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("posflank_name", self.model.tableName(), self.flankposEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.flankposEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)

        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        

    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("posflank_name", self.model.tableName(), self.flankposEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.flankposEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(posflank_id) FROM tbl_flanknames"))
        if query.next():
            maxFlankID= query.value(0).toInt()[0]
            if not maxFlankID:
                flank_id = Constants.MinFlankID
            else:
                flank_id = QString()
                flank_id.setNum(maxFlankID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to flankposID field
        self.flankposID_display.setText(flank_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.flankposID_display.setEnabled(True)
        self.flankposEdit.setEnabled(True)
        
        # initialize form widgets
        self.flankposEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the flank position record is not being referenced in the Positions table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by dependent table, alert user.
        """
        
        childTableList = ["tbl_positions"]
        fieldName = "posflank_id"
        flank_id = self.flankposID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, flank_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)

    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, FlankPosSetupDlg.DESC)        
            if self.flankposEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


# Implements user interface to Position table, which links to Flank Position and Field Position tables.
class PosSetupDlg(QDialog, ui_positionsetup.Ui_PosSetupDlg):
    """Implements position data entry dialog, which accesses and writes to the Positions table.
    
    The player position is a composite of the flank descriptor and the field position.  Some positions do
    not have a field descriptor (goalkeeper), so the flank descriptor can be left blank.
    
    """
    
    POS_ID,  FIELD_ID,  FLANK_ID = range(3)    

    def __init__(self, parent=None):
        """Constructor to PosSetupDlg class."""
        super(PosSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("tbl_positions")
        self.model.setRelation(PosSetupDlg.FIELD_ID, QSqlRelation("tbl_fieldnames", "posfield_id", "posfield_name"))
        self.model.setRelation(PosSetupDlg.FLANK_ID, QSqlRelation("tbl_flanknames", "posflank_id", "posflank_name"))        
        self.model.setSort(PosSetupDlg.POS_ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.positionID_display, PosSetupDlg.POS_ID)
        # set up Field Position combobox that links to tbl_fieldnames
        fieldrelationModel = self.model.relationModel(PosSetupDlg.FIELD_ID)
        self.fieldposSelect.setModel(fieldrelationModel)
        self.fieldposSelect.setModelColumn(fieldrelationModel.fieldIndex("posfield_name"))        
        self.mapper.addMapping(self.fieldposSelect, PosSetupDlg.FIELD_ID)        
         # set up Flank Position combobox that links to tbl_flanknames
        flankrelationModel = self.model.relationModel(PosSetupDlg.FLANK_ID)
        self.flankposSelect.setModel(flankrelationModel)
        self.flankposSelect.setModelColumn(flankrelationModel.fieldIndex("posflank_name"))
        self.mapper.addMapping(self.flankposSelect, PosSetupDlg.FLANK_ID)        
        self.mapper.toFirst()         
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.positionID_display.setDisabled(True)
            self.fieldposSelect.setDisabled(True)
            self.flankposSelect.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)
        
    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if MsgPrompts.SaveDiscardOptionPrompt(self):
                if not self.mapper.submit():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
        QDialog.accept(self)
        
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if MsgPrompts.SaveDiscardOptionPrompt(self):
                if not self.mapper.submit():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                self.mapper.revert()
                return
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(position_id) FROM tbl_positions"))
        if query.next():
            maxPositionID = query.value(0).toInt()[0]
            if not maxPositionID:
                position_id = Constants.MinPositionID
            else:
                position_id = QString()
                position_id.setNum(maxPositionID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to PositionID field
        self.positionID_display.setText(position_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.positionID_display.setEnabled(True)
        self.flankposSelect.setEnabled(True)
        self.fieldposSelect.setEnabled(True)
        
        # initialize form widgets
        self.fieldposSelect.setCurrentIndex(-1)
        self.flankposSelect.setCurrentIndex(-1)
        
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the position record is not being referenced in any of the following tables:
            - Players table
            - Lineup table
        If it is not being referenced in any of the child tables, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by child tables, alert user.
        """
        
        childTableList = ["tbl_players", "tbl_lineups"]
        fieldName = "position_id"
        position_id = self.positionID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, position_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)

    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            editorList = (self.fieldposSelect, self.flankposSelect)
            columnList = (PosSetupDlg.FIELD_ID, PosSetupDlg.FLANK_ID)
            
            for editor, column in zip(editorList, columnList):
                index = self.model.index(row, column)        
                if editor.currentText() != self.model.data(index).toString():
                    return True
        return False


class CountrySetupDlg(QDialog, ui_countrysetup.Ui_CountrySetupDlg):
    """Implements country data entry dialog, which accesses and writes to Countries table.
    
    The country is linked with the confederation of which it is a member.
    
    """
    
    ID,  REGION_ID,  NAME = range(3)    
    
    def __init__(self, parent=None):
        """Constructor for CountrySetupDlg class."""
        super(CountrySetupDlg, self).__init__(parent)
        self.setupUi(self)         
        
        # define model
        # underlying database model
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("tbl_countries")
        self.model.setRelation(CountrySetupDlg.REGION_ID, QSqlRelation("tbl_confederations", "confed_id", "confed_name"))
        self.model.setSort(CountrySetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.countryID_display, CountrySetupDlg.ID)
        self.mapper.addMapping(self.countryEdit, CountrySetupDlg.NAME)        
         # set up combobox that links to foreign table
        relationModel = self.model.relationModel(CountrySetupDlg.REGION_ID)
        self.confedSelect.setModel(relationModel)
        self.confedSelect.setModelColumn(relationModel.fieldIndex("confed_name"))
        self.mapper.addMapping(self.confedSelect, CountrySetupDlg.REGION_ID)        
        self.mapper.toFirst()        
       
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.countryID_display.setDisabled(True)
            self.confedSelect.setDisabled(True)
            self.countryEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
            
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)

        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)
        
    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("cty_name", self.model.tableName(), self.countryEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.countryEdit.text())
        QDialog.accept(self)
        
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("cty_name", self.model.tableName(), self.countryEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.countryEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("cty_name", self.model.tableName(), self.countryEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.countryEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(country_id) FROM tbl_countries"))
        if query.next():
            maxCountryID= query.value(0).toInt()[0]
            if not maxCountryID:
                country_id = Constants.MinCountryID
            else:
                country_id = QString()
                country_id.setNum(maxCountryID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to countryID field
        self.countryID_display.setText(country_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.countryID_display.setEnabled(True)
        self.confedSelect.setEnabled(True)
        self.countryEdit.setEnabled(True)
        
        # initialize data widgets
        self.confedSelect.setCurrentIndex(-1)
        self.countryEdit.setFocus()
        
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the country record is not being referenced in any of the following tables:
            - Players table
            - Referees table
            - Managers table
            - Venues table
        If it is not being referenced in any of the child tables, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by child tables, alert user.
        """
        
        childTableList = ["tbl_players", "tbl_referees",  "tbl_managers",  "tbl_venues"]
        fieldName = "country_id"
        country_id = self.countryID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, country_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, CountrySetupDlg.NAME)        
            if self.countryEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class ConfedSetupDlg(QDialog, ui_confederationsetup.Ui_ConfedSetupDlg):
    """Implements confederation data entry dialog, which accesses and writes to Confederations table."""

    ID,  NAME = range(2)
    
    def __init__(self, parent=None):
        """Constructor for ConfedSetupDlg class."""
        super(ConfedSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_confederations")
        self.model.setSort(ConfedSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.confedID_display, ConfedSetupDlg.ID)
        self.mapper.addMapping(self.confederationEdit, ConfedSetupDlg.NAME)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.confedID_display.setDisabled(True)
            self.confederationEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
            
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("confed_name", self.model.tableName(), self.confederationEdit.text()):
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
        QDialog.accept(self)
        
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("confed_name", self.model.tableName(), self.confederationEdit.text()):        
                if not self.mapper.submit():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.confederationEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)

        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        

    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("confed_name", self.model.tableName(), self.confederationEdit.text()):        
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.confederationEdit.text())
                    self.mapper.revert()
                    return
        
        # move to end of table and insert new record
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(confed_id) FROM tbl_confederations"))
        if query.next():
            maxConfedID= query.value(0).toInt()[0]
            if not maxConfedID:
                confed_id = Constants.MinConfedID
            else:
                confed_id = QString()
                confed_id.setNum(maxConfedID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to confedID field
        self.confedID_display.setText(confed_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.confedID_display.setEnabled(True)
        self.confederationEdit.setEnabled(True)
        # initialize form widgets
        self.confederationEdit.setFocus()
        
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the confederation record is not being referenced in the Country table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by the dependent table, alert user.
        """
        
        childTableList = ["tbl_countries"]
        fieldName = "confed_id"
        confed_id = self.confedID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, confed_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)

    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, ConfedSetupDlg.NAME)        
            if self.confederationEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class TimeZoneSetupDlg(QDialog, ui_timezonesetup.Ui_TimeZoneSetupDlg):
    """Implements time zone data entry dialog, which accesses and writes to Time Zones table."""
    
    ID,  CONFED_ID, NAME, OFFSET = range(4)
    
    def __init__(self, parent=None):
        """Constructor for TimeZoneSetupDlg class."""
        super(TimeZoneSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        CONFED_NAME = 1
        
        # define model
        # underlying database model
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("tbl_timezones")
        self.model.setRelation(TimeZoneSetupDlg.CONFED_ID, QSqlRelation("tbl_confederations", "confed_id", "confed_name"))
        self.model.setSort(TimeZoneSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        localDelegate = GenericDelegate(self)
        localDelegate.insertColumnDelegate(TimeZoneSetupDlg.OFFSET, UTCOffsetDelegate())
        self.mapper.setItemDelegate(localDelegate)        
        self.mapper.addMapping(self.timezoneID_display, TimeZoneSetupDlg.ID)
        
         # set up combobox that links to Confederations table
        confedModel = self.model.relationModel(TimeZoneSetupDlg.CONFED_ID)
        confedModel.setSort(CONFED_NAME, Qt.AscendingOrder)
        self.tzRegionSelect.setModel(confedModel)
        self.tzRegionSelect.setModelColumn(confedModel.fieldIndex("confed_name"))        
        self.mapper.addMapping(self.tzRegionSelect, TimeZoneSetupDlg.CONFED_ID)
        
        # mapping other widgets to form
        self.mapper.addMapping(self.tzNameEdit, TimeZoneSetupDlg.NAME)
        self.mapper.addMapping(self.tzOffsetEdit, TimeZoneSetupDlg.OFFSET)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.timezoneID_display.setDisabled(True)
            self.tzNameEdit.setDisabled(True)
            self.tzRegionSelect.setDisabled(True)
            self.tzOffsetEdit.setDisabled(True)            
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("tz_name", self.model.tableName(), self.tzNameEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.tzNameEdit.text())
        QDialog.accept(self)
        
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("tz_name", self.model.tableName(), self.tzNameEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.tzNameEdit.text())
                self.mapper.revert()
                return
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("tz_name", self.model.tableName(), self.tzNameEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.tzNameEdit.text())
                    self.mapper.revert()
                    return
        
        # move to end of table and insert new record
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(timezone_id) FROM tbl_timezones"))
        if query.next():
            maxTimeZoneID= query.value(0).toInt()[0]
            if not maxTimeZoneID:
                timezone_id = Constants.MinTimeZoneID
            else:
                timezone_id = QString()
                timezone_id.setNum(maxTimeZoneID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to confedID field
        self.timezoneID_display.setText(timezone_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.timezoneID_display.setEnabled(True)
        self.tzNameEdit.setEnabled(True)
        self.tzRegionSelect.setEnabled(True)
        self.tzOffsetEdit.setEnabled(True)
        
        # initialize form widgets
        self.tzOffsetEdit.setText("0.00")
        self.tzRegionSelect.setCurrentIndex(-1)
        self.tzNameEdit.setFocus()
        
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the time zone record is not being referenced in the Venues table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by the dependent table, alert user.
        """
        
        childTableList = ["tbl_venues"]
        fieldName = "timezone_id"
        timezone_id = self.timezoneID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, timezone_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, TimeZoneSetupDlg.NAME)        
            if self.tzNameEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False



class VenueSurfaceSetupDlg(QDialog, ui_venuesurfacesetup.Ui_VenueSurfaceSetupDlg):
    """Implements field surface data entry dialog, and accesses and writes to Time Zones table."""
    
    ID,  DESC = range(2)
    
    def __init__(self, parent=None):
        """Constructor for VenueSurfaceSetupDlg class."""
        super(VenueSurfaceSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_venuesurfaces")
        self.model.setSort(VenueSurfaceSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.vensurfID_display, VenueSurfaceSetupDlg.ID)
        self.mapper.addMapping(self.vensurfNameEdit, VenueSurfaceSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.vensurfID_display.setDisabled(True)
            self.vensurfNameEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("vensurf_desc", self.model.tableName(), self.vensurfNameEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.vensurfNameEdit.text())
                self.mapper.revert()
                return
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("vensurf_desc", self.model.tableName(), self.vensurfNameEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.vensurfNameEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("vensurf_desc", self.model.tableName(), self.vensurfNameEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.vensurfNameEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(venuesurface_id) FROM tbl_venuesurfaces"))
        if query.next():
            maxSurfaceID = query.value(0).toInt()[0]
            if not maxSurfaceID:
                surface_id = Constants.MinSurfaceID
            else:
                surface_id = QString()
                surface_id.setNum(maxRoundID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to SurfaceID field
        self.vensurfID_display.setText(surface_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.vensurfID_display.setEnabled(True)
        self.vensurfNameEdit.setEnabled(True)
        
        # initialize form widgets
        self.vensurfNameEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the field surface record is not being referenced in the Venue History table.
        If it is not being referenced in the dependent table, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by the dependent table, alert user.
        """
        
        childTableList = ["tbl_venuehistory"]
        fieldName = "venuesurface_id"
        surface_id = self.vensurfID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, surface_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, VenueSurfaceSetupDlg.DESC)        
            if self.vensurfNameEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class RoundSetupDlg(QDialog, ui_roundsetup.Ui_RoundSetupDlg):
    """Implements matchday data entry dialog, and accesses and writes to Rounds table."""
    
    ID,  DESC = range(2)
    
    def __init__(self, parent=None):
        """Constructor for RoundSetupDlg class."""
        super(RoundSetupDlg, self).__init__(parent)
        self.setupUi(self)
        
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_rounds")
        self.model.setSort(RoundSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.roundID_display, RoundSetupDlg.ID)
        self.mapper.addMapping(self.rounddescEdit, RoundSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.roundID_display.setDisabled(True)
            self.rounddescEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)
    
    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("round_desc", self.model.tableName(), self.rounddescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.rounddescEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("round_desc", self.model.tableName(), self.rounddescEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.rounddescEdit.text())
                self.mapper.revert()
                return
                
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("round_desc", self.model.tableName(), self.rounddescEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.rounddescEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(round_id) FROM tbl_rounds"))
        if query.next():
            maxRoundID = query.value(0).toInt()[0]
            if not maxRoundID:
                round_id = Constants.MinRoundID
            else:
                round_id = QString()
                round_id.setNum(maxRoundID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to RoundID field
        self.roundID_display.setText(round_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.roundID_display.setEnabled(True)
        self.rounddescEdit.setEnabled(True)
        
        # initialize form widgets
        self.rounddescEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the matchday record is not being referenced in any of the following tables:
            - LeagueMatches linking table
            - GroupMatches linking table
            - PenaltyShootouts table
        If it is not being referenced in the dependent tables, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by the dependent table, alert user.
        """
        
        childTableList = ["tbl_leaguematches",  "tbl_groupmatches", "tbl_penaltyshootouts"]
        fieldName = "round_id"
        round_id = self.roundID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, round_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)

    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, RoundSetupDlg.DESC)        
            if self.rounddescEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False


class WxCondSetupDlg(QDialog, ui_weathersetup.Ui_WxCondSetupDlg):
    """Implements weather condition data entry dialog, accesses and writes to WeatherConditions table."""
    
    ID,  DESC = range(2)
    
    def __init__(self, parent=None):
        """Constructor for WxCondSetupDlg class."""
        super(WxCondSetupDlg, self).__init__(parent)
        self.setupUi(self)
 
        # define model
        # underlying database model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_weather")
        self.model.setSort(WxCondSetupDlg.ID, Qt.AscendingOrder)
        self.model.select()
        
        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.weatherID_display, WxCondSetupDlg.ID)
        self.mapper.addMapping(self.wxcondEdit, WxCondSetupDlg.DESC)
        self.mapper.toFirst()
        
        # disable all fields if no records in database table
        if not self.model.rowCount():
            self.weatherID_display.setDisabled(True)
            self.wxcondEdit.setDisabled(True)
            # disable save and delete buttons
            self.saveEntry.setDisabled(True)
            self.deleteEntry.setDisabled(True)
        
        # disable First and Previous Entry buttons
        self.firstEntry.setDisabled(True)
        self.prevEntry.setDisabled(True)
        
        # disable Next and Last Entry buttons if less than two records
        if self.model.rowCount() < 2:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            
        # configure signal/slot
        self.connect(self.firstEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.FIRST))
        self.connect(self.prevEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.PREV))
        self.connect(self.nextEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NEXT))
        self.connect(self.lastEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.LAST))
        self.connect(self.saveEntry, SIGNAL("clicked()"), lambda: self.saveRecord(Constants.NULL))
        self.connect(self.addEntry, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteEntry, SIGNAL("clicked()"), self.deleteRecord)        
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

    def accept(self):
        """Submits changes to database and closes window upon confirmation from user."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("wx_conditiondesc", self.model.tableName(), self.wxcondEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.wxcondEdit.text())
        QDialog.accept(self)
    
    def saveRecord(self, where):
        """Submits changes to database and navigates through form."""
        row = self.mapper.currentIndex()
        if self.isDirty(row):
            if not CheckDuplicateRecords("wx_conditiondesc", self.model.tableName(), self.wxcondEdit.text()):        
                if MsgPrompts.SaveDiscardOptionPrompt(self):
                    if not self.mapper.submit():
                        MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
            else:
                MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.wxcondEdit.text())
                self.mapper.revert()
                return
        if where == Constants.FIRST:
            self.firstEntry.setDisabled(True)
            self.prevEntry.setDisabled(True)
            if not self.nextEntry.isEnabled():
                self.nextEntry.setEnabled(True)
                self.lastEntry.setEnabled(True)
            row = 0
        elif where == Constants.PREV:
            row -= 1
            if not self.nextEntry.isEnabled():
                    self.nextEntry.setEnabled(True)
                    self.lastEntry.setEnabled(True)   
            if row == 0:
                self.firstEntry.setDisabled(True)
                self.prevEntry.setDisabled(True)                
        elif where == Constants.NEXT:
            row += 1
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            if row >= self.model.rowCount() - 1:
                self.nextEntry.setDisabled(True)
                self.lastEntry.setDisabled(True)
                row = self.model.rowCount() - 1
        elif where == Constants.LAST:
            self.nextEntry.setDisabled(True)
            self.lastEntry.setDisabled(True)
            if not self.prevEntry.isEnabled():
                self.prevEntry.setEnabled(True)
                self.firstEntry.setEnabled(True)
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
        # enable Delete button if at least one record
        if self.model.rowCount():
            self.deleteEntry.setEnabled(True)        
        
    def addRecord(self):
        """Adds new record at end of entry list."""                
        # save current index if valid
        row = self.mapper.currentIndex()
        if row != -1:
            if self.isDirty(row):
                if not CheckDuplicateRecords("wx_conditiondesc", self.model.tableName(), self.wxcondEdit.text()):        
                    if MsgPrompts.SaveDiscardOptionPrompt(self):
                        if not self.mapper.submit():
                            MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                else:
                    MsgPrompts.DuplicateRecordErrorPrompt(self, self.model.tableName(), self.wxcondEdit.text())
                    self.mapper.revert()
                    return
        
        row = self.model.rowCount()
        query = QSqlQuery()
        query.exec_(QString("SELECT MAX(weather_id) FROM tbl_weather"))
        if query.next():
            maxWeatherID = query.value(0).toInt()[0]
            if not maxWeatherID:
                weather_id = Constants.MinWeatherID
            else:
                weather_id = QString()
                weather_id.setNum(maxWeatherID+1)          
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)

        # assign value to WeatherID field
        self.weatherID_display.setText(weather_id)
        
        # disable next/last navigation buttons
        self.nextEntry.setDisabled(True)
        self.lastEntry.setDisabled(True)
        # enable first/previous navigation buttons
        if self.model.rowCount() > 1:
            self.prevEntry.setEnabled(True)
            self.firstEntry.setEnabled(True)
            # enable Delete button if at least one record
            self.deleteEntry.setEnabled(True)
            
        # enable Save button
        if not self.saveEntry.isEnabled():
            self.saveEntry.setEnabled(True)
        
        # enable form widgets
        self.weatherID_display.setEnabled(True)
        self.wxcondEdit.setEnabled(True)
        
        # initialize form widgets
        self.wxcondEdit.setFocus()
    
    def deleteRecord(self):
        """Deletes record from database upon user confirmation.
        
        First, check that the weather condition record is not being referenced in any of the following tables:
            - WeatherKickoff linking table
            - WeatherHalftime linking table
            - WeatherFulltime linking table
        If it is not being referenced in any of the child tables, ask for user confirmation and delete 
        record upon positive confirmation.  If it is being referenced by child tables, alert user.
        """
        
        childTableList = ["tbl_weatherkickoff", "tbl_weatherhalftime", "tbl_weatherfulltime"]
        fieldName = "weather_id"
        weather_id = self.weatherID_display.text()
        
        if not CountChildRecords(childTableList, fieldName, weather_id):
            if QMessageBox.question(self, QString("Delete Record"), 
                                                QString("Delete current record?"), 
                                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
            else:
                row = self.mapper.currentIndex()
                self.model.removeRow(row)
                if not self.model.submitAll():
                    MsgPrompts.DatabaseCommitErrorPrompt(self, self.model.lastError())
                    return
                if row + 1 >= self.model.rowCount():
                    row = self.model.rowCount() - 1
                self.mapper.setCurrentIndex(row) 
                # disable Delete button if no records in database
                if not self.model.rowCount():
                    self.deleteEntry.setDisabled(True)                
        else:
            DeletionErrorPrompt(self)
            
    def isDirty(self, row):
        """Compares current state of data entry form to current record in database, and returns a boolean.
        
        Arguments:
            row: current record in mapper and model
        
        Returns:
            TRUE: there are changes between data entry form and current record in database,
                      or new record in database
            FALSE: no changes between data entry form and current record in database
        """
        if row == self.model.rowCount():
            return True
        else:
            index = self.model.index(row, WxCondSetupDlg.DESC)        
            if self.wxcondEdit.text() != self.model.data(index).toString():
                return True
            else:
                return False
