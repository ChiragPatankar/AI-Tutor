from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form

        if User.query.filter_by(email=data['email']).first():
            flash('Email already registered')
            return redirect(url_for('auth.register'))

        user = User(email=data['email'], name=data['name'])
        user.set_password(data['password'])
        user.learning_level = data['level']
        user.subject = data['subject']

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('dashboard.home'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()

        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard.home'))

        flash('Invalid email or password')
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))