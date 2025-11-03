from flask import Flask, jsonify
from .db import init_db

def create_app():
    app =  Flask(__name__)
    init_db()

    @app.route("/")
    def home():
        return jsonify({"message": "Visual novel!"})
    
    # First scene with background included
    @app.route("/api/scene")
    def get_scene():
        scene_data = {
            "title": "Once there was a powerful mercenary. For coin, she would use her sword in any situation.",
            "background": "Princess.PNG",
            "dialogue": [
                {"speaker": "Mercenary", "line": "Recently, a got a very interesting request from the Kingdom of Hearts."},
                {}
            }
        }
        
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True, port = 5000)