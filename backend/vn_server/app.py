from flask import Flask, jsonify, send_from_directory, abort
from .db import init_db, SessionLocal
from .models import Scene
from .seed import seed_if_empty
import os

def create_app():
    app =  Flask(__name__)
    init_db()
    seed_if_empty() # Only if empty

    @app.route("/")
    def home():
        return jsonify({"message": "Visual novel!"})
    
    @app.get("/health")
    def health():
        return jsonify({"ok": True})
    
    # First scene with background included
    @app.route("/api/scene/<slug>")
    def get_scene(slug):
        with SessionLocal() as s:
            row = s.query(Scene).filter_by(slug=slug).first()
            if not row:
                abort(404, f"Scene '{slug} not found")
            return jsonify({
                "slug": row.slug,
                "title": row.title,
                "script": row.script
            })
        
    @app.get("/api/assets")
    def assets():
        static_dir = os.path.join(app.root_path, "../static")
        try: 
            files = sorted(f for f in os.listdir(static_dir) if os.path.isfile(os.path.join(static_dir, f)))
        except FileNotFoundError:
            files = []
        return jsonify({
            "static_base": "/static/",
            "files": files
        })
        
    @app.route("/static/<path:filename>")
    def serve_static(filename):
        return send_from_directory(os.path.join(app.root_path, "../static"), filename)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True, port = 5000)