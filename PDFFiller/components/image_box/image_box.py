from dataclasses import dataclass

from PDFFiller.attributes import Position, Dimension


@dataclass
class ImageBox:
    key: str
    path: str
    position: Position
    dimension: Dimension
    keep_proportion: bool
