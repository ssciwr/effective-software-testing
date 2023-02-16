from effective_software_testing.__main__ import main
from effective_software_testing import __version__

from click.testing import CliRunner


def test_cli_version() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output
