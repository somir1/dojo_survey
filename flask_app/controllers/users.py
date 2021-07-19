from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.users import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usercreate', methods=["POST"])
def showSurveyinfo():
    print("sofar its working")
    if not User.validate_user(request.form):
        return redirect('/')

    survey = User.insert_user(request.form)    
    print("validation complete")

    return redirect(url_for(".save_user", survey = survey))

@app.route('/userresults')
def save_user():
    survey = request.args['survey']
    print(survey)
    print(request)
    user = User.get_all()
    return render_template("results.html", user = user)
