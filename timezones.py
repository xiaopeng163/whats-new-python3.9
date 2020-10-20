from datetime import datetime
# from pytz import timezone
from zoneinfo import ZoneInfo

current_time = datetime.now()
print(current_time)
print('Amsterdam', current_time.astimezone(ZoneInfo('Europe/Amsterdam')))
print('Amsterdam', current_time.astimezone(ZoneInfo('Europe/Amsterdam')))
print('Shanghai', current_time.astimezone(ZoneInfo('Asia/Shanghai')))


# pip install pytz
# pip install tzdata
