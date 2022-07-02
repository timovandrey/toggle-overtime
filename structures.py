################################################################################
# File:         structures.py
# Author:       Timo Vandrey
# Date:         25.06.2022
# Version:      1
# Description:
# This file is to collect all structures, enums, etc.
################################################################################
# IMPORTS                                                                      #
################################################################################
from datetime import datetime
import enum

from constants import BREAK_MIN_TIME, HOURS_TO_MIN, HOURS_TO_SEC, SUPPOSED_WORK_TIME_DAILY

################################################################################
# DEFINITIONS                                                                  #
################################################################################
class DayType(enum.Enum):
    Unkown = 0
    NormalWork = 1
    SickLeave = 2 
    OvertimeReduction = 3
    Vacation = 4
    NonWorkDay = 5

class Entry:
    date : datetime.date
    dayType : DayType
    breakTime : int
    workTime : int
    supposedWorkTime : int
    supposedBreakTime : int

    def __init__(self, 
                date, 
                dayType, 
                breakTime, 
                workTime, 
                supposedWorkTime = (SUPPOSED_WORK_TIME_DAILY * HOURS_TO_SEC),
                supposedBreakTime = BREAK_MIN_TIME * HOURS_TO_SEC
                )-> None:
        self.date = date
        self.dayType = dayType
        self.breakTime = breakTime
        self.workTime = workTime
        self.supposedWorkTime = supposedWorkTime
        self.supposedBreakTime = supposedBreakTime
        return