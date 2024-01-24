from tests import os_functions
import unittest

from mufor import ffmpegplug, ytdlp


def _convert(filename, new_filename):
    """Convert a file to another format."""

    ffmpegplug.convert(filename, new_filename)


def _check_convert(filename, new_filename):
    """Check if convert function works."""

    filename = _convert(filename, new_filename)

    result = os_functions.exist(filename)
    os_functions.try_rm(filename)
    return result


class TestFFmpegPlug(unittest.TestCase):
    def _assert_convert(self, filename, new_filename):
        """Assert that convert function works."""

        self.assertTrue(_check_convert(filename, new_filename))

    def test_convert(self):
        """Test convert function."""

        filename = os_functions.fl_gen("test_convert.mp4")
        url = "https://www.youtube.com/watch?v=KXG_5xXT6_U"
        filename = ytdlp.load(url, filename)

        new_filename = os_functions.fl_gen("test_convert.mp3")

        self._assert_convert(filename, new_filename)
