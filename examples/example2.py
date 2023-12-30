from pdffiller import PDFFiller, Template
from pdffiller.theme import Theme
from pdffiller.components import TextField, TextFieldTheme, CheckMark, DebugBoxTheme, CheckMarkTheme, ImageBox, \
    ImageBoxTheme
from pdffiller.attributes import Font, Color, Position
from pdffiller.exceptions import NothingToExport, UnableToBuild, UnableToExport
from pdffiller.helpers.performance_decorator import performance_analysis

theme = Theme(
    text_field=TextFieldTheme(
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=11
        )
    ),
    image_box=ImageBoxTheme(
        keep_proportion=False
    ),
    check_mark=CheckMarkTheme(
        symbol="×",
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=11
        )
    ),
    debug_box=DebugBoxTheme(
        text_color=Color(255, 0, 0),
        border_color=Color(0, 255, 0),
        background_color=Color(0, 255, 0),
        border_thickness=1
    )
)

fields = [
    TextField(
        key="text_first_name",
        value="Ali Moussawi",
        position=Position(
            page=0,
            x=330,
            y=415,
            width=100,
            height=21,
        ),
        font=Font(
            family="Helvetica",
            color=Color(256, 0, 0),
            size=12
        )
    ),
    CheckMark(
        key="gender",
        checked=True,
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=8
        ),
        position=Position(
            page=0,
            x=24,
            y=418,
            width=15,
            height=15,
        ),
    ),
    ImageBox(
        key="profile",
        path="./examples/files/sample.jpg",
        keep_proportion=False,
        position=Position(
            page=0,
            x=0,
            y=0,
            width=100,
            height=200,
        ),
    )
]

template1 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
)

template2 = Template(
    source="./examples/files/sample2.pdf",
    theme=theme,
    fields=fields,
)


@performance_analysis
def generate_document():
    pdf_filler = PDFFiller(debug=False)
    try:
        # query = pdf_filler.build(template1)
        # for i in range(0, 100):
        #     query = query.build(template1)
        #
        # result = query.export(destination="./documents/export1.pdf").done()
        result = (
            pdf_filler
            .build(template1)
            .build(template2)
            .export(destination="./examples/build/export.pdf")
            .build(template2)
            .export(destination="./examples/build/export1.pdf")
            .reset()
            .build(template2)
            .done()
        )
        print(result)
    except NothingToExport as e:
        print("nothing to export", e.code)
    except UnableToBuild as e:
        print("unable to build", e.code, e.exception)
    except UnableToExport as e:
        print("unable to export", e.code, e.exception)


generate_document()