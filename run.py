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
import datetime
from email.errors import StartBoundaryNotFoundDefect
from toggl.TogglPy import Toggl
from toggo import Toggo
from credentials import *

################################################################################
# MAIN                                                                         #
################################################################################
def main():
    startDate = datetime.date(2022, 6, 13)
    endDate = datetime.date(2022, 6, 19)
    timeZone = datetime.time(2, 0, 0)

    toggo = Toggo(  userEmail=USER_EMAIL, 
                    userPassword=USER_PASSWORD, 
                    userApiToken=USER_API_TOKEN)
    toggo.fetchDataEntries(startDate, endDate, timeZone)
    
    return

################################################################################
# ENTRY POINT                                                                  #
################################################################################
if(__name__ == "__main__"):
    main()