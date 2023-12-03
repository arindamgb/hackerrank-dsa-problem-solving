# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

from datetime import datetime, timedelta
def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        doP = '26.09.1918'

    if 1700 <= year <= 1917 and year % 4 == 0:
        doP = f'12.09.{str(year)}'
    elif 1700 <= year < 1917:
        doP = f'13.09.{str(year)}'

    if 1919 <= year <= 2700 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        doP = f'12.09.{str(year)}'
    elif 1919 <= year < 2700:
        doP = f'13.09.{str(year)}'

    return doP

year = 1800

print(dayOfProgrammer(year))