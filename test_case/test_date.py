from random_ow.date import date
from test_case.common_utils import execute


class TestDate:
    def test_date(self):
        execute("@date('%Y-%m-%d %H:%M:%S', '+1d')")
        execute("@date('%Y-%m-%d %H:%M:%S', '+24h')")
        print(date.date('%y-%m-%d', '-20d'))
        print(date.date())

    def test_time(self):
        print(date.time('', '+2sec'))
        print(date.time('', '+4sec'))
        execute("@time('', '+4sec')")
