import random
import re

from datetime import datetime, timedelta


def inNone(obj):
    return obj in ('', None)


class Mocker:

    def mocker(self, mock_str):
        keyword = self.get_mocker_key(mock_str)
        args = self.get_mocker_params_to_tuple(mock_str)
        if keyword == 'date':
            return self.date.date(*args)
        elif keyword == 'float':
            return self.basic.float(*args)
        elif keyword == 'natural':
            return self.basic.natural(*args)
        elif keyword == 'integer':
            return self.basic.integer(*args)
        elif keyword == 'boolean':
            return self.basic.boolean(*args)
        elif keyword == 'pick':
            return self.helper.pick(*args)
        return None

    @classmethod
    def get_mocker_key(cls, mock_str):
        if not mock_str.startswith('@'):
            raise MockerExpressionException()
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
        def boolean(cls, min_value=None, max_value=None, current=None):
            min_value = 0 if inNone(min_value) else min_value
            max_value = 1 if inNone(max_value) else max_value
            current = True if inNone(current) else current
            if min_value >= max_value:
                raise MockerExpressionException()
            luck_boolean_number = random.randint(min_value, max_value)
            if luck_boolean_number == min_value:
                return current
            else:
                return not current

        @classmethod
        def float(cls, min_value=None, max_value=None, dmin_value=None,
                  dmax_value=None):
            """
            随机浮点数,example:
            @float(95,100,12,19)
            @float(1,2)
            @float(952)  # 不小于992
            @float()  # 随机
            @float
            :param min_value:个位部分最小值
            :param max_value:个位部分最大值
            :param dmin_value:小数部分最小长度
            :param dmax_value:小数部分最大长度
            :return:
            """

            def __luck():
                return random.randint(1, 4) in (1, 2, 3)

            if inNone(min_value):
                min_value = -9999999999999999
            if inNone(max_value):
                max_value = 9999999999999999
            if inNone(dmin_value):
                dmin_value = random.randint(2, 5) if random.randint(1, 2) == 1 else 0
            if inNone(dmax_value):
                min_dmax_value = dmin_value if 14 > dmin_value > 0 else dmin_value + 1
                dmax_value = random.randint(min_dmax_value + 1, 16)
            decimals = cls.number_str(min_length=dmin_value, max_length=dmax_value)
            if __luck():
                while True:
                    # 满足最小值和最大值的浮点数
                    random_float = random.uniform(min_value, max_value)
                    val = str(random_float)
                    if '.' in val:
                        break
                int_part = val.split(".")[0]
                int_part = int_part if len(int_part) + len(decimals) <= 15 else int_part[:len(decimals)]
                val = f'{int_part}.{decimals}'
                random_float = float(val)
            else:
                random_float = random.uniform(min_value, max_value)
                if __luck():
                    random_float = float(f'{str(random_float)[:-1]}{random.randint(1, 9)}')
            round_num = random.randint(dmin_value, dmax_value)
            return float(round(random_float, round_num))

        @classmethod
        def number_str(cls, min_length=None, max_length=number_str_max_length) -> str:
            if min_length >= max_length:
                raise MockerExpressionException()
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
        def natural(cls, min_value=None, max_value=None) -> int:
            """

            :param min_value: 最小值,默认值:0
            :param max_value: 最大值,默认值:9999999999999999
            :return: 自然数
            """
            if inNone(min_value):
                min_value = 0
            if inNone(max_value):
                max_value = 9999999999999999
            if min_value >= max_value:
                raise MockerExpressionException()
            return random.randint(min_value, max_value)

        @classmethod
        def integer(cls, min_value=None, max_value=None) -> int:
            """

            :param min_value: 最小值,默认值:0
            :param max_value: 最大值,默认值:9999999999999999
            :return: 自然数
            """
            if inNone(min_value):
                min_value = -9999999999999999
            if inNone(max_value):
                max_value = 9999999999999999
            if min_value >= max_value:
                raise MockerExpressionException()
            return random.randint(min_value, max_value)

        @classmethod
        def number_not_start_with_zero(cls, start_number: int, end_number: int) -> int:
            """

            :param end_number: 随机数的最大值,包含
            :param start_number: 随机数的最小值,包含,默认=1
            :return: 从1开始的整数类型的随机数;[start_number,end_number] 取值范围为闭区间
            """
            return random.randint(start_number if start_number != 0 else 1, end_number if end_number != 1 else 2)

        @classmethod
        def character(cls, start_number: int, end_number: int) -> int:
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
                raise MockerExpressionException(remark="The correct expression for time:'+1h' or '-1h'.")
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
                raise MockerExpressionException('pick_list cannot be empty.')
            assert isinstance(pick_list, (str, list, tuple))
            if isinstance(pick_list, str):
                pick_list = eval(pick_list)
            return random.choice(pick_list)

    helper = Helper()


class MockerExpressionException(Exception):
    def __init__(self, exception='Incorrect mocker expression is used.', remark=''):
        super().__init__()
        self.exception = f'{exception}{remark}'

    def __str__(self):
        return self.exception


mocker = Mocker()
