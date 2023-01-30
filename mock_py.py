import random
import re
from datetime import datetime, timedelta

from random_ow import basic
from random_ow.common import MockPyExpressionException, mock_exception


def inNone(obj):
    return obj in ('', None)


def tuple_to_str(objects) -> str:
    """
    :param objects: 被转换的元组/列表
    :return: 列表被转换后的字符串
    """
    return str(''.join(objects))


class MockPy:

    def mocker(self, mock_str):
        keyword = self.get_mocker_key(mock_str)
        args = self.get_mocker_params_to_tuple(mock_str)
        if keyword == 'date':
            return self.date.date(*args)
        elif keyword == 'float':
            return basic.FloatOw.float(*args)
        elif keyword == 'natural':
            return basic.NaturalOw.natural(*args)
        elif keyword == 'integer':
            return basic.IntegerOw.integer(*args)
        elif keyword == 'boolean':
            return basic.BooleanOw.boolean(*args)
        elif keyword == 'character':
            return basic.CharacterOw.character(*args)
        elif keyword == 'string':
            return basic.StringOw.string(*args)
        elif keyword == 'pick':
            return self.helper.pick(*args)
        return None

    @classmethod
    def get_mocker_key(cls, mock_str):
        if not mock_str.startswith('@'):
            raise MockPyExpressionException()
        if not mock_str.endswith(')'):
            # 非)结尾说明是@date,则直接返回属性名
            return mock_str[1:]
        regular = '(?<=(\\@)).*?(?=(\\())'
        keyword = re.search(regular, mock_str).group(0)
        return keyword

    @classmethod
    def get_mocker_params_to_tuple(cls, mock_params) -> tuple:
        """

        :param mock_params: ('%Y.%m.%d %H:%M:%S','+1')
        :return: 将参数组装为元祖,方便后续解包
        """
        regular = '[\\(|（].*[\\)|）]$'
        # '@date("%Y.%m.%d %H:%M:%S","+1")' 获取明天此时的日期
        match = re.search(regular, mock_params)
        if match is None:
            return ()
        group = match.group(0)
        if group == '()':
            return ()
        end_val = group[-1:]
        if not end_val.endswith(','):
            group = f'{group[:-1]},)'
        args = eval(group)
        return args

    class Basic:
        number_str_max_length = None

        @classmethod
        def number_str(cls, min_length=None, max_length=number_str_max_length) -> str:
            """

            :param min_length:
            :param max_length:
            :return: 随机长度的数字字符
            """
            mock_exception.min_max_value_exception(max_length, min_length)
            if inNone(min_length):
                min_length = random.randint(0, 15)
            if inNone(max_length):
                max_length = random.randint(min_length, 16)
            number_string_list = []
            range_size = cls.number_not_start_with_zero(min_length, max_length)
            for kk in range(range_size):
                number_string_list.append(str(random.randint(0, 9)))
            number_str = ''.join(number_string_list)
            return number_str

        @classmethod
        def number_not_start_with_zero(cls, start_number: int, end_number: int) -> int:
            """

            :param end_number: 随机数的最大值,包含
            :param start_number: 随机数的最小值,包含,默认=1
            :return: 从1开始的整数类型的随机数;[start_number,end_number] 取值范围为闭区间
            """
            return random.randint(start_number if start_number != 0 else 1, end_number if end_number != 1 else 2)

    basic = Basic()

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

    class Helper:
        @classmethod
        def pick(cls, pick_list):
            if inNone(pick_list):
                raise MockPyExpressionException('pick_list cannot be empty.')
            assert isinstance(pick_list, (str, list, tuple))
            if isinstance(pick_list, str):
                pick_list = eval(pick_list)
            return random.choice(pick_list)

    helper = Helper()


mocker = MockPy()
