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
TOGGL_API_URL_BASE = "https://api.track.toggl.com/api/v8/time_entries"

# HTML related
URL_COLON = "%3A"
URL_PLUS = "%2B"

# Sync related
START_DATE = "2022.04.19, 00:00:00.00"
START_DATE_FORMAT = "%Y.%m.%d, %H:%M:%S.%f"

# Save related
SYNC_FILE_NAME = "data.json"

# Calculation related
# Hint: The duration in the field "duration" of an entry is always given in seconds.

BREAK_MIN_TIME = 0.75
SUPPOSED_WORK_TIME_DAILY = 8
SUPPOSED_WORK_DAYS_WEEKLY = 5
SUPPOSED_WORK_TIME_WEEKLY = SUPPOSED_WORK_TIME_DAILY * SUPPOSED_WORK_DAYS_WEEKLY

SEC_TO_HOURS = 1/(60*60)
MIN_TO_HOURS = 1/60
HOURS_TO_MIN = 60
HOURS_TO_SEC = 60*60
MIN_TO_SEC = 60
SEC_TO_MIN = 1/60
