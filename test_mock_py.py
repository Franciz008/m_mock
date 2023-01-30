from mock_py import mocker
from random_ow import basic


def execute(params):
    print(f"{params}:{mocker.mocker(params)}")


class TestBasic:
    def test_basic_character(self):
        print(basic.CharacterOw.character())
        execute("@character()")
        execute("@character('lower')")
        execute("@character('upper')")
        execute("@character('number')")
        execute("@character('symbol')")
        execute("@character('aeiou')")

    def test_basic_integer(self):
        print(basic.IntegerOw.integer())
        execute("@integer(2,4)")
        execute("@integer(3)")
        execute("@integer()")
        execute("@integer(2,2)")

    def test_basic_boolean(self):
        print(basic.BooleanOw.boolean())
        execute("@boolean(2,4)")
        execute("@boolean(3)")
        execute("@boolean()")
        execute("@boolean(2,2)")

    def test_basic_float(self):
        # for i in range(20):
        #     print(i, mocker.basic.boolean(1, 5, False))
        # print(mocker.mocker("@boolean(1, 5, False)"))
        # print(mocker.mocker("@date('%Y-%m-%d %H:%M:%S', '+1d')"))
        # print(mocker.mocker("@date('%Y-%m-%d %H:%M:%S', '+24h')"))
        # print(mocker.date.date('%y-%m-%d', '-20d'))
        # print(mocker.date.time('', '+2sec'))
        # print(mocker.date.time('', '+4sec'))
        # print(mocker.Helper().pick('(1,2,3)'))
        # print(mocker.mocker("""@pick('("1",2,"3")')"""))
        print(basic.FloatOw.float())
        execute("@float(2,4)")
        execute("@float(3)")
        execute("@float()")
        execute("@float(2,2)")

    def test_basic_string(self):
        print(basic.StringOw.string())
        print(basic.StringOw.string(7))
        print(basic.StringOw.string(7, 10))
        execute("@string(2)")
        execute('@string("lower", 3)')
        execute('@string("upper", 3)')
        execute('@string("number", 3)')
        execute('@string("symbol", 3)')
        execute('@string("aeiou", 3)')
        execute('@string("lower", 1, 3)')
        execute('@string("upper", 1, 3)')
        execute('@string("number", 1, 3)')
        execute('@string("symbol", 1, 3)')
        execute('@string("aeiou", 1, 3)')
        execute('@string("chinese", 1, 3)')
        execute('@string("cn_symbol", 1, 3)')
        execute('@string("cn_string", 3, 9)')
        execute('@string("cn_string", 1)')
