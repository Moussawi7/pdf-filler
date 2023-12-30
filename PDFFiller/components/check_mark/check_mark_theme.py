from dataclasses import dataclass, field

from PDFFiller.attributes import Font, Color


@dataclass
class CheckMarkTheme:
    symbol: str = field(default_factory=lambda: "X")
    font: Font = field(default_factory=lambda: Font(
        color=Color(0, 0, 0),
        size=12,
        family="Helvetica"
    ))
