from dataclasses import dataclass, field


@dataclass
class ImageBoxTheme:
    keep_proportion: bool = field(default_factory=lambda: True)
