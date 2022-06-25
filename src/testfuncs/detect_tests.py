import sys


class TestFunctionUsedError(Exception):
    """Raised when a function only meant for tests is used in source code"""

    def __init__(self, func):
        super().__init__(f"You cannot use the function {func.__name__} outside of test code")


class TestCodeReachable(Exception):
    """Test class to verify that test code is reachable"""


def test_only(func):
    def detect_testing(*args):
        if 'unittest' in sys.modules:
            func(*args)
        else:
            raise TestFunctionUsedError(func)

    return detect_testing


###############################################################
# testing only
@test_only
def test_func():
    raise TestCodeReachable()


if __name__ == '__main__':
    try:
        test_func()
    except TestFunctionUsedError:
        print("successfully identified as test only")
    else:
        raise Exception("Test only code erroneously exeecuted outside tests")
