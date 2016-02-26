import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        super(BasicTest, self).setUp()

    def test_basic(self):
        self.assertEqual(1, 1)
