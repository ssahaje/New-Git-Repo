import datetime
from datetime import date, timedelta
import calendar

weekno = datetime.datetime.today().weekday()

if weekno < 5:
    print("Weekday")
else:  # 5 Sat, 6 Sun
    print("Weekend")


curr_date = date.today()
curr_day = calendar.day_name[curr_date.weekday()]
print(curr_day)
print(curr_date)
if curr_day not in ['Saturday', 'Sunday']:
    booking_date = curr_date
    print(booking_date)
elif curr_day == 'Sunday':
    booking_date = curr_date + timedelta(1)
    print(booking_date)
elif curr_day == 'Saturday':
    booking_date = curr_date + timedelta(2)
    print(booking_date)

