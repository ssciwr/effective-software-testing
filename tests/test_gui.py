from __future__ import annotations
from effective_software_testing.gui import Gui
from PyQt6.QtCore import Qt
from pytestqt.qtbot import QtBot
from pytest import MonkeyPatch
from typing import List


def test_1x1_gui(
    qtbot: QtBot, monkeypatch: MonkeyPatch, qmessagebox_calls: List
) -> None:
    gui = Gui(1)
    qtbot.add_widget(gui)
    with qtbot.wait_exposed(gui):
        gui.show()
    # click on board -> we win the 1x1 game -> gui calls QMessageBox.information()
    qtbot.mouseClick(gui.windowHandle(), Qt.MouseButton.LeftButton)
    # wait until gui has called QMessageBox.information()
    qtbot.wait_until(lambda: len(qmessagebox_calls) > 0)
    assert len(qmessagebox_calls) == 1
    assert qmessagebox_calls[0]["name"] == "information"
    assert "win" in qmessagebox_calls[0]["title"].lower()
    assert "you won" in qmessagebox_calls[0]["text"].lower()
