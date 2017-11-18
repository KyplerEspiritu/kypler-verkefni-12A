from bottle import *

@route('/')
def app():
    return "<h1>Kypler er kominn á Heroku</h1>"