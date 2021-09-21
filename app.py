from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return render_template("base.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/handle_data', methods=["GET", "POST"])
def handle_data():
    # Testing get form data
    if request.method == "POST":
        # name = email in HTML form under login page
        email = request.form.get("email")
        # password
        password = request.form.get("password")
        return "Your email is "+email+" and your password is "+password
    return render_template("handle_data.html")


@app.route('/terms')
def terms():
    return render_template("terms.html")


@app.route('/about')
def about():
    return render_template("about.html")
# pass in page as var


# @app.route('/<name>/')
# def user(name):
#     return render_template("index.html", content=[name])


if __name__ == "__main__":
    app.run(debug=True)
