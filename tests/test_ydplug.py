from tests import os_functions
import unittest

from mufor import ytdlp


def _download(
    url: str,
    filename: str,
    load: bool,
    format: str = "mp4",
    youtube_dl: str = "yt-dlp",
):
    """Download a file from a URL to a local file."""

    return ytdlp.load(url, filename, load, format, youtube_dl)
    # add version=True for debugging


def _check_download(
    url: str,
    filename: str,
    format: str = "mp4",
    youtube_dl: str = "yt-dlp",
):
    """Check if download function works."""

    filename = _download(url, filename, True, format, youtube_dl)

    if filename.endswith(".%(ext)s"):
        filename = filename.replace(".%(ext)s", ".*")

    print(filename)

    result = os_functions.exist(filename)
    os_functions.try_rm(filename)

    return result


class TestYDPlug(unittest.TestCase):
    def _assert_download(
        self,
        filename: str,
        url: str = "https://www.youtube.com/watch?v=fRh97wohgJ4",
        format: str = "mp4",
        youtube_dl: str = "yt-dlp",
    ):
        """Assert that download function works."""

        self.assertTrue(_check_download(url, filename, format, youtube_dl))

    def test_video_download(self):
        """Test download function."""

        filename = os_functions.fl_gen("test_video.mp4")

        self._assert_download(filename)

    def test_audio_download(self):
        """Test download function."""

        filename = os_functions.fl_gen("test_audio.mp3")

        self._assert_download(filename, format="mp3")

    def test_playlist(self):
        info = ytdlp.get_playlist(
            "https://www.youtube.com/playlist?list=PLtyo3aqsNv_Oe686OmaAi1heDjjnxYRmw"
        )

        file = os_functions.write_json(info, os_functions.fl_gen("test_playlist.json"))
        os_functions.try_rm(file)

        self.assertTrue(info is not None)
