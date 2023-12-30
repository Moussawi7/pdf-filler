from dataclasses import dataclass
from typing import Optional

from PDFFiller.theme.theme import Theme


@dataclass
class Template:
    source: str
    theme: Optional[Theme]
    fields: list
