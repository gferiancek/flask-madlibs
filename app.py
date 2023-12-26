from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_list

app = Flask(__name__)
app.config["SECRET_KEY"] = "madlibs"
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """Homepage that allows user to select Madlib Story"""

    return render_template("index.html", stories=story_list)


@app.route("/<story_id>", methods=["GET", "POST"])
def render_story(story_id):
    """GET request that renders form for building a Madlib Story"""

    story = next(story for story in story_list if story.id == story_id)

    if request.method == "GET":
        return render_template("story_builder.html", story=story)

    if request.method == "POST":
        user_words = {}

        for i in range(1, len(story.prompts)):
            user_words[story.prompts[i-1]] = request.form[f"prompt-{i}"]

        story_text = story.generate(user_words)
        return render_template(
            "story.html", id=story.id, title=story.title, text=story_text
        )
