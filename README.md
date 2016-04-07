coreapidocs [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]
===
Document APIs with CoreAPI.

### Prerequisites

  - Python (2.7, 3.3, 3.4, 3.5)
  - Core API ([Read More](http://www.coreapi.org/))


### Installation
You can install `coreapidocs` through pypi.

    pip install coreapidocs


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
