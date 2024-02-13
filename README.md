# Introduction

Welcome to PDFFiller, a Python library built on top of [PyMuPDF](https://github.com/pymupdf/PyMuPDF) designed to streamline the process of programmatically filling PDF documents with text, checkmarks, and images. With PDFFiller, developers can easily manipulate one or multiple pages, offering the flexibility to export the filled PDF document as a file or as bytes.

**Note: This Library is Under Active Development**

This library is currently in an early stage of development and may undergo significant changes. It is not recommended for production use at this time. Expect frequent updates and improvements as we work towards stabilizing the codebase. Your feedback and contributions are highly valued during this development phase.

Please be cautious when integrating this library into production projects, and consider revisiting the documentation for updates and changes. We appreciate your understanding and patience as we work towards a stable release.

If you encounter issues or have suggestions, feel free to open an issue or contribute to the development. Thank you for your interest in PDFFiller!


## Key Features

- **Text, Check Marks, and Image Insertion:** Effortlessly insert text, checkmarks, and images into PDF documents.

- **Multi-Page Support:** Seamlessly handle one or multiple pages within a PDF for comprehensive document manipulation.

- **Export Options:** Choose between exporting the filled PDF document as a file or as bytes, providing flexibility for various use cases.

```bash
pip install PDFFiller
```

## Usage
You can find the full documentation [here](DOCUMENTATION.md)

#### Simple
```python
# simple example

from PDFFiller import PDFFiller, Template
from PDFFiller.theme import Theme
from PDFFiller.components import TextField, TextFieldTheme, CheckMark, CheckMarkTheme
from PDFFiller.attributes import Font, Color, Position, Dimension
from PDFFiller.exceptions import NothingToExport, UnableToBuild, UnableToExport

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
        ),
        dimension=Dimension(
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
        ),
        dimension=Dimension(
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
        ),
        dimension=Dimension(
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
        ),
        dimension=Dimension(
            width=20,
            height=20,
        )
    ),
    CheckMark(
        key="activity_2",
        checked=True,
        position=Position(
            page=0,
            x=50,
            y=487,
        ),
        dimension=Dimension(
            width=20,
            height=20,
        )
    ),
]

template1 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
)

def generate_document():
    pdf_filler = PDFFiller(debug=False)
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
```


#### Template
```python
# yaml example
from PDFFiller import PDFFiller, Template
from PDFFiller.components import TextFieldValue, CheckMarkValue, ImageBoxValue
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
    pdf_filler = PDFFiller(debug=True)
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
```

## Contributing

We welcome contributions! If you'd like to enhance PDFFiller or report issues, please check out our [contribution guidelines](CONTRIBUTING.md).


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.