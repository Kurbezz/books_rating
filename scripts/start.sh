cd /app

rm -rf prometheus
mkdir prometheus

alembic -c ./app/alembic.ini upgrade head
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8080
