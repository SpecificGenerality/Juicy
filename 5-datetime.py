from dateutil import parser
import time

date = parser.parse("Tuesday, October 17, 2017 at 6:17pm EDT")
timestamp = int(time.mktime(date.timetuple()))
week = int(timestamp/(60*60*24*7))*(60*60*24*7)
print(week)