from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone() #local timezone
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)

france_tz= zoneinfo.ZoneInfo('Europe/Paris')
france_now = utc_now.astimezone(france_tz)
print(france_now)

london_tz = zoneinfo.ZoneInfo('Europe/London')
london_now = utc_now.astimezone(london_tz)
print(london_now)

hongkong_tz = zoneinfo.ZoneInfo('Hongkong')
hongkong_now = utc_now.astimezone(hongkong_tz)
print(hongkong_now)

nairobi_tz = zoneinfo.ZoneInfo('Africa/Nairobi')
nairobi_now = utc_now.astimezone(nairobi_tz)
print(nairobi_now)

print()
print('Avaliable timezone keys')
print('_______________________')
# for zone_key in sorted(zoneinfo.available_timezones()): #displays all of the tz keys
#     print(zone_key)


# Hongkong
# Africa/Nairobi
