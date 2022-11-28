from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("survey.html")

@app.route("/home")
def home():
    return render_template("survey.html")  

@app.route("/home1")
def home1():
    return render_template("tribute.html")  

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        information = request.form

    return render_template("submission.html", data=information)     

if __name__ == " __ main__  ":
    app.run(rebug=True)