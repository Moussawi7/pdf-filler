from dataclasses import dataclass, field
from PDFFiller.attributes import Dimension


@dataclass
class SigningAreaTheme:
    dimension: Dimension = field(default_factory=lambda: Dimension(
        width=100,
        height=100
    ))
