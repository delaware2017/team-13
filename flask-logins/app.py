from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///users.db', echo=True)

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('application.html')

@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        return render_template('application.html', data = result)

    else:
        flash('wrong password!')

    return home()


@app.route('/save', methods = ['POST'])
def save_application():
    # print (request.form)
    # print (data['firstName'][0])
    username = str(request.form['username'])
    firstName = str(request.form['firstName'])
    lastName = str(request.form['lastName'])
    phoneNumber = str(request.form['phoneNumber'])
    email = str(request.form['email'])


    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.firstName.in_([firstName]))
    result = query.first()
    session['logged_in'] = False

    if result:
        result.firstName = firstName
        result.lastName = lastName
        result.phoneNumber = phoneNumber
        result.email = email
        s.commit()
        s.commit()


    else:
        flash('wrong password!')



    return render_template('login.html')







@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
