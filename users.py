from crypt import methods
from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    allusers = User.get_all_users()
    return render_template('index.html', users = allusers)

@app.route('/users', methods=['POST'])
def users():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/all')
def all():
    allusers = User.get_all_users()
    return render_template('/allusers.html', users=allusers)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    delete = User.delete(data)
    return redirect('/all')

@app.route('/update/', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/all')

@app.route('/user/edit/<int:id>')
def new(id):
    data={
        'id':id
    }
    return render_template('Edit_user.html', user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data={
        'id':id
    }
    return render_template('show_user.html', user=User.get_one(data))