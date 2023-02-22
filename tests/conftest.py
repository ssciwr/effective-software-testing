import pytest
from pytest import MonkeyPatch
from PyQt6.QtWidgets import QMessageBox
from typing import Any, List, Callable


@pytest.fixture()
def qmessagebox_calls(monkeypatch: MonkeyPatch) -> List:
    # create a list to store any QMessageBox calls that are made
    calls = []

    def _make_callback(name: str) -> Callable:
        # this function has the same calling interface as the qmessagebox static methods like information()
        def _mock(parent: Any, title: Any, text: Any) -> None:
            # but instead of displaying the message box it just appends the supplied arguments to the calls list
            calls.append({"name": name, "title": title, "text": text})

        return _mock

    for name in ["information", "warning", "critical"]:
        # mock QMessageBox static method `name` with our callback
        monkeypatch.setattr(QMessageBox, name, _make_callback(name))

    return calls
