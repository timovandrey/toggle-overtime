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
    toggo = Toggo(  userEmail=USER_EMAIL, 
                    userPassword=USER_PASSWORD, 
                    userApiToken=USER_API_TOKEN)
    timeZone = datetime.time(2, 0, 0)
    toggo.sync(timeZone=timeZone)
    #toggo.load()

    # Test
    totalBreakTime = 0
    for entry in toggo.data:
        try:
            if(entry["description"] != "Pause"):
                continue
            totalBreakTime += entry["duration"]
        except:
            pass
    print("Total break time:", totalBreakTime)

    toggo.save()
    return

################################################################################
# ENTRY POINT                                                                  #
################################################################################
if(__name__ == "__main__"):
    main()