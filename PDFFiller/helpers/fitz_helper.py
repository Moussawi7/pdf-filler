import copy
from dataclasses import fields, is_dataclass


class FitzHelper:

    def inherit_attributes(self, source, destination):

        element = copy.deepcopy(destination)
        def _inherit_attributes(source, destination):
            if not is_dataclass(source) or not is_dataclass(destination):
                return
            for field in fields(source):
                if not getattr(destination, field.name, None):
                    setattr(destination, field.name, getattr(source, field.name))
                elif isinstance(getattr(destination, field.name), type(getattr(source, field.name))):
                    _inherit_attributes(getattr(source, field.name), getattr(destination, field.name))
            return destination

        return _inherit_attributes(source, element)

    def convert_to_fitz_color(self, rgb_color):
        color = (
            rgb_color.red / 256,
            rgb_color.green / 256,
            rgb_color.blue / 256
        )
        return color
