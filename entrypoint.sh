echo "Starting gunicorn"
gunicorn --bind 0.0.0.0:5000 --workers 2 --threads 2 app:app
