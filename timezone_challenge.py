from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

#timezone keys for creating ZoneInfo objects:

zones= (
    'Europe/Paris',
    'Europe/London',
    'Hongkong',
    'Africa/Nairobi',
    'Europe/Copenhagen'
)

#get the current time in utc
# utc_now = datetime.now(tz=timezone.utc)
local_now=datetime.now()
# local_now = local_now.replace(microsecond=0) # to remove microseconds


for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    # required_time = datetime.now(tz=tz)
    required_time = local_now.astimezone(tz)
    #the city is the last item, after slitting the zone at the /
    city = zone.split('/')[-1]
    # print(f'The time in {city} is {required_time}')
    print(f'The time in {city} is {required_time.strftime("%d/%m/%Y %H:%M:%S %z %Z")}')
    # ('%Y(year)-%m(month)-%d(date) %H(hour):%M(minute)   %z (utc time) %Z ytc code')


# france_tz= zoneinfo.ZoneInfo('Europe/Paris')
# france_now = utc_now.astimezone(france_tz)
# print(france_now)
#
# london_tz = zoneinfo.ZoneInfo('Europe/London')
# london_now = utc_now.astimezone(london_tz)
# print(london_now)
#
# hongkong_tz = zoneinfo.ZoneInfo('Hongkong')
# hongkong_now = utc_now.astimezone(hongkong_tz)
# print(hongkong_now)
#
# nairobi_tz = zoneinfo.ZoneInfo('Africa/Nairobi')
# nairobi_now = utc_now.astimezone(nairobi_tz)
# print(nairobi_now)

print()
print('Avaliable timezone keys')
print('_______________________')