"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
from datetime import date

dateOne = date(2014, 7, 2)
dateTwo = date(2014, 7, 11)
deltaDate = dateTwo - dateOne
print(deltaDate.days)
