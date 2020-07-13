from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    first_name = "Sushiqueen"
    last_name = "Rainbowroll"
    animals = ["Giraffe", "Koala", "Elephant"]
    return render_template("index.html", first_name=first_name, last_name=last_name, animals=animals)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run()