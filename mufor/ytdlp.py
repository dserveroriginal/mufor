from yt_dlp import YoutubeDL
import os




def get_info(url: str):
    """Get a playlist from a URL."""

    with YoutubeDL({"dump_single_json": True, "quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def load(
    url: str,
    filename: str,
    format: str = "",
    ffmpeg_location: str ="/usr/bin/"
):
    """Load a file from a URL."""


    # someone please fix this, I'm dumb
    selection="bestaudio/best"
    ydl_opts={
        "format":selection,
        "outtmpl": filename, 
        "writethumbnail":True,
        "postprocessors": [{"key":"FFmpegExtractAudio","preferredcodec":format}],
        "verbose":True,
        "ffmpeg_location":ffmpeg_location
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        file = ydl.prepare_filename(info)
        info = ydl.post_process(filename, info)


    print(file)
    return file


