from fitz import TEXT_ALIGN_CENTER
from PDFFiller.helpers import FitzHelper


class CheckMarkBuilder:

    def __init__(self):
        self.fitz_helper = FitzHelper()

    def build(self, pdf_page, element):
        shape_rect = (element.position.x,
                      element.position.y,
                      element.position.x + element.position.width,
                      element.position.y + element.position.height)

        color = self.fitz_helper.convert_to_fitz_color(element.font.color)
        pdf_page.insert_textbox(
            rect=shape_rect,
            buffer=element.symbol if element.checked else '',
            fontname=element.font.family,
            fontsize=element.font.size,
            align=TEXT_ALIGN_CENTER,
            color=color
        )
