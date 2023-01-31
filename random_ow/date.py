import re
from datetime import datetime, timedelta

from random_ow.common import inNone, MockPyExpressionException


class Date:
    @classmethod
    def datetime(cls, format_str=None, time_interval: str = None):
        """
        example:
        @date('%Y-%m-%d %H:%M:%S')  2022-12-09 16:50:00
        @date('%Y-%m-%d %H:%M:%S','-1')  2022-12-08 16:50:00
        @date('%Y-%m-%d %H-%M-%S')
        @date()
        :param format_str:
        :param time_interval:'+1min'/'-1mil'
        :return:
        """
        # 判断是否满足表达式
        if not inNone(time_interval) and (len(time_interval) <= 1 or time_interval[:1] not in ('+', '-')):
            raise MockPyExpressionException(remark="The correct expression for time:'+1h' or '-1h'.")
        # '@date("%Y.%m.%d %H:%M:%S","+1")'
        if inNone(format_str):
            format_str = '%Y-%m-%d %H:%M:%S'
        # 定义初始化变量
        days = 0
        seconds = 0
        microseconds = 0
        milliseconds = 0
        minutes = 0
        hours = 0
        # 当前时间
        curr_time = datetime.now()
        today = (curr_time.strftime(format_str))
        # 处理时间的计算
        if not inNone(time_interval):
            calculate = time_interval[:1]
            # 正则获取时间单位
            regular = '[a-zA-Z]+'  # 正则匹配英文
            match = re.search(regular, time_interval)
            group = match.group(0)
            unit = group
            # 时间的间隔量
            amount = int(time_interval[1:-len(unit)])
            # 处理时间的量
            if 'hours'.startswith(unit):
                hours = amount
            elif 'minutes'.startswith(unit):
                minutes = amount
            elif 'milliseconds'.startswith(unit):
                milliseconds = amount
            elif 'microseconds'.startswith(unit):
                microseconds = amount
            elif 'seconds'.startswith(unit):
                seconds = amount
            elif 'days'.startswith(unit):
                days = amount
            timedelta_value = timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                        milliseconds=milliseconds, minutes=minutes, hours=hours)
            if calculate == '+':
                random_data = (curr_time + timedelta_value).strftime(format_str)
                return random_data
            elif calculate == '-':
                random_data = (curr_time - timedelta_value).strftime(format_str)
                return random_data
        return today

    @classmethod
    def date(cls, format_str=None, time_interval: str = None):
        """
        example:
        @date('%Y-%m-%d')  2022-12-09
        @date('%Y-%m-%d','-1')  2022-12-08
        @date()
        可以传参'%Y-%m-%d %H:%M:%S'
        :param format_str:'%Y-%m-%d';'%Y:%m:%d'/'%Y-%m-%d %H:%M:%S'
        :param time_interval: 加或减
        :return: 随机日期(年月日/年月日时分秒)
        """
        format_str = '%Y-%m-%d' if inNone(format_str) else format_str
        return cls.datetime(format_str, time_interval)

    @classmethod
    def time(cls, format_str=None, time_interval: str = None):
        """
        example:
        @time('%Y-%m-%d')  15:03:49
        @time('%Y-%m-%d','-1')  2022-12-08
        @time()
        可以传参'%Y-%m-%d %H:%M:%S'
        :param time_interval: 加或减
        :param format_str:'%H:%M:%S'/'%Y:%m:%d';'%Y-%m-%d %H:%M:%S'
        :return: 随机日期(时分秒/年月日时分秒)
        """
        format_str = '%H:%M:%S' if inNone(format_str) else format_str
        return cls.datetime(format_str, time_interval=time_interval)


date = Date()
