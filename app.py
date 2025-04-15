from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>My Flask Application</h1><p>Welcome to my app!</p>"


@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>Hi, I'm Thomas Arnone. I'm learning Flask and building web apps using Python.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
