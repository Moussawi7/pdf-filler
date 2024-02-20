

class SigningAreaBuilder:

    def __init__(self):
        pass

    def build(self, pdf_page, element):
        if element.path is None:
            return
        shape_rect = (element.position.x,
                      element.position.y,
                      element.position.x + element.dimension.width,
                      element.position.y + element.dimension.height)

        pdf_page.insert_image(
            rect=shape_rect,
            filename=element.path,
            height=element.dimension.height,
            width=element.dimension.width,
            keep_proportion=True
        )
