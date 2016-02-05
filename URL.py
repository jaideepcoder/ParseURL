from Helper import Switch, case


class URL(object):
    def __init__(self, scheme="", netloc="", path="", params="", query="",
                 fragment="", username="", password="", hostname="", port=""):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.params = params
        self.query = query
        self.fragment = fragment
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    def set_attr(self, key, value):
        if key == 'scheme':
            self.scheme = value
        elif key == 'netloc':
            self.netloc = value
        elif key == 'path':
            self.path = value
        elif key == 'params':
            self.params = value
        elif key == 'query':
            self.query = value
        elif key == 'fragment':
            self.fragment = value
        elif key == 'username':
            self.username = value
        elif key == 'password':
            self.password = value
        elif key == 'hostname':
            self.hostname = value
        elif key == 'port':
            self.port = value

    def get_attr(self, key):
        if key == 'scheme':
            return self.scheme
        if key == 'netloc':
            return self.netloc
        if key == 'path':
            return self.path
        if key == 'params':
            return self.params
        if key == 'query':
            return self.query
        if key == 'fragment':
            return self.fragment
        if key == 'username':
            return self.username
        if key == 'password':
            return self.password
        if key == 'hostname':
            return self.hostname
        if key == 'port':
            return self.port

    def __repr__(self):
        return 'ParseURL(scheme="{0}", netloc="{1}", path="{2}", params="{3}", query="{4}", fragment="{5}",' \
               ' username="{6}",password="{7}", hostname="{8}", port="{9}")'.format(self.scheme, self.netloc, self.path,
                                                                                  self.params, self.query, self.fragment,
                                                                                  self.username, self.password,
                                                                                  self.hostname, self.port)
