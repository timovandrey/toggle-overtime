################################################################################
# File:         entry.py
# Author:       Timo Vandrey
# Date:         23.06.2022
# Version:      1
# Description:
# This object represents a day for the tracking of the time, breaks and overtime
################################################################################
# IMPORTS                                                                      #
################################################################################
import enum

################################################################################
# OBJECT DECLARATION & DEFINITION                                              #
################################################################################
class DayType(enum.Enum):
    NormalWork = 0
    SickLeave = 1
    OvertimeReduction = 2
    Vacation = 3

class Entry:
    
    def __init__(self):
        self.breakTime = 0
        self.dayType = DayType.NormalWork
        return