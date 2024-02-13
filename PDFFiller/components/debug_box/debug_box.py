from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Font, Color, Position, Dimension


@dataclass
class DebugBox:
    key: str
    position: Position
    dimension: Dimension
    font: Optional[Font] = None
    background_color: Optional[Color] = None
    border_thickness: Optional[float] = None
    border_color: Optional[Color] = None

