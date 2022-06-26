from unittest import TestCase
from src.testfuncs.detect_tests import test_only_foo, TestCodeReachable


class Test(TestCase):
    def test_test_only(self):
        self.assertRaises(TestCodeReachable, test_only_foo)
