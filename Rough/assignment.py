import datetime
from zoneinfo import ZoneInfo, available_timezones


current_date = datetime.date(2024, 12, 30 )
print("current_date", current_date)
current_today = datetime.date.today()
print("current_today", current_today)
current_time = datetime.datetime.today().strftime("%A-%d-%b-%Y %H:%M:%S")
print("current_time", current_time)
