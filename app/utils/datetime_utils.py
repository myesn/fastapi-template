from datetime import datetime
from zoneinfo import ZoneInfo

TZ_Shanghai = ZoneInfo('Asia/Shanghai')


def get_datetime_now_with_tz():
    return datetime.now(TZ_Shanghai)
