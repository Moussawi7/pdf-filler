from dataclasses import dataclass, field
from PDFFiller.attributes import Dimension


@dataclass
class ImageBoxTheme:
    keep_proportion: bool = field(default_factory=lambda: False)
    dimension: Dimension = field(default_factory=lambda: Dimension(
        width=50,
        height=50
    ))
