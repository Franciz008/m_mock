import random
import string

from random_ex.common import *


class String:
    @classmethod
    def _string_lower(cls, min_value=None, max_value=None) -> str:
        """
        :return: 随机小写英文字符
        """
        return cls.__get_string_by_source(string.ascii_lowercase, min_value, max_value)

    @classmethod
    def __get_string_by_source(cls, source=None, min_value: int = None, max_value: int = None) -> str:
        if inNone(min_value):
            length = random.randint(1, 9)
        elif inNone(max_value):
            length = min_value
        else:
            length = random.randint(min_value, max_value)
        str_list = []
        for i in range(length):
            str_list.append(random.choice(source))
        random.shuffle(str_list)
        return tuple_to_str(str_list)

    @classmethod
    def _string_upper(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机大写英文字符
        """
        return cls.__get_string_by_source(string.ascii_uppercase, min_value, max_value)

    @classmethod
    def _string_number(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机数字字符
        """
        return cls.__get_string_by_source(string.digits, min_value, max_value)

    @classmethod
    def _string_symbol(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机标点符号字符
        """
        return cls.__get_string_by_source(string.punctuation, min_value, max_value)

    @classmethod
    def _string(cls, min_value=None, max_value=None) -> str:
        """

        :return: 包含(英文/英文标点/数字)的随机字符
        """
        source = string.ascii_letters + string.digits + string.punctuation
        return cls.__get_string_by_source(source, min_value, max_value)

    @classmethod
    def string(cls, *args) -> str:
        """

        :param args: 参数,例如:返回字符的长度
        :return: 随机长度的英/数/英文标点符号的混合字符
        """
        if len(args) <= 1 or isinstance(args[0], int):
            return cls._string(*args)
        elif 3 >= len(args) >= 2:
            string_type = args[0]
            new_args = args[1:]
            if string_type == 'lower':
                return cls._string_lower(*new_args)
            elif string_type == 'upper':
                return cls._string_upper(*new_args)
            elif string_type == 'number':
                return cls._string_number(*new_args)
            elif string_type == 'symbol':
                return cls._string_symbol(*new_args)
            elif string_type == 'string':
                return cls._string(*new_args)
            else:
                return cls.__get_string_by_source(string_type, *new_args)
        elif len(args) > 3:
            raise MockerExpressionException('only 3 parameters are allowed.')
