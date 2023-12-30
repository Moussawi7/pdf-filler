from dataclasses import dataclass
from typing import Optional

from pdffiller.attributes import Font, Position


@dataclass
class CheckMark:
    key: str
    checked: bool
    position: Position
    symbol: Optional[str] = None
    font: Optional[Font] = None
