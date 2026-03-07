from sqlalchemy import text
from app import create_app
from app.models import db

app = create_app()

# Make sure the app config uses the Docker port
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/ggpa_db"

with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))
        print("Database is up!")
    except Exception as e:
        print("Database connection failed:", e)