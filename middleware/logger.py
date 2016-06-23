class LoggingMiddleware(object):
    """Simple logging middleware"""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('Yeah, I was reached!')
        return self.app(environ, start_response)

