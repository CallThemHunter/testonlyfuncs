import sys


class TestFunctionUsedError(Exception):
    """Raised when a function only meant for tests is used in source code"""

    def __init__(self, func):
        super().__init__(f"You cannot use the function {func.__name__} outside of test code")


class TestFunctionHasIncorrectNameError(Exception):
    """Raised when a function marked as test only does not start with 'test_only'"""

    def __init__(self, func):
        super().__init__(f"The function {func.__name__} should start with test_only to indicate its usage")


class TestCodeReachable(Exception):
    """Test class to verify that test code is reachable"""


def test_only(func):
    def detect_testing(*args):
        if 'unittest' in sys.modules:
            func(*args)
        elif not func.__name__.startswith("test_only"):
            raise TestFunctionHasIncorrectNameError(func)
        else:
            raise TestFunctionUsedError(func)

    return detect_testing


###############################################################
# testing only
@test_only
def test_only_foo():
    raise TestCodeReachable()


if __name__ == '__main__':
    try:
        test_only_foo()
    except TestFunctionUsedError:
        print("successfully identified as test only")
    else:
        raise Exception("Test only code erroneously exeecuted outside tests")
