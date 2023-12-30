import io
import fitz

from PDFFiller.components import CheckMark, TextField, ImageBox, DebugBox
from PDFFiller.helpers import FitzHelper

from .text_field_builder import TextFieldBuilder
from .check_mark_builder import CheckMarkBuilder
from .debug_box_builder import DebugBoxBuilder
from .image_box_builder import ImageBoxBuilder


class FitzBuildService:

    def __init__(self, debug=False):
        self.debug = debug
        self.fitz_helper = FitzHelper()
        self.text_field_builder = TextFieldBuilder()
        self.check_mark_builder = CheckMarkBuilder()
        self.image_box_builder = ImageBoxBuilder()
        self.debug_box_builder = DebugBoxBuilder()

    def _build_debug_box(self, pdf_page, field, debug_box_template):
        element = self.fitz_helper.inherit_attributes(
            debug_box_template,
            DebugBox(
                key=field.key,
                position=field.position
            )
        )
        self.debug_box_builder.build(pdf_page, element)

    def _save_to_stream(self, pdf_document):
        pdf_stream = io.BytesIO()
        pdf_document.save(pdf_stream)
        pdf_document.close()
        return pdf_stream.getvalue()

    def build(self, template):
        pdf_document = fitz.open(template.source)
        for field in template.fields:
            pdf_page = pdf_document[field.position.page]
            if self.debug:
                self._build_debug_box(pdf_page, field, template.theme.debug_box)
                continue

            if type(field) == TextField:
                element = self.fitz_helper.inherit_attributes(
                    template.theme.text_field,
                    field
                )
                self.text_field_builder.build(pdf_page, element)
            elif type(field) == CheckMark:
                element = self.fitz_helper.inherit_attributes(
                    template.theme.check_mark,
                    field
                )
                self.check_mark_builder.build(pdf_page, element)
            elif type(field) == ImageBox:
                element = self.fitz_helper.inherit_attributes(
                    template.theme.image_box,
                    field
                )
                self.image_box_builder.build(pdf_page, element)
            else:
                raise NotImplementedError

        pdf_stream = self._save_to_stream(pdf_document)
        return pdf_stream
