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


@app.route('/<story_id>')
def render_story_builder(story_id):
    """GET request that renders form for building a Madlib Story"""

    story = next(story for story in story_list if story.id == story_id)
    return render_template('story_builder.html', story=story)