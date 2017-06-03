import unittest

from oversee import thumbnail


class TestFileType(unittest.TestCase):
    """Tests for thumbnail create method"""

    def test_create(self):
        with self.assertRaises(thumbnail.CannotGenerateThumbnail):
            thumbnail.create('/home/abcd.xyz', '/home/abcd123.xyz')
