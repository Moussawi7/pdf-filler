from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Font, Position, Dimension


@dataclass
class TextField:
    key: str
    value: str
    position: Position
    dimension: Dimension
    font: Optional[Font] = None
