#ex1
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Five Days Ago:", five_days_ago.strftime("%Y-%m-%d"))

#ex2 
from datetime import datetime, timedelta
today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print("today:", today.strftime("%Y-%m-%d"))
print("yesterday:", yesterday.strftime("%Y-%m-%d"))
print("tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#ex3 
from datetime import datetime
current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("DateTime without Microseconds:", current_datetime_without_microseconds)


#ex4
Year1 = int(input())
Month1 = int(input())
Date1 = int(input())
Year2 = int(input())
Month2 = int(input())
Date2 = int(input())
S1 = Year1 * 365 + Month1 * 30 + Date1
S2 = Year2 * 365 + Month2 * 30 + Date2
T1 = S1 * 86400
T2 = S2 * 86400
D = T1 - T2
print("the difference of dates in seconds is - ", D)


