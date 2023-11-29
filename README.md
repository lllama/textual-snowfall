# textual-snowfall

[![PyPI - Version](https://img.shields.io/pypi/v/textual-snowfall.svg)](https://pypi.org/project/textual-snowfall)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textual-snowfall.svg)](https://pypi.org/project/textual-snowfall)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install textual-snowfall
```

## License

`textual-snowfall` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Usage

Textual-snowfall is a [Textual](https://textual.textualize.io) container widget that'll add snow to your app. Use it as you would use a normal container, or use it as a mixin with other container classes.

For example:

```py
from textual.app import App
from textual.containers import ScrollableContainer

from textual_snowfall.widgets import Snowfall

class SnowScroll(ScrollableContainer, Snowfall):
    pass

class MyApp(App):
    def compose(self):
        yield SnowScroll()
```
