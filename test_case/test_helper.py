from random_ow.date import date
from random_ow.helper import helper
from test_case.common_utils import execute


class TestHelper:
    def test_helper(self):
        helper.pick('(1,2,3)')
        execute("""@pick('("1",2,"3")')""")
