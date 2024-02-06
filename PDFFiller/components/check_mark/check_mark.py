from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Font, Position, Dimension


@dataclass
class CheckMark:
    key: str
    position: Position
    checked: Optional[bool] = False
    dimension: Optional[Dimension] = None
    symbol: Optional[str] = None
    font: Optional[Font] = None
