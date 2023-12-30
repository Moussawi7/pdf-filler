from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Font, Position


@dataclass
class TextField:
    key: str
    value: str
    position: Position
    font: Optional[Font] = None
