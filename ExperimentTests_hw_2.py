__author__ = 'k0emt'

import unittest
from Experiment_hw_1 import Greeter


class MyTestCase(unittest.TestCase):
        def test_default_greeting_set(self):
                    greeter = Greeter()
                            self.assertEqual(greeter.message, 'Hello world!')


                            if __name__ == '__main__':
                                    unittest.main()
