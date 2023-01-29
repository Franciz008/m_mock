def inNone(obj):
    return obj in ('', None)


def tuple_to_str(objects) -> str:
    """
    :param objects: 被转换的元组/列表
    :return: 列表被转换后的字符串
    """
    return str(''.join(objects))


class MockerExpressionException(Exception):
    def __init__(self, exception='Incorrect mocker expression is used.', remark=''):
        super().__init__()
        self.exception = f'{exception}{remark}'

    def __str__(self):
        return self.exception
