from mock_py import mocker
from random_ex import basic


def execute(params):
    print(f"{params}:{mocker.mocker(params)}")


def test_basic_string():
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
    print(basic.String.string())
    print(basic.String.string(7))
    print(basic.String.string(7, 10))
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