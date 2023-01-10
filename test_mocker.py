from mocker_utils import mocker


def test():
    # for i in range(20):
    #     print(i, mocker.basic.boolean(1, 5, False))
    # print(mocker.mocker("@boolean(1, 5, False)"))
    # print(mocker.mocker("@date('%Y-%m-%d %H:%M:%S', '+1d')"))
    # print(mocker.mocker("@date('%Y-%m-%d %H:%M:%S', '+24h')"))
    # print(mocker.date.date('%y-%m-%d', '-20d'))
    # print(mocker.date.time('', '+2sec'))
    # print(mocker.date.time('', '+4sec'))
    print(mocker.Helper().pick('(1,2,3)'))
    print(mocker.mocker("""@pick('("1",2,"3")')"""))
