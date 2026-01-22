"""Example module demonstrating generic types and dataclasses."""

from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Comparable(Protocol):
    """Protocol for types that support comparison operations."""

    def __lt__(self, other: "Comparable") -> bool: ...
    def __gt__(self, other: "Comparable") -> bool: ...


@dataclass
class Point:
    """A 2D point with x and y coordinates."""

    x: float
    y: float

    def distance_from_origin(self) -> float:
        """Calculate distance from origin.

        Returns:
            Euclidean distance from (0, 0)
        """
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other: "Point") -> "Point":
        """Add two points together.

        Args:
            other: Another point

        Returns:
            New point with summed coordinates
        """
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Person:
    """A person with name and age."""

    name: str
    age: int
    email: str | None = None

    def is_adult(self) -> bool:
        """Check if person is an adult.

        Returns:
            True if age >= 18
        """
        return self.age >= 18


class Container(Generic[T]):
    """A generic container that holds items of type T."""

    def __init__(self) -> None:
        """Initialize empty container."""
        self._items: list[T] = []

    def add(self, item: T) -> None:
        """Add item to container.

        Args:
            item: Item to add
        """
        self._items.append(item)

    def get_all(self) -> list[T]:
        """Get all items in container.

        Returns:
            List of all items
        """
        return self._items.copy()

    def find_first(self, predicate: Callable[[T], bool]) -> T | None:
        """Find first item matching predicate.

        Args:
            predicate: Function that returns True for matching items

        Returns:
            First matching item or None
        """
        for item in self._items:
            if predicate(item):
                return item
        return None


def process_numbers(numbers: list[int]) -> dict[str, float]:
    """Process a list of numbers and return statistics.

    Args:
        numbers: List of integers to process

    Returns:
        Dictionary with 'mean', 'min', 'max' keys
    """
    if not numbers:
        return {"mean": 0.0, "min": 0.0, "max": 0.0}

    return {
        "mean": sum(numbers) / len(numbers),
        "min": float(min(numbers)),
        "max": float(max(numbers)),
    }


if __name__ == "__main__":
    # Example with Point
    p1 = Point(3.0, 4.0)
    p2 = Point(1.0, 2.0)
    print(f"Point 1 distance: {p1.distance_from_origin()}")
    print(f"Sum: {p1 + p2}")

    # Example with Person
    person = Person("Alice", 25, "alice@example.com")
    print(f"{person.name} is adult: {person.is_adult()}")

    # Example with Container
    container: Container[int] = Container()
    container.add(1)
    container.add(2)
    container.add(3)
    print(f"Container items: {container.get_all()}")

    # Example with process_numbers
    numbers = [1, 2, 3, 4, 5]
    stats = process_numbers(numbers)
    print(f"Stats: {stats}")
