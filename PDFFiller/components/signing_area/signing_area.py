from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Position, Dimension


@dataclass
class SigningArea:
    key: str
    position: Position
    path: Optional[str] = ''
    dimension: Optional[Dimension] = None
