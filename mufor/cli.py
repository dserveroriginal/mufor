import os
from mufor import format, loader
import pyperclip


def main(config, *args):
    """Main entry point."""

    errors = config["errors"]
    path = config["path"]

    command = input(path + "> ").split(" ")
    while True:
        match command:
            case ["ex"]:
                break
            case ["hp"]:
                print(_help_default())
            case ["cd", *args]:
                _cd(path, args[0])
            case ["ls"]:
                print(os.listdir(path))
            case ["mf", *args]:
                format.format_current_directory(" ".join(args))
            case ["dl", *args]:
                _download(config, path, *args)
            case ["dp", *args]:
                _download(config, path, *args, playlist=True)
            case _:
                if errors:
                    print("invalid command , for more info type hp")

        command = input(path + "> ").split(" ")

        # /media/dserver/Data/Audio/mufor/tests


def _cd(path: str, dir: str):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        try:
            os.chdir(path + "/" + dir)
        except FileNotFoundError:
            print("\ninvalid directory: " + dir)
    return len(dir)


def _help_default():
    help = "commands list:\n"
    help += "ex - exit the program\n"
    help += "hp - print this help message\n"
    help += "cd - change directory\n"
    help += "ls - list directory contents\n"
    help += "mf - format current directory\n"
    help += "dl - download video/audio\n"
    help += "dp - download playlist\n"
    help += "for more commands use shell commands (exit this program)"
    return help


def _download(config, path, *args, **kwargs):
    link = pyperclip.paste()
    if len(args) < 1:
        type = config["format"]["default"]
    elif args[0].startswith("--"):
        type = args[0].replace("-", "")
        link = link if len(args) < 2 else args[1]
    else:
        link = args[0]
        type = config["format"]["default"] if len(args) < 2 else args[1]

    print("\n" + type + "\n" + link + "\n")
    if input("\ncorrect? y/n\n").__contains__("n"):
        link = input("link: ")
        type = input("type: ")
    config["format"]["default"] = type
    loader.download(link, config, path + "/", **kwargs)