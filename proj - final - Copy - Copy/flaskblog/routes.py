from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post, Patients, Staff, Medicine, Appointments
from flask_login import login_user, current_user, logout_user, login_required

import sqlite3
from sqlite3 import Error

posts = [
    {
        'author': '',
        'title': 'CLINIC MANAGEMENT SYSTEM',
        'content': '''GROUP MEMBERS
ITB414            PARVATHI NAIR
ITB417    JESSICA NETALKAR
ITB446         DEVESH TAJANE
ITB447     ABHISHEK THAKRE
''',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
    session['user_name'] = username.data

@app.route("/modules")
@login_required
def modules():
    return render_template('modules.html', title='Modules')

@app.route('/Patients', methods = ['GET', 'POST'])
@login_required
def Patients():
    
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('Patients.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM Patients ")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('Patients.db')
            cur = conn.cursor()
            cur.execute("Insert into Patients(pID,Fname,LName,PhoneNo,sex,Age) values (?,?,?,?,?,?)", (data.get('pID'),data.get('Fname'),data.get('Lname'),data.get('PhoneNo'),data.get('sex'),data.get('Age')))
            conn.commit()
            cur.execute("SELECT * FROM Patients")
            rows = cur.fetchall()
            
            return render_template('patients.html', data=rows)
            print(rows)
       except Error as e:
            print(e)
    return render_template('patients.html')
   
    

@app.route('/Medicines', methods = ['GET', 'POST'])
@login_required
def Medicines():
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('Medicines.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM Medicine")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('Medicines.db')
            cur = conn.cursor()
            cur.execute("Insert into Medicine(Mno,MName,MAvailability,MPrice,Manufacturing_Date,Expiry_Date) values (?,?,?,?,?,?)", (data.get('Mno'),data.get('MName'),data.get('MAvailability'),data.get('MPrice'),data.get('Manufacturing_Date'),data.get('Expiry_Date')))
            conn.commit()
            cur.execute("SELECT * FROM Medicine")
            rows = cur.fetchall()
            
            return render_template('medicine.html', data=rows)
            print(rows)
       except Error as e:
            print(e)
    return render_template('medicine.html')


@app.route('/Staff', methods = ['GET', 'POST'])
@login_required
def Staff():
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('Staff.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM Staff")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('Staff.db')
            cur = conn.cursor()
            cur.execute("Insert into Staff(sID,Firstname,LastName,Sex,Shift,Designation,WHours) values (?,?,?,?,?,?,?)", (data.get('sID'),data.get('FirstName'),data.get('LastName'),data.get('Sex'),data.get('Shift'),data.get('Designation'),data.get('WHours')))
            conn.commit()
            cur.execute("SELECT * FROM Staff")
            rows = cur.fetchall()
            
            return render_template('staff.html', data=rows)
            print(rows)
       except Error as e:
            print(e)      

    return render_template('staff.html')



@app.route('/Appointments', methods = ['GET', 'POST'])
@login_required
def Appointments():
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('Appointment.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM Appointments")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('Appointment.db')
            cur = conn.cursor()
            cur.execute("Insert into Appointments(AID,AName,AProblem,ATime,ADoctor) values (?,?,?,?,?)", (data.get('AID'),data.get('AName'),data.get('Problem'),data.get('ATime'),data.get('ADoctor')))
            conn.commit()
            cur.execute("SELECT * FROM Appointments")
            rows = cur.fetchall()
            
            return render_template('appointments.html', data=rows)
            print(rows)
       except Error as e:
            print(e)      

    return render_template('appointments.html')



@app.route("/Doctors")
@login_required
def Doctors():
    return render_template('doctors.html')