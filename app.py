from dotenv import load_dotenv

from src import app
from src import routes

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)