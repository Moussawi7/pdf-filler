# simple example

from pdffiller import PDFFiller, Template
from pdffiller.theme import Theme
from pdffiller.components import TextField, TextFieldTheme, CheckMark, CheckMarkTheme
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
    check_mark=CheckMarkTheme(
        symbol="X",
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=10
        )
    ),
)

fields = [
    TextField(
        key="text_first_name",
        value="Ali Moussawi",
        position=Position(
            page=0,
            x=130,
            y=155,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_date",
        value="29-12-2023",
        position=Position(
            page=0,
            x=450,
            y=155,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_address",
        value="Beirut - Lebanon",
        position=Position(
            page=0,
            x=130,
            y=172,
            width=100,
            height=21,
        )
    ),
    CheckMark(
        key="activity_1",
        checked=True,
        position=Position(
            page=0,
            x=50,
            y=332,
            width=20,
            height=20,
        ),
    ),
    CheckMark(
        key="activity_2",
        checked=True,
        position=Position(
            page=0,
            x=50,
            y=487,
            width=20,
            height=20,
        ),
    ),
]

template1 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
)


@performance_analysis
def generate_document():
    pdf_filler = PDFFiller(debug=True)
    try:
        result = (
            pdf_filler
            .build(template1)
            .export(destination="./examples/build/export1.pdf")
            .done()
        )
        print(result)
    except NothingToExport as e:
        print(e.code)
    except UnableToBuild as e:
        print(e.code, e.exception)
    except UnableToExport as e:
        print(e.code, e.exception)


generate_document()