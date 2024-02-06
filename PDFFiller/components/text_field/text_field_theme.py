from dataclasses import dataclass, field

from PDFFiller.attributes import Font, Color, Dimension


@dataclass
class TextFieldTheme:
    font: Font = field(default_factory=lambda: Font(
        color=Color(0, 0, 0),
        size=12,
        family="Helvetica"
    ))
    dimension: Dimension = field(default_factory=lambda: Dimension(
        width=120,
        height=24
    ))
