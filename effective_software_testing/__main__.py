from __future__ import annotations
import click
import sys
from PyQt6.QtWidgets import QApplication
from effective_software_testing.gui import Gui
from effective_software_testing import __version__

@click.command()
@click.option(
    "-s",
    "--size",
    type=click.IntRange(1, 16),
    default=3,
    show_default=True,
    help="Size of the board",
)
@click.version_option(__version__)
def main(size: int) -> None:
    app = QApplication(sys.argv)
    window = Gui(size)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
