coreapidocs [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]
===
Document APIs with CoreAPI.

### Prerequisites

  - Python (2.7, 3.3, 3.4, 3.5)
  - Core API ([Read More](http://www.coreapi.org/))


### Installation
You can install `coreapidocs` through pypi.

    pip install coreapidocs


### Usage
You will have to pass a `.json` document to initialize the docs.

```python
from coreapidocs.docs import Docs

try:
    schema = open(filename, 'rb').read()
    docs = Docs(schema)
except (IOError, OSError):
    abort(400, {"msg": "No such file or directory - %s" % filename})
```

Then you can simply pass the `docs` variable to your template (ie. Flask):

```python
return render_template('home.html', docs=docs.get_docs())
```

For more information view the source of [example.py](coreapidocs/example.py).


### Development
Create the virtualenv and install the requirements.

    virtualenv env
    source env/bin/activate

    pip install -r requirements.txt


You will need to pass an argument ie. `document.json`.

    python coreapidocs/example.py document.json
    # Then go to: http://127.0.0.1:5000/


### Tests
In order to run the tests you will have to run:

    python runtests.py


[travis-image]: https://travis-ci.org/ekonstantinidis/coreapidocs.svg
[travis-url]: https://travis-ci.org/ekonstantinidis/coreapidocs

[pypi-image]: https://badge.fury.io/py/coreapidocs.svg
[pypi-url]: https://pypi.python.org/pypi/coreapidocs/
