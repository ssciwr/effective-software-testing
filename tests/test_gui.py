from __future__ import annotations
from effective_software_testing.gui import Gui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from pytestqt.qtbot import QtBot
from pytest import MonkeyPatch
from typing import List, Any


def test_1x1_gui_ignore_win_message_box(qtbot: QtBot, monkeypatch: MonkeyPatch) -> None:
    gui = Gui(1)
    qtbot.add_widget(gui)
    with qtbot.wait_exposed(gui):
        gui.show()

    # a function that takes any args and does nothing
    def do_nothing(*args: Any, **kwargs: Any) -> None:
        return

    # monkeypatch information message box call to instead call do_nothing
    # otherwise the test hangs waiting for the message box to be closed
    monkeypatch.setattr(QMessageBox, "information", do_nothing)
    # click on board -> we win the 1x1 game -> gui calls QMessageBox.information()
    qtbot.mouseClick(gui.windowHandle(), Qt.MouseButton.LeftButton)
    # it would be nice to check that the messagebox was displayed with the correct message - see next test...


def test_1x1_gui_test_win_message_box(qtbot: QtBot, qmessagebox_calls: List) -> None:
    gui = Gui(1)
    qtbot.add_widget(gui)
    with qtbot.wait_exposed(gui):
        gui.show()
    # click on board -> we win the 1x1 game -> gui calls QMessageBox.information()
    qtbot.mouseClick(gui.windowHandle(), Qt.MouseButton.LeftButton)
    # wait until gui has displayed a QMessageBox
    qtbot.wait_until(lambda: len(qmessagebox_calls) > 0)
    assert len(qmessagebox_calls) == 1
    assert qmessagebox_calls[0]["name"] == "information"
    assert "win" in qmessagebox_calls[0]["title"].lower()
    assert "you won" in qmessagebox_calls[0]["text"].lower()
