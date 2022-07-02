# toggle-overtime
This is a little application (work in progress) which lets you graphically access and calculate your overtime.

## How is overtime calculated?
To make this work, you need to tag your breaks. The breaks should have the description "break" (or something similar, defined in `constants.py`). That way, the program will find the general work time on that day and the break time. Also, you can tag your workdays as different types of scheduled time (sick leave, overtime recuction, normal work day, etc.). That way the program can calculate all relevant data, which are:
- Your work day type
- The time you worked that day
- How long you were supposed to work
- etc.

## Current state
The current state of the program does nothing fancy. It is just getting developed so expect not much from this. To try it out on your own you need to clone this repo and then create a file called `credentials.py` in the repo directory. In that file, you need to write the following:
```python
# User data
# The users Toggl API token can be found under Toggl -> My Profile (scroll down)
USER_API_TOKEN = "YourAPIToken"
USER_EMAIL = "YourEmail"
USER_PASSWORD = "YourPassword"
```
This file is intentionally left out by the gitignore.
