import unittest

from oversee.filetype import FileType


class TestFileType(unittest.TestCase):
    """Tests for FileType class"""

    def test_get_type(self):
        image_path = '/home/documents/abcd.jpg'
        video_path = '/home/video.mov'
        unkown_path1 = '/home/test.html'
        unkown_path2 = '/home/textfile'

        self.assertEqual(FileType.get_type(image_path), FileType.image)
        self.assertEqual(FileType.get_type(video_path), FileType.video)
        self.assertEqual(FileType.get_type(unkown_path1), FileType.unkown)
        self.assertEqual(FileType.get_type(unkown_path2), FileType.unkown)
