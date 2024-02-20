from dataclasses import dataclass, field
from typing import Optional

from PDFFiller.components import TextFieldTheme, DebugBoxTheme, CheckMarkTheme, ImageBoxTheme, SigningAreaTheme


@dataclass
class Theme:
    version: Optional = "1.0"
    debug_box: Optional[DebugBoxTheme] = field(default_factory=lambda: DebugBoxTheme())
    text_field: Optional[TextFieldTheme] = field(default_factory=lambda: TextFieldTheme())
    check_mark: Optional[CheckMarkTheme] = field(default_factory=lambda: CheckMarkTheme())
    image_box: Optional[ImageBoxTheme] = field(default_factory=lambda: ImageBoxTheme())
    signing_area: Optional[ImageBoxTheme] = field(default_factory=lambda: SigningAreaTheme())
