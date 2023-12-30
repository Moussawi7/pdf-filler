import copy
from dataclasses import fields


class FitzHelper:

    def inherit_attributes(self, source, destination):
        element = copy.copy(destination)
        for field in fields(source):
            if not getattr(element, field.name, None):
                setattr(element, field.name, getattr(source, field.name))
        return element

    def convert_to_fitz_color(self, rgb_color):
        color = (
            rgb_color.red / 256,
            rgb_color.green / 256,
            rgb_color.blue / 256
        )
        return color
