from flask import Flask, render_template, request, redirect, flash
import os, re
app = Flask(__name__)
app.secret_key = os.urandom(32)
emailRegex = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z]+\.com')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result',methods=['POST'])
def postResult():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    passwrd = request.form['passwrd']
    confirmPass = request.form['confirmPass']
    error = False
    if len(firstName) < 1:
        flash('First Name may not be empty','firstError')
        error = True
    if len(lastName) < 1:
        flash("Last Name may not be empty",'lastError')
        error = True
    if len(passwrd) < 8:
        flash("Password must be AT LEAST 8 characters",'passShort')
        error = True
    if passwrd != confirmPass:
        flash("Password and Confirm Password must be the same",'passMatch')
        error = True
    if not emailRegex.match(email):
        flash("Invalid email address",'emailError')
        error = True
    if not error:
        flash("Thanks for submitting",'correct')
    return redirect('/')
app.run(debug=True)
