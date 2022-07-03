################################################################################
# File:         calculator.py
# Author:       Timo Vandrey
# Date:         02.07.2022
# Version:      1
# Description:
# This is an object for easy overtime calculation. It abstracts all the ground
# work of the program.
################################################################################
# IMPORTS                                                                      #
################################################################################
# Project specific
from xml.sax.handler import EntityResolver
from credentials import *
from constants import *
from exceptions import *
from datahandler import *
from entryparser import *
from structures import *
# General
import datetime
from re import A
from urllib import request
from xmlrpc.client import DateTime
from dateutil.rrule import rrule, DAILY
# Toggl API
from toggl.TogglPy import Toggl

################################################################################
# OBJECT DECLARATION & DEFINITION                                              #
################################################################################
class Calculator:
    
    parser : EntryParser
    handler : DataHandler
    entries : Entry = []
    startDate : datetime.date
    endDate : datetime.date
    timeZone : datetime.time

    def __init__(self) -> None:
        self.handler = DataHandler(userEmail=USER_EMAIL,
                     userPassword=USER_PASSWORD,
                     userApiToken=USER_API_TOKEN)
        self.parser = EntryParser()
        self.timeZone = datetime.time(2, 0, 0)
        self.startDate = datetime.datetime.strptime(START_DATE, START_DATE_FORMAT)
        self.endDate = datetime.datetime.now()

    def update(self):
        self.handler.data = []
        self.handler.download(self.timeZone)
        self.entries = []
        self.__populate()
        self.__correct()

    def setDayType(self, date : datetime.time, dayType : DayType) -> bool:
        # Returns True if successful, False if unsuccessful
        for entry in self.entries:
            if(entry.date == date):
                entry.dayType = dayType
                return True
        return False

    def toString(self, date : datetime.date):
        for entry in self.entries:
            if entry.date == date:
                break        
        print("Entry:")
        print("Date:", str(date))
        print("Work time:", entry.workTime * SEC_TO_HOURS)
        print("Break time:", entry.breakTime * SEC_TO_HOURS)
        print("Type of day:", str(entry.dayType))

    def __populate(self):
        for date in rrule(DAILY, dtstart=self.startDate, until=self.endDate):
            date = date.date()
            tmpEntry = Entry(date, 
                        self.__determineStandardDayType(date), 
                        self.parser.getTotalBreakTimeAtDate(self.handler.data, date),
                        self.parser.getTotalWorkTimeAtDate(self.handler.data, date))
            self.entries.append(tmpEntry)
        pass

    def __correct(self):
        for entry in self.entries:
            entry.breakTime = self.__determineBreakTime(entry.breakTime, 
                                                        entry.supposedBreakTime,
                                                        entry.workTime,
                                                        entry.dayType)
            entry.supposedWorkTime = self.__determineSupposedWorkTime(entry.dayType)
            pass
        pass 

    def __determineBreakTime(self, breakTimeIn : int, supposedBreakTime : int, workTime: int, dayType : DayType) -> int :
        breakTime : int = breakTimeIn
        if(dayType == DayType.Unkown):
            breakTime = breakTimeIn
            pass
        if(dayType != DayType.NormalWork):
            breakTime = 0
        if(breakTimeIn < supposedBreakTime):
            breakTime = supposedBreakTime
        return breakTime

    def __determineSupposedWorkTime(self, dayType : DayType) -> int :
        supposedWorkTime : int
        if( dayType == DayType.NonWorkDay or
            dayType == DayType.SickLeave or
            dayType == DayType.Vacation):
            supposedWorkTime = 0
        else:
            supposedWorkTime = SUPPOSED_WORK_TIME_DAILY * HOURS_TO_SEC
        return supposedWorkTime

    def __determineStandardDayType(self, date : datetime.date):
        # Monday 0, Tuesday 1, Wednesday 2,
        # Thursday 3, Friday 4, Saturday 5, Sunday 6
        weekday = date.weekday()
        if(weekday >= 5):
            return DayType.NonWorkDay
        return DayType.NormalWork
        
    def calculate(self, printOut : bool) -> int:
        overTime : int = 0
        supposedWorkTime : int = 0
        breakTime : int = 0
        workTime : int = 0
        
        for entry in self.entries:
            supposedWorkTime += entry.supposedWorkTime 
            breakTime += entry.breakTime
            workTime += entry.workTime
        overTime = workTime - supposedWorkTime
        if(printOut):
            print("workTime:", workTime * SEC_TO_HOURS)
            print("supposedWorkTime:", supposedWorkTime * SEC_TO_HOURS)
            print("overTime:", overTime * SEC_TO_HOURS)
        return overTime

    def save(self):
        raise NotImplemented

    def load(self):
        raise NotImplemented