coreapi-docs [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]
===
Document APIs with CoreAPI.

### Prerequisites

  - Python (2.7, 3.3, 3.4, 3.5)
  - Core API ([Read More](http://www.coreapi.org/))


### Installation
You can install `coreapi-docs` through pypi.

    pip install coreapi-docs


### Development

    virtualenv env
    source env/bin/activate

    pip install -r requirements.txt

    python coreapi_docs/example.py
    # Then go to: http://127.0.0.1:5000/


### Tests
In order to run the tests you will have to run:

    python runtests.py


[travis-image]: https://travis-ci.com/ekonstantinidis/coreapi-docs.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master
[travis-url]: https://travis-ci.com/ekonstantinidis/coreapi-docs

[pypi-image]: https://badge.fury.io/py/coreapi-docs.svg
[pypi-url]: https://pypi.python.org/pypi/coreapi-docs/
