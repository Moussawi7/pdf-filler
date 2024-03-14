import io
import fitz

from PDFFiller.components import CheckMark, TextField, ImageBox, DebugBox, SigningArea
from PDFFiller.helpers import FitzHelper

from .text_field_builder import TextFieldBuilder
from .check_mark_builder import CheckMarkBuilder
from .debug_box_builder import DebugBoxBuilder
from .image_box_builder import ImageBoxBuilder
from .signing_area_builder import SigningAreaBuilder


class FitzBuildService:

    def __init__(self, debug=False):
        self.debug = debug
        self.fitz_helper = FitzHelper()
        self.text_field_builder = TextFieldBuilder()
        self.check_mark_builder = CheckMarkBuilder()
        self.image_box_builder = ImageBoxBuilder()
        self.signing_area_builder = SigningAreaBuilder()
        self.debug_box_builder = DebugBoxBuilder()

    def _build_debug_box(self, pdf_page, field, debug_box_template):
        element = self.fitz_helper.inherit_attributes(
            debug_box_template,
            DebugBox(
                key=field.key,
                position=field.position,
                dimension=field.dimension
            )
        )
        self.debug_box_builder.build(pdf_page, element)

    def _save_to_stream(self, pdf_document):
        pdf_stream = io.BytesIO()
        pdf_document.save(pdf_stream)
        pdf_document.close()
        return pdf_stream.getvalue()

    def _fill_fields_with_values(self, fields, values):
        for field in fields:
            for value in values:
                if field.key == value.key:
                    field.__dict__.update(value.__dict__)
        return fields

    def _build_text_field(self, pdf_page, template, field):
        element = self.fitz_helper.inherit_attributes(
            template.theme.text_field,
            field
        )
        if self.debug:
            self._build_debug_box(pdf_page, element, template.theme.debug_box)
            return
        self.text_field_builder.build(pdf_page, element)

    def _build_check_mark(self, pdf_page, template, field):
        element = self.fitz_helper.inherit_attributes(
            template.theme.check_mark,
            field
        )
        if self.debug:
            self._build_debug_box(pdf_page, element, template.theme.debug_box)
            return
        self.check_mark_builder.build(pdf_page, element)

    def _build_image_box(self, pdf_page, template, field):
        element = self.fitz_helper.inherit_attributes(
            template.theme.image_box,
            field
        )
        if self.debug:
            self._build_debug_box(pdf_page, element, template.theme.debug_box)
            return
        self.image_box_builder.build(pdf_page, element)

    def _build_signing_area(self, pdf_page, template, field):
        element = self.fitz_helper.inherit_attributes(
            template.theme.signing_area,
            field
        )
        if self.debug:
            self._build_debug_box(pdf_page, element, template.theme.debug_box)
            return
        self.signing_area_builder.build(pdf_page, element)

    def _read_pdf_document(self, source):
        if type(source) == bytes:
            return fitz.open(stream=source)
        return fitz.open(source)

    def build(self, template):
        pdf_document = self._read_pdf_document(template.source)
        fields = self._fill_fields_with_values(template.fields, template.values)
        for field in fields:
            pdf_page = pdf_document[field.position.page]
            if type(field) == TextField:
                self._build_text_field(pdf_page, template, field)
            elif type(field) == CheckMark:
                self._build_check_mark(pdf_page, template, field)
            elif type(field) == ImageBox:
                self._build_image_box(pdf_page, template, field)
            elif type(field) == SigningArea:
                self._build_signing_area(pdf_page, template, field)
            else:
                raise NotImplementedError

        pdf_stream = self._save_to_stream(pdf_document)
        return pdf_stream
