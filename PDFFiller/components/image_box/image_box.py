from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Position, Dimension


@dataclass
class ImageBox:
    key: str
    position: Position
    path: Optional[str] = ''
    keep_proportion: Optional[bool] = False
    dimension: Optional[Dimension] = None
