def inNone(obj):
    if isinstance(obj, (tuple, list)):
        # 只要有一个是空的就返回True
        boo = []
        for i in obj:
            boo.append(i in ('', None))
        return True if True in boo else False
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
