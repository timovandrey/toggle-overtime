################################################################################
# File:         toggo.py
# Author:       Timo Vandrey
# Date:         07.06.2022
# Version:      1
# Description:
# This main object of the overtime calculator.
################################################################################
# IMPORTS                                                                      #
################################################################################
from constants import *
import datetime
from re import A
from urllib import request
from xmlrpc.client import DateTime
from toggl.TogglPy import Toggl
import json

################################################################################
# OBJECT DECLARATION & DEFINITION                                              #
################################################################################
class Toggo:

    def __init__(self, userEmail, userPassword, userApiToken):
        global toggl
        toggl = Toggl()
        toggl.setAuthCredentials(userEmail, userPassword) 
        toggl.setAPIKey(userApiToken)
        self.data = None
        return

    def save(self):
        with open(SYNC_FILE_NAME, "w+") as fp:
            fp.write(json.dumps(self.data))
        return

    def load(self):
        with open(SYNC_FILE_NAME, "r+") as fp:
            self.data = json.load(fp)
        return

    def sync(self, timeZone : datetime.time):
        today = datetime.datetime.now()
        startdate = datetime.datetime.strptime(START_DATE, START_DATE_FORMAT)
        self.data = self.fetchDataEntries(startdate, today, timeZone)

    def fetchDataEntries(self, startDate : datetime.date, endDate : datetime.date, timeZone : datetime.time):
        response = toggl.request(self.modRequestURL(startDate, endDate, timeZone))
        return response

    def modRequestURL(self, startDate : datetime.date, endDate : datetime.date, timeZone : datetime.time):
        startDateImplicator = "start_date"
        endDateImplicator = "end_date"
            
        requestUrl = TOGGL_API_URL_BASE
        requestUrlAdd = ""
        requestUrlAdd += "?"
        requestUrlAdd += startDateImplicator
        requestUrlAdd += "="
        requestUrlAdd += str(startDate.year)
        requestUrlAdd += "-"
        requestUrlAdd += str(startDate.month).rjust(2, "0")
        requestUrlAdd += "-"
        requestUrlAdd += str(startDate.day).rjust(2, "0")
        requestUrlAdd += "T"
        requestUrlAdd += "00:00:01+"
        requestUrlAdd += str(timeZone.hour).rjust(2, "0") + ":" + str(timeZone.minute).rjust(2, "0")
        requestUrlAdd += "&"
        requestUrlAdd += endDateImplicator
        requestUrlAdd += "="
        requestUrlAdd += str(endDate.year)
        requestUrlAdd += "-"
        requestUrlAdd += str(endDate.month).rjust(2, "0")
        requestUrlAdd += "-"
        requestUrlAdd += str(endDate.day).rjust(2, "0")
        requestUrlAdd += "T"
        requestUrlAdd += "23:59:59+"
        requestUrlAdd += str(timeZone.hour).rjust(2, "0") + ":" + str(timeZone.minute).rjust(2, "0")
        
        requestUrlAdd = requestUrlAdd.replace(":", URL_COLON)
        requestUrlAdd = requestUrlAdd.replace("+", URL_PLUS)

        requestUrl += requestUrlAdd
        return requestUrl