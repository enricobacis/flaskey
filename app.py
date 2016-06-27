from middleware.headers import HeaderGetter
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world!'

app.wsgi_app = HeaderGetter(app.wsgi_app)
