from dataclasses import dataclass, field

from PDFFiller.attributes import Color, Font


@dataclass
class DebugBoxTheme:
    font: Font = field(default_factory=lambda: Font(
        color=Color(0, 0, 0),
        size=12,
        family="Helvetica"
    ))
    background_color: Color = field(default_factory=lambda: Color(256, 256, 0))
    border_thickness: float = 0.3
    border_color: Color = field(default_factory=lambda: Color(256, 126, 0))
