from dataclasses import dataclass


@dataclass
class Position:
    page: int
    x: int
    y: int
    width: int
    height: int

