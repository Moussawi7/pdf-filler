from dataclasses import dataclass

from pdffiller.attributes import Position


@dataclass
class ImageBox:
    key: str
    path: str
    position: Position
    keep_proportion: bool
