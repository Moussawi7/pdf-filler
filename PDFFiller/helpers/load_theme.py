import yaml

from ..components import TextFieldTheme, CheckMarkTheme, ImageBoxTheme, SigningAreaTheme, DebugBoxTheme
from ..attributes import Font, Color, Dimension
from ..theme import Theme


def load_theme(path):
    with open(path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
        theme = Theme(
            version=data_loaded.get("version")
        )
        text_field = data_loaded.get("text_field")
        if text_field is not None:
            font = text_field.get("font")
            dimension = text_field.get("dimension")
            theme.text_field = TextFieldTheme(
                font=Font(
                    color=Color(**font.get("color")),
                    size=font.get("size"),
                    family=font.get("family")
                ),
                dimension=Dimension(
                    width=dimension.get("width"),
                    height=dimension.get("height")
                )
            )
        check_mark = data_loaded.get("check_mark")
        if check_mark is not None:
            font = check_mark.get("font")
            theme.check_mark = CheckMarkTheme(
                symbol=check_mark.get("symbol"),
                font=Font(
                    color=Color(**font.get("color")),
                    size=font.get("size"),
                    family=font.get("family")
                )
            )
        image_box = data_loaded.get("image_box")
        if image_box is not None:
            theme.image_box = ImageBoxTheme(
                keep_proportion=image_box.get("keep_proportion"),
                dimension=Dimension(**image_box.get("dimension")),
            )
        signing_area = data_loaded.get("signing_area")
        if signing_area is not None:
            theme.image_box = SigningAreaTheme(
                dimension=Dimension(**signing_area.get("dimension")),
            )
        debug_box = data_loaded.get("debug_box")
        if debug_box is not None:
            font = debug_box.get("font")
            theme.debug_box = DebugBoxTheme(
                font=Font(
                    color=Color(**font.get("color")),
                    size=font.get("size"),
                    family=font.get("family")
                ),
                background_color=Color(**debug_box.get("background_color")),
                border_thickness=debug_box.get("border_thickness"),
                border_color=Color(**debug_box.get("border_color")),
            )

        return theme
