from unittest import TestCase
from src.testfuncs.detect_tests import test_func, TestCodeReachable


class Test(TestCase):
    def test_test_only(self):
        self.assertRaises(TestCodeReachable, test_func)
