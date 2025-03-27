import datetime
import locale

# locale.setlocale(locale.LC_ALL,'da_DK.utf-8') #locale changes languages here to danish where fr_FR.utf-8
locale.setlocale(locale.LC_ALL,'')

start = datetime.date(2022,2,4)
print(start)

pretty_start = start.strftime('%A %d %B,%Y')
print(pretty_start)

year = start.year
month = start.month
day= start.day

print(f'The {year} ...{day}.... {month} ')

today = datetime.date.today()
print(today)

print(today.strftime('%A'))
print(today.weekday()) #zero based so 0,1,2
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

duration = datetime.timedelta(days=15, hours=48)
end = start + duration
print(end)
print(duration)

d1=datetime.timedelta(hours=4)
d2= datetime.timedelta(minutes=240)
d3= datetime.timedelta(seconds=7200*2)

print(d1,d2,d3, sep=', ')
print(repr(d1), repr(d2), repr(d3), sep=', ')

difference = end - start
print(repr(difference))
print(difference == duration)