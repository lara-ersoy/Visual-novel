from .db import SessionLocal
from .models import Scene 

def seed_if_empty():
    with SessionLocal() as s:
        if s.query(Scene).count() == 0:
            s.add(Scene(
                slug = "Once there was a powerful mercenary. For coin, she would use her weapon in any situation.",
                title = "Mercenary X",
                script={
                    "background": "Princess.PNG",
                    "dialogue": [
                        {"speaker": "Mercenary", "line": "Recently, a got a very interesting request from the Kingdom of Hearts."},
                        {"speaker": "Mercenary", "line": "I am expecting to accept this request, but this might be a dangerous one."}
                    ]
                }
            ))
            s.commit()