from flask import Flask, request

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


@app.route("/fortune", methods=["GET", "POST"])
def fortune():
    if request.method == "POST":
        name = request.form.get("user")
        color = request.form.get("color")
        number = request.form.get("number")

        fortunes = {
            ("red", "1"): "Today is the perfect day to take a leap of faith.",
            ("red", "2"): "A challenge will become your biggest opportunity.",
            ("red", "3"): "You’ll rediscover something valuable you thought was lost.",
            ("red", "4"): "Your passion will lead someone else to success.",
            ("yellow", "1"): "Happiness is closer than you think — embrace it.",
            ("yellow", "2"): "Someone will appreciate your sunny attitude today.",
            ("yellow", "3"): "A golden opportunity is waiting for you to notice it.",
            ("yellow", "4"): "Your optimism will light the way for others.",
            ("blue", "1"): "Peace and clarity will guide your next decision.",
            ("blue", "2"): "A calm mind opens doors to unexpected wisdom.",
            ("blue", "3"): "Embrace serenity — answers will come to you.",
            ("blue", "4"): "Your loyalty will be rewarded in the days ahead.",
            ("green", "1"): "Growth is happening even if you don’t see it yet.",
            ("green", "2"): "New paths will open when you trust your instincts.",
            ("green", "3"): "Nature has a message for you — go outside and listen.",
            ("green", "4"): "Your kindness will inspire someone quietly watching.",
        }

        fortune_text = fortunes.get((color, number))

        return f"""
        <h1>Fortune for {name}</h1>
        <p>You chose <strong>{color}</strong> and <strong>{number}</strong>.</p>
        <p><em>{fortune_text}</em></p>
        <a href="/fortune">Try again</a>
        """

    return """
    <h1>Welcome to the Fortune Teller!</h1>
    <form method="POST" action="/fortune">
        <label>Name:</label><br>
        <input type="text" name="user" required><br><br>

        <label>Pick a color:</label><br>
        <select name="color" required>
            <option value="red">Red</option>
            <option value="yellow">Yellow</option>
            <option value="blue">Blue</option>
            <option value="green">Green</option>
        </select><br><br>

        <label>Pick a number:</label><br>
        <select name="number" required>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
        </select><br><br>

        <button type="submit">Submit</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
