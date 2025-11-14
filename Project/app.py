import os
import sqlite3
from functools import wraps

from flask import(
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for,
    flash,
)

from werkzeug.security import generate_password_hash, check_password_hash
from Scenes import SCENES
app = Flask(__name__)
app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY", "dev-change-this")

DB_PATH = ".db"

# Helpers
def get_db():
    "SQLite connection"
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory=sqlite3.Row
    return connection

def init_db():
    "User table"
    connection = get_db()
    create =connection.cursor()
    create.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            hash TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()
    
@app.route("/game", methods=["GET", "POST"])
@login_required
def game():
    if "scene" not in session:
        session["scene"] = "start"

    current_key = session["scene"]
    scene = SCENES[current_key]

    if request.method == "POST":
        if request.form.get("restart"):
            session["scene"]="start"
            return redirect(url_for("game"))
        
        choice_label = request.form.get("choice")
        if choice_label and choice_label in scene["choices"]:
            next_key = scene["choices"][choice_label]
            session["scene"]=next_key
            return redirect(url_for("game"))
        else:
            flash("404 error")
        
    return render_template("game.html", scene_key=current_key,scene=scene)

