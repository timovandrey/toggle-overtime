################################################################################
# File:         entryparser.py
# Author:       Timo Vandrey
# Date:         23.06.2022
# Version:      1
# Description:
# This object represents a parser to get information from Toggl json objects.
################################################################################
# IMPORTS                                                                      #
################################################################################
# Project specific
from tracemalloc import start
from constants import *
from exceptions import *
# General
from html import entities
from xmlrpc.client import Boolean
import datetime
from socketserver import DatagramRequestHandler

################################################################################
# OBJECT DECLARATION & DEFINITION                                              #
################################################################################
class EntryParser:

    def __init__(self) -> None:
        pass

    def getWorkDays(self, data : dict) -> datetime.date:
        workdays = []
        for entry in data:
            date = self.parseDate(entry)
            # Check whether date is already in list
            dateAlreadyAppended = False
            for workday in workdays:
                if(workday == date): 
                    dateAlreadyAppended = True
                    break
            if(dateAlreadyAppended): 
                continue
            workdays.append(date)
        return workdays

    def getTotalBreakTimeAtDate(self, data : dict, date : datetime.date):
        totalBreakTimeAtDate = 0
        entriesAtDate = self.__getEntriesAtDate(data, date)
        for entry in entriesAtDate:
            try: 
                if(self.__isEntryPauseEntry(entry)):
                    totalBreakTimeAtDate += entry["duration"]
            except:
                pass
        return totalBreakTimeAtDate

    def getTotalWorkTimeAtDate(self, data : dict, date : datetime.date):
        totalWorkTimeAtDate = 0
        entriesAtDate = self.__getEntriesAtDate(data, date)
        for entry in entriesAtDate:
            try:
                totalWorkTimeAtDate += entry["duration"]
            except:
                pass
        totalBreakTimeAtDate = self.getTotalBreakTimeAtDate(data, date)
        return totalWorkTimeAtDate - totalBreakTimeAtDate
        
    def __getEntriesAtDate(self, data : dict, date : datetime):
        entriesAtDate = []
        for entry in data:
                if(self.__parseDate(entry) == date):
                    entriesAtDate.append(entry)
        return entriesAtDate

    def __isEntryPauseEntry(self, data : dict) -> Boolean:
        try:
            for breakKeyWord in BREAK_KEYWORDS:
                if(data["description"] == breakKeyWord):
                    return True
        except:
            return False
        return False
    
    def __parseFullDateString(self, dateString : str):
        dateFormat = "%Y-%m-%dT%H:%M:%S"
        dateStrings = dateString.split("+")
        date = datetime.datetime.strptime(dateStrings[0], dateFormat)
        return date

    def __parseDate(self, dictEntry : dict):
        # Format: 2022-06-20T15:18:28+00:00
        dateStart = dictEntry["start"]
        dateEnd = dictEntry["stop"]
        dateStart = str(dateStart).split("T")
        dateEnd = str(dateEnd).split("T")
        dateFormat = "%Y-%m-%d"        
        dateStart = datetime.datetime.strptime(dateStart[0], dateFormat)
        dateEnd = datetime.datetime.strptime(dateEnd[0], dateFormat)
        
        if(dateStart != dateEnd):
            raise InvalidWorkHoursException("You shouldn't work at 00:00. Check whether you have an entry that spans over two days.")
        return datetime.datetime.date(dateStart)
    
