import datetime
from flask import Flask
from flask import render_template
from docs import Docs

app = Flask(__name__)

# ToDo:
# Flask
# & serve static
# Takes a document (file/url)
# 1 View that renders the document


@app.route('/')
def docs():
    """
    Generate the coreapi-docs and serve them to roor.
    """
    docs = Docs("document.json")
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
