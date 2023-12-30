from PDFFiller.helpers import FitzHelper


class TextFieldBuilder:

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
            buffer=element.value,
            fontname=element.font.family,
            fontsize=element.font.size,
            color=color
        )
