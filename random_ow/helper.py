import random

from random_ow.common import inNone, MockPyExpressionException


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
