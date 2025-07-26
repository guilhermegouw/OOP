import math


class Point:
    """
    Point class represents a point in 2-dimensional
    geometric coordinates.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a Point instance with given x and y
        coordinates.

        Args:
            x (float): The x-coordinate defaults to 0.0.
            y (float): The y-coordinate defaults to 0.0.
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Resets the point to the origin (0, 0).
        """
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        """
        Moves the point to a new location specified by x and y.

        Args:
            x (float): The new x-coordinate.
            y (float): The new y-coordinate.
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculates the distance between this point and another point.

        Args:
            other (Point): The other point.

        Returns:
            float: The distance between the two points.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
