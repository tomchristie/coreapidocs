import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

# ToDo:
# Flask
# & serve static
# Takes a document (file/url)
# 1 View that renders the document


@app.route('/')
def docs():
    now = datetime.datetime.now()
    return render_template('coreapi_docs/templates/home.html', date=now)


if __name__ == '__main__':
    app.debug = True
    app.run()
