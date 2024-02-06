from dataclasses import dataclass, field

from PDFFiller.attributes import Font, Color, Dimension


@dataclass
class CheckMarkTheme:
    symbol: str = field(default_factory=lambda: "X")
    font: Font = field(default_factory=lambda: Font(
        color=Color(0, 0, 0),
        size=12,
        family="Helvetica"
    ))
    dimension: Dimension = field(default_factory=lambda: Dimension(
        width=20,
        height=20
    ))
