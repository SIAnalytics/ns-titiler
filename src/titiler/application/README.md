## titiler.application

<img style="max-width:400px" src="https://user-images.githubusercontent.com/10407788/115224800-53d9d980-a0db-11eb-86c3-1c94fde3ed4a.png"/>
<p align="center">Titiler's demo application.</p>

## Installation

```bash
$ pip install -U pip

# From Pypi
$ pip install titiler.application

# Or from sources
$ git clone https://github.com/developmentseed/titiler.git
$ cd titiler && pip install -e titiler/application
```

Launch Application
```bash
$ pip install uvicorn
$ uvicorn titiler.application.main:app --reload
```

## Package structure

```
titiler/
 └── application/
    ├── tests/                   - Tests suite
    └── titiler/application/     - `application` namespace package
        ├── templates/
        |   ├── index.html       - demo landing page
        |   ├── cog_index.html   - demo viewer for `/cog`
        |   └── stac_index.html  - demo viewer for `/stac`
        ├── main.py              - Main FastAPI application
        └── settings.py          - demo settings (cache, cors...)
```
