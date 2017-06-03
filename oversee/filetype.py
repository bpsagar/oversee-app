import os


class FileType(object):
    """Class that provides methods related to the file"""

    _IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
    _VIDEO_EXTENSIONS = ['mp4', 'mov']

    image = 'IMAGE'
    video = 'VIDEO'
    unkown = 'UNKOWN'

    @classmethod
    def get_type(cls, filepath):
        """Returns the type of file from the file path"""
        filename = os.path.basename(filepath)

        if '.' not in filename:
            return FileType.unkown

        extension = filename.split('.')[-1]
        if extension in cls._IMAGE_EXTENSIONS:
            return FileType.image

        if extension in cls._VIDEO_EXTENSIONS:
            return FileType.video

        return FileType.unkown
