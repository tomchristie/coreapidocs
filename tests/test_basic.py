import sys
import unittest
from coreapidocs import example


class TestBasic(unittest.TestCase):

    def setUp(self):
        super(TestBasic, self).setUp()
        sys.argv = ["example.py", "document.json"]
        example.app.config['TESTING'] = True
        self.app = example.app.test_client()

    def test_missing_arg_filename(self):
        sys.argv = ["example.py"]
        rv = self.app.get('/')
        assert 'Missing file parameter ie. document.json' in rv.data

    def test_filename_not_exists(self):
        sys.argv = ["example.py", "missing.json"]
        rv = self.app.get('/')
        assert 'No such file or directory - missing.json' in rv.data
