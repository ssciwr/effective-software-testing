from __future__ import annotations
from effective_software_testing.gui import Gui
from PyQt6.QtCore import Qt
from pytestqt.qtbot import QtBot
from PyQt6.QtWidgets import QMessageBox
from typing import Any
from pytest import MonkeyPatch


def test_1x1_gui(qtbot: QtBot, monkeypatch: MonkeyPatch) -> None:
    gui = Gui(1)
    qtbot.add_widget(gui)
    messagebox_data = {}

    def _mock_QMessageBox_information(parent: Any, title: Any, text: Any) -> None:
        messagebox_data["title"] = title
        messagebox_data["text"] = text

    # mock QMessageBox.information() to just store the title/text and return
    monkeypatch.setattr(QMessageBox, "information", _mock_QMessageBox_information)

    with qtbot.wait_exposed(gui):
        gui.show()
    # click on board, we win the 1x1 game
    qtbot.mouseClick(gui.windowHandle(), Qt.MouseButton.LeftButton)
    qtbot.wait_until(lambda: "title" in messagebox_data)

    assert "win" in messagebox_data["title"].lower()
    assert "you won" in messagebox_data["text"].lower()
