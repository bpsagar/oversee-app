from moviepy.editor import VideoFileClip
from PIL import Image

from .filetype import FileType


class CannotGenerateThumbnail(Exception):
    """Exception raised when a thumbnail cannot be created for the file"""
    pass


def _resize_image(filepath, outfilepath, width):
    """Resize, optimize and make the image progressive"""
    image = Image.open(filepath)
    ratio = image.size[0] / float(image.size[1])
    height = int(width / ratio)
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(outfilepath, optimize=True, progressive=True)


def create(filepath, outfilepath, width=200):
    """Generates a thumbnail for a file with a default width of 200px and
    height calculated based on the width/height ratio"""
    file_type = FileType.get_type(filepath=filepath)

    if file_type == FileType.unkown:
        raise CannotGenerateThumbnail()

    if file_type == FileType.video:
        video = VideoFileClip(filepath)
        # Saving the frame from the center of the video
        video.save_frame(outfilepath, t=video.duration / 2.)
        _resize_image(
            filepath=outfilepath, outfilepath=outfilepath, width=width)

    if file_type == FileType.image:
        _resize_image(filepath=filepath, outfilepath=outfilepath, width=width)
