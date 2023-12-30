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
```python
from PDFFiller import PDFFiller, Template
from PDFFiller.theme import Theme
from PDFFiller.components import TextField, CheckMark, TextFieldTheme
from PDFFiller.attributes import Font, Color, Position

theme = Theme(
    text_field=TextFieldTheme(
        font=Font(
            family="Helvetica",
            color=Color(0, 0, 0),
            size=11
        )
    )
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
    CheckMark(
        key="activity",
        checked=True,
        position=Position(
            page=0,
            x=50,
            y=332,
            width=20,
            height=20,
        ),

]

template1 = Template(
    source="./examples/files/sample1.pdf",
    theme=theme,
    fields=fields,
)

pdf_filler = PDFFiller()
result = (
    pdf_filler
    .build(template1)
    .export(destination="./examples/build/export1.pdf")
    .done()
)
```

## Contributing

We welcome contributions! If you'd like to enhance PDFFiller or report issues, please check out our [contribution guidelines](CONTRIBUTING.md).


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.