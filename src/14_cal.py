"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
# gets todays date
today = datetime.now()
args = sys.argv[1:]
print(args)

try:
  if len(args) == 2:
    month = int(args[0])
    year = int(args[1])

  # User provides only a month
  elif len(args) == 1:
    month = int(args[0])
    year = today.year

  # User provides no args
  elif len(args) == 0:
    month = today.month
    year = today.year

  # User provieds incorrect args
  else :
    print("Error: Must be in the format: '14_cal.py month [year]")
  text_calendar = calendar.TextCalendar()
  text_calendar.prmonth(year, month)

except:
  print("Error: Must be in the format: '14_cal.py month [year]")