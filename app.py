from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return render_template("base.html")

# pass in page as var


@app.route('/<name>/')
def user(name):
    return render_template("index.html", content=[name])


if __name__ == "__main__":
    app.run(debug=True)
