from dataclasses import dataclass
from typing import Optional

from pdffiller.theme.theme import Theme


@dataclass
class Template:
    source: str
    theme: Optional[Theme]
    fields: list
