import os
from mufor import ffmpegplug
from mufor import ytdlp
import hashlib


def download(url: str, config, dir: str, playlist=False, load=True,**kwargs):
    """Download a file from a URL to a local file."""

    if not playlist:
        return _load(url, config, dir,load, **kwargs)
    else:
        info = ytdlp.get_playlist(url)
        files = []

        if info is not None:
            for video in info["entries"]:
                files += [_load(video["webpage_url"], config, dir, load, **kwargs)]

        return files


def _load(url: str, config, dir: str, load, **kwargs):
    filename = dir + "%(release_date,upload_date|Unknown)s__"
    filename += "%(fulltitle|Unnamed)s__"
    filename += "%(creator,channel|Author unknown)s__"
    filename += "%(playlist|None)s__"
    filename += "%(id)s__"
    filename += ".%(ext)s"
    filename = ytdlp.load(
        url,
        filename,
        load,
        config["format"][config["format"]["default"]],
        kwargs=kwargs,
    )

    if filename.__eq__(""):
        return filename
    
    tagparts = filename.split(".")
    # ext= tagparts[-1]
    tagparts = [tagparts[0].split("/")[-1]] + tagparts[1:]
    tags = tagparts[-2].split("__")

    if filename.endswith(".NA"):
        return ""

    newfilename = filename.replace(" ", "_")
    filename = newfilename if os.rename(filename, newfilename) is None else filename

    # print(filename)

    newfilename = dir + (
        config["sheme"]
        % {
            "version": config["version"]["number"] + config["version"]["name"],
            "md5": hashlib.md5(tags[4].encode()).hexdigest(),
            "date": tags[0],
            "title": tags[1],
            "artist": tags[2],
            "album": tags[3],
            "comment": tags[4],
            "ext": config["format"][config["format"]["default"]],
        }
    )

    # print(newfilename, filename)

    filename = ffmpegplug.convert(
        filename,
        newfilename,
        date=tags[0],
        title=tags[1],
        artist=tags[2],
        album=tags[3],
        comment=url,
    )

    return filename
