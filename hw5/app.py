from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Step 2: Define the database model
class VideoGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<VideoGame {self.title}>"


# Workaround for database setup on first request
@app.before_request
def create_tables():
    if not hasattr(app, "db_initialized"):
        db.create_all()
        if not VideoGame.query.first():
            games = [
                VideoGame(
                    title="The Legend of Zelda: Breath of the Wild",
                    genre="Adventure",
                    platform="Switch",
                ),
                VideoGame(title="Halo Infinite", genre="Shooter", platform="Xbox"),
                VideoGame(title="Stardew Valley", genre="Simulation", platform="PC"),
                VideoGame(title="God of War", genre="Action", platform="PlayStation"),
            ]
            db.session.bulk_save_objects(games)
            db.session.commit()
        app.db_initialized = True


@app.route("/")
def home():
    return "<h1>My Flask Application</h1><p>Welcome to my app!</p>"


@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>Hi, I'm Thomas Arnone. I'm learning Flask and building web apps using Python.</p>
    """


# Route to show all games
@app.route("/games")
def games():
    all_games = VideoGame.query.all()
    return render_template("index.html", games=all_games)


# Route to show a single game
@app.route("/game/<int:game_id>")
def game_detail(game_id):
    game = VideoGame.query.get_or_404(game_id)
    return render_template("detail.html", game=game)


if __name__ == "__main__":
    app.run(debug=True)
