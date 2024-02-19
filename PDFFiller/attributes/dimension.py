from dataclasses import dataclass
from typing import Optional


@dataclass
class Dimension:
    width: Optional[int] = None
    height: Optional[int] = None

