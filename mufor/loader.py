import os
from mufor import ffmpegplug
from mufor import ytdlp
import hashlib


def download(config, url: str, dir: str, id: str = "", playlist: bool = False):
    """Download a file from a URL to a local file."""

    if not playlist:
        singles = _get_ids(config["path"]["links"])["id"]
        if id in singles:
            return ""
        return [_load(url, config, dir)]
    else:
        return load_all(config, dir, link=url)


def load_all(config, dir: str, link: str = ""):
    if link.__eq__(""):
        link_list = open(config["path"]["links"] + "links.txt", "r").read().split("\n")
    else:
        link_list = [link]

    ids = []

    for link in link_list:
        if link.__eq__(""):
            continue
        info = ytdlp.get_info(link)
        if info is None:
            raise Exception("Error loading info")
        print(link)

        if info["_type"] == "video":
            ids += download(config, link, dir, info["id"])
            continue

        for video in info["entries"]:
            ids += download(config, video["webpage_url"], dir, video["id"])

    return ids


def _load(url: str, config, dir: str = ""):
    if url.__eq__(""):
        return ""
    info = ytdlp.get_info(url)
    if info is None:
        raise Exception("Error loading info")

    tags = {
        "date":info["upload_date"],
        "title":info["title"],
        "artist":info["channel"],
        "playlist":info["playlist"],
        "id":info["id"]
    }

    if dir.__eq__(""):
        dir = config["path"]["files"]

    filename = (
        dir
        + "/"
        + config["sheme"]
        % {
            "date": tags["date"],
            "title": tags["title"],
            "artist": tags["artist"],
            "album": tags["playlist"],
            "comment": tags["id"],
            "ext": "%(ext)s",
            "md5": hashlib.md5(tags["id"].encode()).hexdigest(),
            "id": id,
            "version": config["version"]["number"] + config["version"]["name"],
        }
    )
    filename = ytdlp.load(url, filename, config["format"][config["format"]["default"]])

    if filename.endswith(".NA") or filename.__eq__(""):
        return ""

    # print(filename)

    newfilename = filename.replace(
        filename.split(".")[-1], config["format"][config["format"]["default"]]
    )

    # print(newfilename, filename)

    filename = ffmpegplug.convert(
        filename,
        newfilename,
        date=tags["date"],
        title=tags["title"],
        artist=tags["artist"],
        album=tags["playlist"],
        comment=tags["id"],
    )
    
    ids=_get_ids(config["path"]["links"])
    ids["id"].append(tags["id"])
    _write_ids(config, ids)

    return tags["id"]


def _write_ids(config, loaded):
    import json

    path = config["path"]["links"]
    file = open(path + "loaded.json", "w")
    json.dump(loaded, file)
    file.close()


def _get_ids(path):
    import json

    file = open(path + "loaded.json", "r")
    loaded = json.load(file)
    file.close()
    return loaded
