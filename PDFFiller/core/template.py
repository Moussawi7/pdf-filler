from dataclasses import dataclass, field
from typing import Union, Optional

from PDFFiller.theme.theme import Theme


@dataclass
class Template:
    source: Union[str, bytes]
    theme: Optional[Theme]
    fields: list
    values: Optional[list] = field(default_factory=lambda: [])
