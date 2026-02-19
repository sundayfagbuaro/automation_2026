# Install Python Virtual Environment
    python3 -m venv .venv

# Activate the virtual environment
    source .venv/bin/activate

# Install python-dotenv. This library loads variables from a .env file into environment variables.
    pip install python-dotenv

# Create a .env file. Put this in your project root (same level as your main script).
    touch .env

        API_KEY=sk-123456789
        DB_PASSWORD=super_secret_password
        DEBUG=True

# Avoid committing .env file to git, so add it to .gitignore file
    .gitignore < .env

# Load .env in your Python script, At the top of your main file:
    from dotenv import load_dotenv
    import os

        load_dotenv()  # loads variables from .env into the environment

        api_key = os.getenv("API_KEY")
        db_password = os.getenv("DB_PASSWORD")
        debug = os.getenv("DEBUG")


