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
# General
import datetime
from email.errors import StartBoundaryNotFoundDefect
# Toggl API
from toggl.TogglPy import Toggl

################################################################################
# MAIN                                                                         #
################################################################################
def main():
    dh = DataHandler(  userEmail=USER_EMAIL, 
                    userPassword=USER_PASSWORD, 
                    userApiToken=USER_API_TOKEN)
    timeZone = datetime.time(2, 0, 0)
    dh.download(timeZone=timeZone)
    
    # Test
    parser = EntryParser()
    workdays = parser.getWorkDays(dh.data)

    print(workdays)
    print("Worked days:", len(workdays))


    dh.save()
    return

################################################################################
# ENTRY POINT                                                                  #
################################################################################
if(__name__ == "__main__"):
    main()