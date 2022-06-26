################################################################################
# File:         run.py
# Author:       Timo Vandrey
# Date:         19.06.2022
# Version:      1
# Description:
# This is a script to calculate the overtime done by a certain user
# automatically using the TogglTrack API.
################################################################################
# IMPORTS                                                                      #
################################################################################
# Project specific
from credentials import *
from datahandler import DataHandler
from entryparser import EntryParser
from util import *
from structures import *
from constants import *
# General
import datetime
from email.errors import StartBoundaryNotFoundDefect
# Toggl API
from toggl.TogglPy import Toggl

################################################################################
# MAIN                                                                         #
################################################################################


def main():
    dh = DataHandler(userEmail=USER_EMAIL,
                     userPassword=USER_PASSWORD,
                     userApiToken=USER_API_TOKEN)
    timeZone = datetime.time(2, 0, 0)
    dh.download(timeZone=timeZone)

    # Test
    parser = EntryParser()
    date = datetime.date(2022, 6, 7)
    breakTime = parser.getTotalBreakTimeAtDate(dh.data, date)
    workTime = parser.getTotalWorkTimeAtDate(dh.data, date)
    print("Total break time:", breakTime * SEC_TO_HOURS)
    print("Total work time:", workTime * SEC_TO_HOURS)
    print("Total time in office:", (workTime + breakTime) * SEC_TO_HOURS)

    dh.save()
    return


################################################################################
# ENTRY POINT                                                                  #
################################################################################
if(__name__ == "__main__"):
    main()
