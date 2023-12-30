

class ImageBoxBuilder:

    def __init__(self):
        pass

    def build(self, pdf_page, element):
        shape_rect = (element.position.x,
                      element.position.y,
                      element.position.x + element.position.width,
                      element.position.y + element.position.height)

        pdf_page.insert_image(
            rect=shape_rect,
            filename=element.path,
            height=element.position.height,
            width=element.position.width,
            keep_proportion=element.keep_proportion
        )
