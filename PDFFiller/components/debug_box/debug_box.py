from dataclasses import dataclass
from typing import Optional

from PDFFiller.attributes import Color, Position


@dataclass
class DebugBox:
    key: str
    position: Position
    text_size: Optional[int] = 9
    text_color: Optional[Color] = None
    background_color: Optional[Color] = None
    border_thickness: Optional[float] = None
    border_color: Optional[Color] = None

