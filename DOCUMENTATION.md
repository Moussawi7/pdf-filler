# PDFFiller Comprehensive Documentation

PDFFiller is a Python library designed to streamline the process of filling PDF templates with dynamic content. It offers a versatile and user-friendly interface for customizing and generating PDF documents.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Functions](#functions)
4. [Components](#components)
    1. [TextField](#textfield)
    2. [CheckMark](#checkmark)
    3. [ImageBox](#imagebox)
5. [Theme](#theme)
6. [Attributes](#attributes)
7. [Exceptions](#exceptions)

## Installation

```bash
pip install PDFFiller
```

## Quick Start

If you prefer exploring usage through examples, please refer to the examples folder.

```python
from PDFFiller import PDFFiller, Template
from PDFFiller.theme import Theme
from PDFFiller.components import TextField, TextFieldTheme, CheckMark, DebugBoxTheme, CheckMarkTheme, ImageBox, \
    ImageBoxTheme
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
```

## Functions

### Build

This function builds the template based on the source, theme, and fields provided by the theme as a template.

```python
build(template)
```

### Export

This function exports the built template as a PDF file, taking the destination as a parameter.

```python
export(destination)
```

**Note:** You can build again after the export; each export includes all built templates unless reset or done are triggered.

### Reset

This function clears the cached templates.

```python
reset()
```

### Done

This function returns all built templates as bytes and `None` in case of None.

```python
done()
```

## Components

### TextField

The TextField component is used to display text inside the document.

```python
class TextField:
    key: str  # used in debug mode
    value: str  # the value that will be displayed
    position: Position  # the position of the field, check the attributes below
    font: Optional[Font] = None  # the font details, usually inherited from the theme
```

### CheckMark

The CheckMark component is used to display a checkmark inside the document.

```python
class CheckMark:
    key: str  # used in debug mode
    checked: bool  # mark the field as checked or not
    position: Position  # the position of the field, check the attributes below
    symbol: Optional[str] = None  # It is an 'X' by default
    font: Optional[Font] = None  # the font details, usually inherited from the theme
```

### ImageBox

The ImageBox component is used to display an image inside the document.

```python
class ImageBox:
    key: str  # used in debug mode
    path: str  # the path of the image
    position: Position  # the position of the field, check the attributes below
    keep_proportion: bool  # in order to make the image proportional or not to the box size
```

## Theme

The Theme is used to set global configuration for the document, especially font and dimension.

```python
class Theme:
    debug_box: Optional[DebugBoxTheme]
    text_field: Optional[TextFieldTheme]
    check_mark: Optional[CheckMarkTheme]
    image_box: Optional[ImageBoxTheme]
```

## Attributes

### Color

```python
class Color:
    red: int
    green: int
    blue: int
```

### Font

```python
class Font:
    family: str
    color: Color
    size: int
```

### Position

```python
class Position:
    page: int
    x: int
    y: int
    width: int
    height: int
```

## Exceptions

### UnableToBuild

This exception is thrown in case the PDF file could not be built under any condition, such as inaccessibility or a broken document.

### UnableToExport

This exception is thrown if the PDF could not be exported, usually due to insufficient permissions.

### NothingToExport

This exception is thrown if no template is built.