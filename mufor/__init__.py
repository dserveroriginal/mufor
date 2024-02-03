from mufor.cli import _update_files


def main(*args):
    """Main entry point."""

    from mufor import config as cfg

    config = cfg.load()

    print("version: " + config["version"]["number"] + "-" + config["version"]["name"])
    print(config["format"])
    print(config["path"])
    print(config["sheme"])
    
    if args.__len__() > 0:
        if args[0].__contains__("-u"):
            _update_files(config, config["path"]["files"], "-a")
            return 0
    
    if config["ui"]["mode"].startswith("cli"):
        _load_cli(config, *args)
    elif config["ui"]["mode"].startswith("gui"):
        _load_gui(config, args)
    return 0


def _load_cli(config, *args):
    """Load CLI."""

    from mufor import cli

    cli.main(config, *args)


def _load_gui(config, *args):
    """Load GUI."""
    # TODO: implement
    # from mufor import gui
    # gui.main(*args)
