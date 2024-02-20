# yaml example
from PDFFiller import PDFFiller, Template
from PDFFiller.components import TextFieldValue, CheckMarkValue, ImageBoxValue, SigningAreaValue
from PDFFiller.helpers import load_theme, load_fields
from PDFFiller.exceptions import NothingToExport, UnableToBuild, UnableToExport
from PDFFiller.helpers.performance_decorator import performance_analysis

theme = load_theme("./examples/theme.yml")
fields = load_fields("./examples/fields.yml")

values = [
    TextFieldValue(
        key="text_first_name",
        value="Ali Moussawi"
    ),
    CheckMarkValue(
        key="chk_gender",
        checked=False
    ),
    ImageBoxValue(
        key="img_logo",
        path="./examples/files/sample.jpg"
    ),
    SigningAreaValue(
        key="signing_area_1",
        path="./examples/files/sample.jpg"
    )
]

template1 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
    values=values
)


template2 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
)


@performance_analysis
def generate_document():
    pdf_filler = PDFFiller(debug=False)
    try:
        result = (
            pdf_filler
            .build(template1)
            .build(template2)
            .export(destination="./examples/build/export1.pdf")
            .done()
        )
        print(result)
    except NothingToExport as e:
        print(e.code)
        raise e
    except UnableToBuild as e:
        print(e.code, e.exception)
        raise e
    except UnableToExport as e:
        print(e.code, e.exception)
        raise e


generate_document()