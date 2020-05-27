"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.prmonth(year, month))
