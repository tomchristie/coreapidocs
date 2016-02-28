import sys
from flask import Flask, render_template, abort
from docs import Docs

app = Flask(__name__)


@app.route('/')
def docs():
    """
    Generate the coreapi-docs and serve them to roor.
    Accepts one parameter with a filename (ie. document.json)
    """

    if len(sys.argv) != 2:
        abort(400, {"msg": "Missing file parameter ie. document.json"})

    filename = sys.argv[-1]

    try:
        schema = open(filename, 'r').read()
        docs = Docs(schema)
    except (IOError, OSError):
        abort(400, {"msg": "No such file or directory - %s" % filename})

    return render_template('home.html', docs=docs.get_docs())


@app.route('/<path:path>')
def static_proxy(path):
    """
    Serve static files.
    "send_static_file" will guess the correct MIME type
    """
    return app.send_static_file(path)


if __name__ == '__main__':
    app.debug = True
    app.run()
