from project.config import config
from project.models import Genre, Director, Movie
from project.server import create_app, db

app = create_app(config)

"""У app при запуске есть много разных параметров, что сделать при запуске
Но это пока too much"""


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie
    }

if __name__ == "__main__":
    app.run()
