from dataclasses import dataclass, field

from PDFFiller.attributes import Color


@dataclass
class DebugBoxTheme:
    text_size: int = field(default_factory=lambda: 9)
    text_color: Color = field(default_factory=lambda: Color(0, 0, 0))
    background_color: Color = field(default_factory=lambda: Color(256, 256, 0))
    border_thickness: float = 0.3
    border_color: Color = field(default_factory=lambda: Color(256, 126, 0))
