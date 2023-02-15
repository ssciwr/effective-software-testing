from __future__ import annotations
import click
import sys
from PyQt6.QtWidgets import QApplication
from effective_software_testing.gui import Gui


@click.command()
@click.option("-s", "--size", default=3, show_default=True, help="Size of the board")
def main(size: int) -> None:
    app = QApplication(sys.argv)
    window = Gui(size)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
