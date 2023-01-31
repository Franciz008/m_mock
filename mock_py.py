import random
import re
from datetime import datetime, timedelta

from random_ow import basic
from random_ow.common import MockPyExpressionException
from random_ow.date import date
from random_ow.helper import helper


class MockPy:

    def mocker(self, mock_str):
        keyword = self.get_mocker_key(mock_str)
        args = self.get_mocker_params_to_tuple(mock_str)
        if keyword == 'date':
            return date.date(*args)
        elif keyword == 'time':
            return date.time(*args)
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
            return helper.pick(*args)
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


mocker = MockPy()
