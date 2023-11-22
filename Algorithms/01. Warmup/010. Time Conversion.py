# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM' and s[:2] == '12':
        convertedTime = '00' + s[2:-2]
    elif s[-2:] == 'AM':
        convertedTime = s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        convertedTime = s[:-2]
    else:
        convertedTime = (str(int(s[:2]) + 12)) + s[2:-2]


    return convertedTime



#time = '12:01:00AM'
#time = '03:05:00AM'
#time = '12:01:00PM'
#time = '05:05:45PM'


time = '07:05:45PM'

timeIn24HourFormat = timeConversion(time)

print(timeIn24HourFormat)