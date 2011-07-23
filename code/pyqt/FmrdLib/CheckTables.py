#!/usr/bin/env python
#
#    Football Match Result Database (FMRD)
#    Desktop-based data entry tool
#
#    Contains functions that count number of records in FMRD tables.
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
from FmrdLib import Constants

# Function: CheckMinimumCompetitions
#
# Check Competition table
# Returns TRUE if there is at least one record in 
# Competition table
def CheckMinimumCompetitions():
    
    CompetitionQuery = QSqlQuery()
    CompetitionQuery.prepare("SELECT COUNT(*) FROM tbl_competitions")
    CompetitionQuery.exec_()
    
    if CompetitionQuery.isActive():
        CompetitionQuery.next()
        numCompetitions = CompetitionQuery.value(0).toInt()[0]
        if numCompetitions >= Constants.MIN_COMPETITIONS:
            return 1
        else:
            return 0
    else:
        return 0

# Function: CheckMinimumTeams
#
# Check Teams table
# Returns TRUE if there are at least two records in Teams table
def CheckMinimumTeams():
    
    TeamsQuery = QSqlQuery()
    TeamsQuery.prepare("SELECT COUNT(*) FROM tbl_teams")
    TeamsQuery.exec_()
    
    if TeamsQuery.isActive():
        TeamsQuery.next()
        numTeams = TeamsQuery.value(0).toInt()[0]
        if numTeams >= Constants.MIN_TEAMS:
            return 1
        else:
            return 0
    else:
        return 0
    
# Function: CheckMinimumVenueHosts
#
# Check Teams table
# Returns TRUE if there is at least one record in Teams table
def CheckMinimumVenueHosts():
    
    HostsQuery = QSqlQuery()
    HostsQuery.prepare("SELECT COUNT(*) FROM tbl_teams")
    HostsQuery.exec_()
    
    if HostsQuery.isActive():
        HostsQuery.next()
        numHosts = HostsQuery.value(0).toInt()[0]
        if numHosts >= Constants.MIN_VENUEHOSTS:
            return 1
        else:
            return 0
    else:
        return 0
        
# Function: CheckMinimumManagers
#
# Check Managers table
# Returns TRUE if there are at least two records in Managers table
def CheckMinimumManagers():
    
    ManagerQuery = QSqlQuery()
    ManagerQuery.prepare("SELECT COUNT(*) FROM tbl_managers")
    ManagerQuery.exec_()

    if ManagerQuery.isActive():
        ManagerQuery.next()
        numManagers = ManagerQuery.value(0).toInt()[0]
        if numManagers >= Constants.MIN_MANAGERS:
            return 1
        else:
            return 0
    else:
        return 0

# Function: CheckMinimumReferees
#
# Check Referees table
# Returns TRUE if there is at least one referee in Referees table
def CheckMinimumReferees():
    
    RefereeQuery = QSqlQuery()
    RefereeQuery.prepare("SELECT COUNT(*) FROM tbl_referees")
    RefereeQuery.exec_()
    
    if RefereeQuery.isActive():
        RefereeQuery.next()
        numReferees = RefereeQuery.value(0).toInt()[0]
        if numReferees >= Constants.MIN_REFEREES:
            return 1
        else:
            return 0
    else:
        return 0


# Function: CheckMinimumMatchCriteria
#
# Call other functions to determine minimum criteria for match entry
# Returns TRUE only if ALL conditions are satisfied in tables:
#   -- at least one referee
#   -- at least two managers
#   -- at least two teams
#   -- at least one venue
#   -- at least one competition
def CheckMinimumMatchCriteria():
    
    if CheckMinimumCompetitions():
        if CheckMinimumVenueHosts() and CheckMinimumTeams():
                if CheckMinimumManagers() and CheckMinimumReferees():
                    return 1
                
    return 0

# Function: CheckMinimumLineups
#
# Check Lineup table
# Returns TRUE only if ALL conditions are satisfied in table:
#   -- at least 11 starting players
#   -- at least one designated captain
#   -- at least one goalkeeper among starting players
def CheckMinimumLineups():
        
    StartersQuery = QSqlQuery()
    StartersQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE lp_starting")
    StartersQuery.exec_()
    
    CaptainQuery = QSqlQuery()
    CaptainQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE lp_starting AND lp_captain")
    CaptainQuery.exec_()
    
    GoalkeeperQuery = QSqlQuery()
    GoalkeeperQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE lp_starting AND "
                                            "position_id IN (SELECT position_id from positions_list WHERE position_name = ?)")
    GoalkeeperQuery.addBindValue(QVariant("Goalkeeper"))
    GoalkeeperQuery.exec_()
    if StartersQuery.isActive() and CaptainQuery.isActive() and GoalkeeperQuery.isActive():
        StartersQuery.next()
        numStarters = StartersQuery.value(0).toInt()[0]
        
        CaptainQuery.next()
        numCaptains = CaptainQuery.value(0).toInt()[0]
        
        GoalkeeperQuery.next()
        numGoalkeepers = GoalkeeperQuery.value(0).toInt()[0]
        
        if (numStarters >= Constants.MIN_STARTERS) and \
        (numCaptains >= Constants.MIN_STARTING_CAPTAINS) and \
        (numGoalkeepers >= Constants.MIN_STARTING_GOALKEEPERS):
            return 1
        else:
            return 0
    else:
        return 0

# Function: CheckMinimumSubstitutes
#
# Check number of designated substitutes in Lineup table
# Returns TRUE only there are at least three substitutes 
# (non-starting players) in table
def CheckMinimumSubstitutes():
    
    SubstituteQuery = QSqlQuery()
    SubstituteQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE NOT lp_starting")
    SubstituteQuery.exec_()
    
    if SubstituteQuery.isActive():
        SubstituteQuery.next()
        numSubstitutes = SubstituteQuery.value(0).toInt()[0]
        
        if numSubstitutes >= Constants.MIN_SUBSTITUTES:
            return 1
        else:
            return 0
    else:
        return 0


# Function: CountStarters
#
# Count number of starters for a team in Lineup table
# Returns number of entries where starter flag set to TRUE
#   for a given match and team
def CountStarters(match_id, team_id):
    
    StartersQuery = QSqlQuery()
    StartersQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE match_id=? AND team_id=? AND lp_starting")
    StartersQuery.addBindValue(QVariant(match_id))
    StartersQuery.addBindValue(QVariant(team_id))
    StartersQuery.exec_()
    
    if StartersQuery.next():
        return StartersQuery.value(0).toInt()[0]
    else:
        return 0
        

# Function: CountSubstitutes
#
# Count number of substitutes for a team in Lineup table
# Returns number of entries where starter flag set to FALSE
#   for a given match and team
def CountSubstitutes(match_id, team_id):
    
    SubstituteQuery = QSqlQuery()
    SubstituteQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE match_id=? AND team_id=? AND NOT lp_starting")
    SubstituteQuery.addBindValue(QVariant(match_id))
    SubstituteQuery.addBindValue(QVariant(team_id))
    SubstituteQuery.exec_()
    
    if SubstituteQuery.next():
        return SubstituteQuery.value(0).toInt()[0]
    else:
        return 0


# Function: CountCaptains
#
# Count number of captains for a team in Lineup table
# Returns number of entries where captain flag set to TRUE
#   for a given match and team
def CountCaptains(match_id, team_id):
    
    CaptainQuery = QSqlQuery()
    CaptainQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE match_id=? AND team_id=? AND lp_starting AND lp_captain")
    CaptainQuery.addBindValue(QVariant(match_id))
    CaptainQuery.addBindValue(QVariant(team_id))
    CaptainQuery.exec_()
    
    if CaptainQuery.next():
        return CaptainQuery.value(0).toInt()[0]
    else:
        return 0


# Function: CountGoalkeepers
#
# Count number of starting goalkeepers for a team in Lineup table
# Returns number of entries where starting flag set to TRUE and 
# position is goalkeeper for a given match and team
def CountGoalkeepers(match_id, team_id):
    
    GoalkeeperQuery = QSqlQuery()
    GoalkeeperQuery.prepare("SELECT COUNT(*) FROM tbl_lineups WHERE match_id=? AND team_id=? AND lp_starting \
                        AND position_id IN (SELECT position_id FROM positions_list WHERE position_name = ?)")
    GoalkeeperQuery.addBindValue(QVariant(match_id))
    GoalkeeperQuery.addBindValue(QVariant(team_id))
    GoalkeeperQuery.addBindValue(QVariant("Goalkeeper"))                        
    GoalkeeperQuery.exec_()
    
    if GoalkeeperQuery.next():
        return GoalkeeperQuery.value(0).toInt()[0]
    else:
        return 0
