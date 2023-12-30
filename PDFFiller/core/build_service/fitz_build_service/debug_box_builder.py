from PDFFiller.helpers import FitzHelper


class DebugBoxBuilder:

    def __init__(self):
        self.fitz_helper = FitzHelper()

    def build(self, pdf_page, element):
        shape = pdf_page.new_shape()
        shape_rect = (element.position.x,
                      element.position.y,
                      element.position.x + element.position.width,
                      element.position.y + element.position.height)
        shape.draw_rect(shape_rect)

        color = self.fitz_helper.convert_to_fitz_color(element.text_color)
        shape.insert_textbox(
            rect=shape_rect,
            buffer=element.key,
            fontsize=element.text_size,
            color=color
        )

        shape.finish(
            width=element.border_thickness,
            color=self.fitz_helper.convert_to_fitz_color(element.border_color),
            fill=self.fitz_helper.convert_to_fitz_color(element.background_color),
        )
        shape.commit()
