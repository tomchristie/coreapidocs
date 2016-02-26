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
    now = datetime.datetime.now()
    docs = Docs("document.json")
    return render_template('home.html', date=now, docs=docs.get_docs())


if __name__ == '__main__':
    app.debug = True
    app.run()
