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
from calculator import Calculator
from credentials import *
from datahandler import DataHandler
from entryparser import EntryParser
from util import *
from structures import *
from constants import *
# General
import datetime
from dateutil.rrule import rrule, DAILY
from email.errors import StartBoundaryNotFoundDefect
# Toggl API
from toggl.TogglPy import Toggl

################################################################################
# MAIN                                                                         #
################################################################################

def main():
    
    calc = Calculator()
    calc.calculate(True)

    #date = datetime.date(day=1, month=7, year=2022)
    #calc.toString(date)


    return


################################################################################
# ENTRY POINT                                                                  #
################################################################################
if(__name__ == "__main__"):
    main()
