from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=["post"])
def register():
    if not request.form.get("name") or not request.form.get("sport") in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")
