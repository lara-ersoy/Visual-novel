# Import in packages
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

# Import scenes 
from Scenes import SCENES

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-change-this")

DB_PATH = "adventure.db"

# Helpers
def get_db():
    "SQLite connection"
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    "User table"
    connection = get_db()
    create = connection.cursor()
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

def get_user_by_username(username):
    connection = get_db()
    create = connection.cursor()
    create.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = create.fetchone()
    connection.close()
    return row 

def insert_user(username, password_hash):
    connection = get_db()
    create = connection.cursor()
    create.execute("INSERT INTO users (username, hash) VALUES (?,?)",
                   (username, password_hash),
    )
    connection.commit()
    connection.close()

# Login

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route("/")
def index():
    if session.get("user_id") is None:
        return redirect(url_for("login"))
    return redirect(url_for("game"))


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Vul gebruikersnaam en wachtwoord in.")
            return render_template("login.html")

        user = get_user_by_username(username)
        if user is None or not check_password_hash(user["hash"], password):
            flash("Ongeldige gebruikersnaam en/of wachtwoord.")
            return render_template("login.html")

        session["user_id"] = user["id"]
        session.setdefault("scene", "start")
        return redirect(url_for("game"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirmation = request.form.get("confirmation", "")

        if not username or not password or not confirmation:
            flash("Vul alle velden in.")
            return render_template("register.html")
        
        if password != confirmation:
            flash("Wachtworden komen niet overheen.")
            return render_template("register.html")
        
        if password != confirmation:
            flash("Wachtworden komen niet overheen.")
            return render_template("register.html")
        
        if get_user_by_username(username) is not None:
            flash("Gebruikersnaam bestaat al")
            return render_template("register.html")
        
        pwd_hash = generate_password_hash(password) 
        insert_user(username, pwd_hash)

        flash("Account aangemaakt. Log nu in.")
        return redirect("/login")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

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

if __name__ == "__main__":
    init_db()
    app.run(debug=True)