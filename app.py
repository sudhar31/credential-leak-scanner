from flask import Flask, render_template, request
from breach_checker import check_email_breach

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        email = request.form["email"]
        result = check_email_breach(email)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()