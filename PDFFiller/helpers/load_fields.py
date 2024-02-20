import yaml

from ..components import TextField, CheckMark, ImageBox, SigningArea
from ..attributes import Font, Color, Position, Dimension


def load_fields(path):
    fields = []
    with open(path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
        for text_field in data_loaded.get("text_fields", []):
            dimension = text_field.get("dimension")
            font = text_field.get("font")
            field = TextField(
                key=text_field.get("key"),
                value=text_field.get("value"),
                position=Position(**text_field.get("position"))
            )
            if dimension:
                field.dimension = Dimension(**dimension)
            if font:
                field.font = Font(
                    color=Color(**font.get("color")),
                    size=font.get("size"),
                    family=font.get("family")
                )
            fields.append(field)
        for check_mark in data_loaded.get("check_marks", []):
            dimension = check_mark.get("dimension")
            font = check_mark.get("font")
            checked = check_mark.get("checked")
            field = CheckMark(
                key=check_mark.get("key"),
                symbol=check_mark.get("symbol"),
                position=Position(**check_mark.get("position"))
            )
            if dimension:
                field.dimension = Dimension(**dimension)
            if font:
                field.font = Font(
                    color=Color(**font.get("color")),
                    size=font.get("size"),
                    family=font.get("family")
                )
            if checked:
                field.checked = checked
            fields.append(field)

        for image_box in data_loaded.get("image_boxes", []):
            dimension = image_box.get("dimension")
            field = ImageBox(
                key=image_box.get("key"),
                path=image_box.get("path"),
                keep_proportion=image_box.get("keep_proportion"),
                position=Position(**image_box.get("position"))
            )
            if dimension:
                field.dimension = Dimension(**dimension)
            fields.append(field)

        for image_box in data_loaded.get("signing_areas", []):
            dimension = image_box.get("dimension")
            field = SigningArea(
                key=image_box.get("key"),
                path=image_box.get("path"),
                position=Position(**image_box.get("position"))
            )
            if dimension:
                field.dimension = Dimension(**dimension)
            fields.append(field)

    return fields
