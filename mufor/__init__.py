import sys


def main(use_cfg: bool = True, *args):
    """Main entry point."""

    from mufor import config as cfg

    config = cfg.load()

    print("version: " + config["version"]["number"] + "-" + config["version"]["name"])
    print(config["format"])
    print(config["path"])
    print(config["sheme"])

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
