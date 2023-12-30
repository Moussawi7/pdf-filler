# simple example

from PDFFiller import PDFFiller, Template
from PDFFiller.theme import Theme
from PDFFiller.components import TextField, TextFieldTheme, CheckMark, CheckMarkTheme
from PDFFiller.attributes import Font, Color, Position
from PDFFiller.exceptions import NothingToExport, UnableToBuild, UnableToExport
from PDFFiller.helpers.performance_decorator import performance_analysis

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

fields1 = [
    TextField(
        key="text_last_name",
        value="Moussawi",
        position=Position(
            page=0,
            x=200,
            y=185,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_first_name",
        value="Ali",
        position=Position(
            page=0,
            x=200,
            y=201,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_middle_name",
        value="Ibrahim",
        position=Position(
            page=0,
            x=200,
            y=215,
            width=100,
            height=21,
        )
    ),
    CheckMark(
        key="activity_2",
        checked=True,
        position=Position(
            page=0,
            x=195,
            y=233,
            width=20,
            height=20,
        ),
    ),
    TextField(
        key="text_date_of_birth",
        value="07/11/1988",
        position=Position(
            page=0,
            x=200,
            y=248,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_place_of_birth",
        value="Bekaa",
        position=Position(
            page=0,
            x=150,
            y=262,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_country_of_birth",
        value="Lebanon",
        position=Position(
            page=0,
            x=340,
            y=262,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_city_of_birth",
        value="Zahleh",
        position=Position(
            page=0,
            x=490,
            y=262,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_kuwait_residence",
        value="---",
        position=Position(
            page=0,
            x=170,
            y=318,
            width=100,
            height=21,
        )
    ),
    TextField(
        key="text_address_details",
        value="Moussawi building, First floor",
        position=Position(
            page=0,
            x=160,
            y=349,
            width=300,
            height=22,
        )
    ),
    TextField(
        key="text_address_country",
        value="Lebanon",
        position=Position(
            page=0,
            x=150,
            y=364,
            width=300,
            height=22,
        )
    ),
    TextField(
        key="text_address_country",
        value="Zahleh",
        position=Position(
            page=0,
            x=370,
            y=364,
            width=300,
            height=22,
        )
    ),
    TextField(
        key="text_declaration_name",
        value="Ali Moussawi",
        position=Position(
            page=1,
            x=130,
            y=502,
            width=300,
            height=22,
        ),
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=13
        )
    ),
    TextField(
        key="text_declaration_date",
        value="31/12/2023",
        position=Position(
            page=1,
            x=142,
            y=542,
            width=300,
            height=22,
        ),
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=13
        )
    ),
]

fields2 = [
    TextField(
        key="text_full_name",
        value="Ali Ibrahim Moussaoui",
        position=Position(
            page=0,
            x=230,
            y=148,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_civil_id_number",
        value="123456",
        position=Position(
            page=0,
            x=230,
            y=165,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_date_of_birth",
        value="11-07-1988",
        position=Position(
            page=0,
            x=230,
            y=183,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_resident_address",
        value="Moussawi building, First floor",
        position=Position(
            page=0,
            x=320,
            y=220,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_resident_city",
        value="Zahleh",
        position=Position(
            page=0,
            x=320,
            y=246,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_resident_country",
        value="Lebanon",
        position=Position(
            page=0,
            x=320,
            y=263,
            width=150,
            height=21,
        )
    ),
    CheckMark(
        key="text_us_person",
        checked=True,
        position=Position(
            page=0,
            x=220,
            y=400,
            width=20,
            height=20,
        ),
    ),
    TextField(
        key="text_declaration_name",
        value="Ali Moussawi",
        position=Position(
            page=0,
            x=50,
            y=655,
            width=150,
            height=21,
        )
    ),
    TextField(
        key="text_declaration_date",
        value="31/12/2023",
        position=Position(
            page=0,
            x=350,
            y=655,
            width=150,
            height=21,
        )
    ),
]

template1 = Template(
    source="./examples/files/CRS_Form_NBK_Capital_v2021.pdf",
    theme=theme,
    fields=fields1,
)


template2 = Template(
    source="./examples/files/FATCA_NBK_Capital_v2021.pdf",
    theme=theme,
    fields=fields2,
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
    except UnableToBuild as e:
        print(e.code, e.exception)
    except UnableToExport as e:
        print(e.code, e.exception)


generate_document()