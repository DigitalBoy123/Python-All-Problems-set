'''Installed flask and wrote "hey flask!"'''
from flask import Flask
Application =Flask(__name__)
@Application.route('/')
def f():
    return "Welcome to the world of hackers"
Application.run()
 

