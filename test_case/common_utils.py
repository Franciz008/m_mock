from mock_py import mocker


def execute(params):
    print(f"{params}:{mocker.mocker(params)}")
