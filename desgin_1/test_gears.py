import pytest
from gears import Gear


def test_gear_initialization():
    gear = Gear(50, 11, 26, 1.5)
    assert gear.chainring == 50
    assert gear.cog == 11


def test_gear_ratio():
    gear = Gear(50, 11, 26, 1.5)
    ratio = gear.ratio()
    assert ratio == 50 / 11


def test_inches():
    gear = Gear(52, 11, 26, 1.5)
    inches = gear.inches()
    assert inches == pytest.approx(137.09, rel=1e-2)
