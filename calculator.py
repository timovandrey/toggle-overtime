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
from cgitb import handler
from sqlite3 import DateFromTicks
from time import timezone
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
import json
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
        self.startDate = datetime.strptime(START_DATE, START_DATE_FORMAT)
        self.endDate = datetime.now().date

        self.handler.download(self.timeZone)

        for date in rrule(DAILY, dtstart=self.startDate, until=self.endDate):
            date = date.date()
            tmpEntry = Entry(date, 
                        DayType.Unkown, 
                        self.parser.getTotalBreakTimeAtDate(self.handler.data, date),
                        self.parser.getTotalWorkTimeAtDate(self.handler.data, date))
            self.entries.append(tmpEntry)           
        pass



