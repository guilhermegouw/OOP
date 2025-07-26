from .point import Point


def test_initialization():
    """
    Point class initializes with the given values.
    """
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_default_initialization():
    """
    Point class initializes with x=0, y=0 by default.
    """
    p = Point()
    assert p.x == 0
    assert p.y == 0


def test_reset():
    """
    The reset method sets x, y to 0.
    """
    p = Point(5, 10)
    p.reset()
    assert p.x == 0
    assert p.y == 0


def test_move():
    """
    The move method sets x, y to the given values.
    """
    p = Point(5, 10)
    p.move(3, -2)
    assert p.x == 3
    assert p.y == -2


def test_calculate_distance():
    """
    The calculate_distance method calculates the distance
    between two points.
    """
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    distance = p1.calculate_distance(p2)
    assert distance == 5.0  # 3-0, 4-0 -> sqrt(3^2 + 4^2) = 5.0
