def inNone(obj):
    if isinstance(obj, (tuple, list)):
        # 都为空的就返回True
        boo = []
        for i in obj:
            boo.append(i in ('', None))
        return False if False in boo else True
    return obj in ('', None)


def tuple_to_str(objects) -> str:
    """
    :param objects: 被转换的元组/列表
    :return: 列表被转换后的字符串
    """
    return str(''.join(objects))


class MockPyExpressionException(Exception):
    def __init__(self, exception='Incorrect mocker expression is used.', remark=''):
        super().__init__()
        self.exception = f'{exception}{remark}'

    def __str__(self):
        return self.exception

    @classmethod
    def min_max_value_exception(cls, min_value, max_value):
        if (max_value is None or min_value is None) is False:
            if min_value >= max_value:
                raise MockPyExpressionException('min_value cannot be greater than or equal to max_value.')


mock_exception = MockPyExpressionException()
