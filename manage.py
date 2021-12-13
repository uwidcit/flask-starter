import click
from flask import Flask
from .main import app
from .models import db, User

#create database command excute by running "flask init-db"
@app.cli.command('init-db')
def init_db():
    db.create_all(app=app)
    print('database initialized!')


@app.cli.command('insert-users')
def insert_users():
    bob = User('bob', 'bobpass')
    jane = User('jane', 'janepass')
    rick = User('rick', 'rickpass')
    db.session.add(bob)
    db.session.add(jane)
    db.session.add(rick)
    db.session.commit()
    print('users created!')

