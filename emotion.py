from flask import Flask, render_template, request, session, logging, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
import os
import secrets

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__,template_folder='template')
app.secret_key = 'super-secret-key'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = params['gmail_user']
app.config['MAIL_PASSWORD'] = params['gmail_password']
mail = Mail(app)


if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    cno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Register(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password =db.Column(db.String(20), nullable=False)
    password2 =db.Column(db.String(20), nullable=False)


class Details(db.Model):
    dno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phn = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    return render_template('index.html',  params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/dashboard")
def dashboard():
	if ('email' in session and session['email']):
            details = Details.query.filter_by().all()
            return render_template('dashboard.html', params=params, details=details)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        fname = request.form.get('fname')
        lname =request.form.get('lname')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Contact(fname=fname, lname=lname, message = message, email = email,date= datetime.now() )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from '+fname+" "+lname,
                          sender=email,
                          recipients=[params['gmail_user']],
                          body=message)
    return render_template('contact.html', params=params)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if(password==password2):
            entry=Register(name=name, email=email, password=password, password2=password2)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash("plz enter right password")
    return render_template('register.html', params=params)


@app.route("/details", methods=['GET', 'POST'])
def details():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        address =request.form.get('address')
        phn = request.form.get('phn')
        entry = Details(name=name, address=address, phn=phn, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('search'))
    return render_template('details.html', params=params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if ('email' in session and session['email']):
        return redirect('/dashboard')
        # return render_template('dashboard.html', params=params)

    if(request.method=="POST"):
        email = request.form["email"]
        password = request.form["password"]

        login = Register.query.filter_by(email=email, password=password).first()
        if login is not None:
            session['email'] = email
            return redirect('/dashboard')
            # return render_template("dashboard.html", params=params)
        else:
            flash("Please Enter Correct Password")
    return render_template('login.html', params=params)


@app.route('/search', methods=['GET','POST'])
def search():
    if ('email' in session and session['email']):
        details = Details.query.all()
        return render_template('search.html', params=params, details=details)

    if (request.method == "POST"):
        email = request.form["email"]
        password = request.form["password"]
        if (email==email and password==password):
            session['email']=email
            details = Details.query.all()
            return render_template('search.html', params=params, details=details)


@app.route("/find")
def find():
    if ('email' in session and session['email']):
        details = Details.query.filter_by().all()
        return render_template('find.html', params=params, details=details)

    if (request.method == "POST"):
        email = request.form["email"]
        password = request.form["password"]
        if (email==email and password==password):
            session['email']=email
            details = Details.query.all()
            return render_template('find.html', params=params, details=details)


@app.route('/patient/<string:pname>',methods=['GET','POST'])
def patient(pname):
    if ('email' in session and session['email']):
        details = Details.query.filter_by(name=pname).first()
        return render_template('patient.html', params=params, details=details)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('email')
    return redirect(url_for('login'))


@app.route('/main', methods=['GET', 'POST'])
def main():
    from capture import capture
    return render_template('main.html', params=params)


if __name__ == "__main__":
    
    app.run(debug=True)
