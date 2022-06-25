################################################################################
# File:         constants.py
# Author:       Timo Vandrey
# Date:         19.06.2022
# Version:      1
# Description:
# These is the general hub for all the constants used in the toggl overtime
# calculator. Not all are in here, but most.
################################################################################
# CONSTANTS / GLOBALS                                                          #
################################################################################
# Tracking related
BREAK_KEYWORDS = ["Pause", "Break"]
BREAK_MIN_TIME = 45
TOGGL_API_URL_BASE = "https://api.track.toggl.com/api/v8/time_entries"

# HTML related
URL_COLON = "%3A"
URL_PLUS = "%2B"

# Sync related
START_DATE = "2020.01.01, 00:00:00.00"
START_DATE_FORMAT = "%Y.%m.%d, %H:%M:%S.%f"

# Save related
SYNC_FILE_NAME = "data.json"

