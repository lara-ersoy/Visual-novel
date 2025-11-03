# Preserving the history

git mv server.py backend/vn_server/app.py
git mv client_pygame.py client/vn_client/game.py
mkdir -p backend/vn_server client/vn_client backend/static content/scenes tests docs .github/workflows
touch backend/vn_server/{__init__.py,models.py,db.py,seed.py,config.py}