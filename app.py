from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

'''
    Main python app that runs the flask server and loads html pages.
    All logic should be sent to other .py files for processing
'''

# Home page


@app.route('/')
def home():
    return render_template("testing_homepage.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/testing_homepage')
def homepage():
    return render_template("testing_homepage.html")

@app.route('/profile_setup')
def profile():
    return render_template("profile_setup.html")

@app.route('/testing_recipes')
def recipes():
    return render_template("testing_recipes.html")




@app.route('/handle_form', methods=["GET", "POST"])
def handle_form():
    # Testing get form data
    if request.method == "POST":
        # name = email in HTML form under login page
        username = request.form.get("username")
        # password
        password = request.form.get("password")
        return "Your name is " + username + " and your password is " + password

# For json data EXAMPLE


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return ''

# pass in page as var


# @app.route('/<name>/')
# def user(name):
#     return render_template("index.html", content=[name])


if __name__ == "__main__":
    app.run(debug=True)
