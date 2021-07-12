  
from flask import Flask, render_template, request, redirect, flash
from flask.globals import session
app = Flask(__name__)
app.secret_key = "surveystuff"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/userresults', methods=["POST"])
def showSurveyinfo():
    return render_template("results.html", name = request.form["name"], dojo = request.form["dojo_location"], favlang = request.form["favlang"], comments = request.form["comments"])

if __name__=="__main__":
    
    app.run(debug=True) 