import pytest

from detect_kit import __version__

pytestmark = pytest.mark.lib


def test_version() -> None:
    assert __version__ == "0.1.0"
