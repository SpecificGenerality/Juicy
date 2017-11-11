from dateutil import parser
import time

date = parser.parse("Tuesday, October 17, 2017 at 6:17pm EDT")
print(int(time.mktime(date.timetuple())))