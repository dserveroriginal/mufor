import subprocess
import os


def convert(inputfile: str, outputfile: str, ffmpeg: str = "ffmpeg", **kwargs):
    """Convert a file to another format."""

    tags = [f"{key}={value}" for key, value in kwargs.items()]

    args = []

    for index in range(len(tags)):
        args += ["-metadata"] + [tags[index]]

    process = [ffmpeg, "-i", inputfile] + args + [outputfile]

    command = ""

    for part in process:
        command += part + " "

    print(command)

    process = subprocess.Popen(process)
    if process.wait() != 0:
        raise Exception("Error converting file")
    os.remove(inputfile)
    return outputfile
