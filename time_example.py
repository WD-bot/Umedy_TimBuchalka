from datetime import time, date

meeting =time(hour= 13, minute=14, second=15)
print(meeting)

end_time = time(hour=14, minute=45)
print(end_time)

# print(end_time-meeting) # errors because there is no dates

iso_time = 'T11:15:00'
_time = time.fromisoformat(iso_time)
print(_time)

iso_date= '2025-03-26'
_date = date.fromisoformat(iso_date)
print(_date)

