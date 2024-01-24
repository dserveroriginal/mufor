from yt_dlp import YoutubeDL


ydlaudio = ["3gp", "aac", "m4a", "mp3", "ogg", "wav"]
ydl = ydlaudio + ["mp4", "webm", "flv"]


def get_playlist(url: str, youtube_dl: str = "yt-dlp"):
    """Get a playlist from a URL."""
    # if youtube_dl.__eq__("yt-dlp"):

    with YoutubeDL({"dump_single_json": True}) as ydl:
        info = ydl.extract_info(url, download=False)
    # else:

    # TODO: do something about this
    return info


def load(
    url: str,
    filename: str,
    load: bool,
    format: str = "",
    youtube_dl: str = "yt-dlp",
    **kwargs,
):
    """Load a file from a URL."""

    format, filename = _get_format(format, filename)

    file = filename
    try:
        # if youtube_dl.__eq__("yt-dlp"):

        with YoutubeDL({"outtmpl": filename, "format": format}) as ydl:
            file = ydl.prepare_filename(ydl.extract_info(url, download=load))
    except:
        if format.__eq__(""):
            raise Exception("Error loading file")
        # if youtube_dl.__eq__("yt-dlp"):
        file = _load_any(url, filename, load)

    return file


def _load_any(
    url: str,
    filename: str,
    download: bool,
    youtube_dl: str = "yt-dlp",
):
    """Last resort for loading a file from a URL."""

    return load(url, filename, download)


def _get_format(format: str, filename: str):
    if format in ydlaudio:
        return ["bestaudio[ext={audio}]".format(audio=format), filename]
    elif format in ydl:
        return [
            "bestvideo[ext={video}]+bestaudio*/best[ext={video}]".format(video=format),
            filename,
        ]
    else:
        format = "bestvideo+bestaudio/best"
        for ext in ydl:
            filename = filename.replace(ext, "%(ext)s")
        print(filename)
        return [format, filename]
