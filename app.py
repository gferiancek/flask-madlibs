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
        ui_prompts = [prompt.replace("_", " ") for prompt in story.prompts]
        return render_template(
            "story_builder.html", title=story.title, prompts=ui_prompts, id=story.id
        )

    if request.method == "POST":
        user_words = {}

        for i in range(0, len(story.prompts)):
            key = story.prompts[i]
            print(key, i)
            user_words[key] = user_words.get(key, []) + [request.form[f"prompt-{i+1}"]]

        story_text = story.generate(user_words)
        return render_template(
            "story.html", id=story.id, title=story.title, text=story_text
        )
