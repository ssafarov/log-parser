import unittest

from parser import file_name
from parser import file_size


class MyTestCase(unittest.TestCase):
    def test_filesize(self):
        """
        Test file size function
        """
        file = 'parser.py'
        result = file_size(file)

        self.assertGreater(result, 0)

    def test_filename(self):
        """
        Test file name function
        """
        file = 'parser.py'
        result = file_name(file)

        self.assertEqual(result, 'parser')


if __name__ == '__main__':
    unittest.main()
