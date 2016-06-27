from flask.wrappers import Request

class HeaderGetter(object):
    """Header Getter middleware"""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ, shallow=True)
        print req.headers.get('X-Auth-Token')
        return self.app(environ, start_response)
