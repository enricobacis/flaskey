from middleware.logger import LoggingMiddleware
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world!'

app.wsgi_app = LoggingMiddleware(app.wsgi_app)
