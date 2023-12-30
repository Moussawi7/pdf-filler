from dataclasses import dataclass

from PDFFiller.attributes import Position


@dataclass
class ImageBox:
    key: str
    path: str
    position: Position
    keep_proportion: bool
