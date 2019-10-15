__author__ = 'hs434'

import unittest
from Experiment_hw_1 import Greeter


class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Welcome to this interesting world!')


if __name__ == '__main__':
    unittest.main()
