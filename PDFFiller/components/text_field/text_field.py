from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Font, Position, Dimension


@dataclass
class TextField:
    key: str
    position: Position
    value: Optional[str] = ''
    dimension: Optional[Dimension] = None
    font: Optional[Font] = None
