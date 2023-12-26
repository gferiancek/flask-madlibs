from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_list

app = Flask(__name__)
app.config["SECRET_KEY"] = "madlibs"
debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Homepage that allows user to select Madlib Story"""

    return render_template('index.html', stories=story_list)