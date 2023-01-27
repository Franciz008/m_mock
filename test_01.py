import random
import string

import mocker_utils


def test_basic():
    print(random.randint(1, 1))
    print(mocker_utils.mocker.basic.string())
