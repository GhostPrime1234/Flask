from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS: [str] = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("name") or not request.form.get("sport") in SPORTS:
            return render_template("failure.html")
        return render_template("success.html")
    else:
        if not request.args.get("name") or not request.args.get("sport") in SPORTS:
            return render_template("failure.html")
        return render_template("success.html")
