from dataclasses import dataclass, field
from typing import Optional

from PDFFiller.theme.theme import Theme


@dataclass
class Template:
    source: str
    theme: Optional[Theme]
    fields: list
    values: Optional[list] = field(default_factory=lambda: [])
