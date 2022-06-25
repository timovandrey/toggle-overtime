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
from exceptions import *
# General
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

    def getTotalBreakTime(self, data : dict, date : datetime.date):
        
        
        
        pass

    def parseDate(self, dictEntry : dict):
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
    
