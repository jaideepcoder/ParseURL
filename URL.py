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
        while Switch(key):
            if case('scheme'):
                self.scheme = value
                break
            if case('netloc'):
                self.netloc = value
                break
            if case('path'):
                self.path = value
                break
            if case('params'):
                self.params = value
                break
            if case('query'):
                self.query = value
                break
            if case('fragment'):
                self.fragment = value
                break
            if case('username'):
                self.username = value
                break
            if case('password'):
                self.password = value
                break
            if case('hostname'):
                self.hostname = value
                break
            if case('port'):
                self.port = value
                break

    def get_attr(self, key):
        while Switch(key):
            if case('scheme'):
                return self.scheme
            if case('netloc'):
                return self.netloc
            if case('path'):
                return self.path
            if case('params'):
                return self.params
            if case('query'):
                return self.query
            if case('fragment'):
                return self.fragment
            if case('username'):
                return self.username
            if case('password'):
                return self.password
            if case('hostname'):
                return self.hostname
            if case('port'):
                return self.port

    def __repr__(self):
        return 'ParseURL(scheme="{0}", netloc="{1}", path="{2}", params="{3}", query="{4}", fragment="{5}",' \
               ' username="{6}",password="{7}", hostname="{8}", port={9})'.format(self.scheme, self.netloc, self.path,
                                                                              self.params, self.query, self.fragment,
                                                                              self.username, self.password,
                                                                              self.hostname, self.port)
