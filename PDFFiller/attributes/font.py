from dataclasses import dataclass

from .color import Color


@dataclass
class Font:
    family: str
    color: Color
    size: int
