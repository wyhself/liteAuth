#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    时间处理函数
"""
import time
from datetime import timedelta, datetime, date

FORMAT_DATE = '%Y-%m-%d'
FORMAT_DATE_CHINA = "%-m月%-d日"
FORMAT_DATE_CHINA_FULL = "%Y年%m月%d日"
COMPACT_DATE = "%Y%m%d"
DOT_DATE = "%Y.%m.%d"
COMPACT_TIME = "%H%M%S"
FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'
FORMAT_ONLY_TIME = "%H:%M"
COMPACT_DATETIME = "%Y%m%d%H%M%S"


def now():
    return datetime.now()


def datetime_to_str(_datetime, date_format=FORMAT_DATETIME):
    """
    将datetime对象转换成字符串
    :param _datetime:
    :param date_format:
    :return:
    """
    return _datetime.strftime(date_format)


def str_to_datetime(date_str, date_format=FORMAT_DATETIME):
    """
    将时间字符串转换成datetime对象
    :param date_str:
    :param date_format:
    :return:
    """
    return datetime.strptime(date_str, date_format)


def str_to_date(date_str, date_format=FORMAT_DATE):
    return datetime.strptime(date_str, date_format).date()


def get_today():
    """
         获取当前日期，格式：2014-07-14 00:00:00
    """
    _now = datetime.now()
    return datetime(_now.year, _now.month, _now.day)


def get_today_date():
    """
         获取当前日期，格式：2014-07-14
    """
    _now = datetime.now()
    return date(_now.year, _now.month, _now.day)


def get_yesterday():
    """
    """
    _date = datetime.now() - timedelta(days=1)
    return datetime(_date.year, _date.month, _date.day)


def get_yesterday_date():
    _date = datetime.now() - timedelta(days=1)
    return date(_date.year, _date.month, _date.day)


def get_tomorrow():
    # type: () -> object
    """
    返回明天
    :return:
    """
    _date = datetime.now() + timedelta(days=1)
    return datetime(_date.year, _date.month, _date.day)


def is_today(_datetime):
    """
          判断时间是否是今天
          :param _datetime:
    """
    _now = datetime.now()
    return True if _now.year == _datetime.year and _now.month == _datetime.month and _now.day == _datetime.day else False


def is_yesterday(_datetime):
    """
    判断是否是昨天
    :param _datetime:
    :return:
    """
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.year == _datetime.year and yesterday.month == _datetime.month and yesterday.day == _datetime.day


def timedelta_to_hour(delta):
    """
         换算时间
         :param delta:
    """
    seconds = int(round(delta.total_seconds()))
    hour = seconds / 3600
    minute = (seconds % 3600) / 60
    second = (seconds % 3600) % 60
    return hour, minute, second


def datetime_to_timestamp(time_):
    """
        datetime类型转换为unix时间戳*1000
        :param time_:
    """
    timestamp = time.mktime(time_.timetuple())
    return int(timestamp * 1000)


def timestamp_to_datetime(t):
    return datetime.fromtimestamp(t)


def minus_one_month(_datetime):
    """
    当前日期增加一个月
    :param _datetime:
    :return:
    """
    day = _datetime.day
    month = _datetime.month - 1
    if month == 0:
        month = 12
        year = _datetime.year - 1
    else:
        year = _datetime.year
    return datetime(year=year, month=month, day=day, hour=_datetime.hour, minute=_datetime.minute,
                    second=_datetime.second)


def add_one_month(_datetime):
    """
    当前日期增加一个月
    :param _datetime:
    :return:
    """
    return add_month(_datetime, 1)


def is_leap_year(year):
    """
    判断闰年
    :param year:
    :return:
    """
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    return False


def add_month(_datetime, months):
    """
    为当前时间加几个月
    :param _datetime:
    :param months:
    :return:
    """
    small_month = [4, 6, 9, 11]
    day = _datetime.day
    month = _datetime.month + months
    if month % 12 == 0:
        add_year = month / 12 - 1
        month = 12
    else:
        add_year = month / 12
        month %= 12
    year = _datetime.year + add_year
    if month in small_month and day > 30:
        day = 30
    elif month == 2 and day > 28:
        if is_leap_year(year):
            day = 29
        else:
            day = 28
    return datetime(
        year=year, month=month, day=day, hour=_datetime.hour, minute=_datetime.minute, second=_datetime.second)


def show_time_for_people(_datetime):
    """
    根据时间决定是否输出几天前或者几月几日还是今天的时间(给人类看的时间...)
    :param _datetime:
    :return:
    """
    now_time = now()
    yesterday = get_yesterday()
    if now_time.year == _datetime.year and now_time.month == _datetime.month and now_time.day == _datetime.day:
        return datetime_to_str(_datetime, date_format=FORMAT_ONLY_TIME)
    elif yesterday.year == _datetime.year and yesterday.month == _datetime.month and yesterday.day == _datetime.day:
        return u"昨天"
    else:
        return datetime_to_str(_datetime, date_format=FORMAT_DATE_CHINA)


def get_week_start_end(_datetime):
    """
    得到datetime所处周的开始,结束

    python weekday()返回的周,周一是0,周日是6

    注意!
    为了方便,返回的结束时间是下周一 0点

    :param datetime:
    :return: start,end
    """
    weekday = _datetime.weekday()
    start = _datetime + timedelta(- weekday)
    end = _datetime + timedelta(7 - weekday)
    return start, end


def is_birthday_today(birthday):
    """
    判断生日
    :param birthday: datetime
    :return:
    """
    if get_today().month == birthday.month and get_today().day == birthday.day:
        return True
    else:
        return False


def datetime_to_ago_str(t: datetime):
    """
    返回： 今天，n天前，...n月前，...n年前
    :param t:
    :return:
    """
    n = get_today()
    t = datetime(t.year, t.month, t.day)
    day = (n - t).days

    if day == 0:
        return '今天'
    elif day < 30:
        return '%d天前' % day
    elif day < 365:
        return '%d月前' % int(day / 30)
    elif day < 365:
        return '%d年前' % int(day / 365)
