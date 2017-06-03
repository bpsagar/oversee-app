from moviepy.editor import VideoFileClip
from PIL import Image

from .filetype import FileType


class CannotGenerateThumbnail(Exception):
    """Exception raised when a thumbnail cannot be created for the file"""
    pass


def create(filepath, outfilepath, width=200):
    """Generates a thumbnail for a file with a default width of 100px and
    height calculated based on the width/height ratio"""
    file_type = FileType.get_type(filepath=filepath)

    if file_type == FileType.unkown:
        raise CannotGenerateThumbnail()

    if file_type == FileType.video:
        video = VideoFileClip(filepath)
        resized_video = video.resize(width=width)
        # Saving the frame from the center of the video
        resized_video.save_frame(outfilepath, t=video.duration / 2.)

    if file_type == FileType.image:
        image = Image.open(filepath)
        ratio = image.size[0] / float(image.size[1])
        height = int(width / ratio)
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(outfilepath)
