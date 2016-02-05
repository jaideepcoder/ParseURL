from URL import URL


class ParseURL(object):
    """A python module to parse url emulates urllib.urlparse()."""
    def __init__(self, url):
        self.url = url
        self.url_string = url
        self.parsed_url = URL()
        self.parse()

    def parse_scheme(self, url):
        """A method to parse the url scheme."""
        dot_ind = url.find('.')
        col_ind = url.find(':')
        scheme = ''
        if col_ind < dot_ind and col_ind != -1:
            scheme = url[:col_ind]
        self.url = url[col_ind+3:]
        return scheme.lower()

    def parse_netloc(self, url):
        """A method to parse the url netloc."""
        self.url = ''
        return url

    def parse_path(self, url):
        """A method to parse the url path."""
        ind = url.find('/')
        if ind != -1:
            self.url = url.replace(url[ind:], '')
            return url[ind:]
        return ''

    def parse_params(self, url):
        raise NotImplemented

    def parse_query(self, url):
        """A method to parse the url query."""
        start_ind = url.find('?')
        if start_ind == -1:
            return dict()
        end_ind = url.find('#')
        if end_ind == -1:
            query_string = url[start_ind+1:]
        else:
            query_string = url[start_ind+1:end_ind]
        self.url = url.replace('?' + query_string, '')
        return self.query_parse(query_string)

    def parse_fragment(self, url):
        """A method to parse the url fragment."""
        ind = url.find('#')
        if ind != -1:
            self.url = url[:ind]
            return url[ind+1:]
        return ''

    def parse_username(self, url):
        """A method to parse the url username."""
        if '@' in url: at_char = '@'
        elif '%40' in url: at_char = '%40'
        else: at_char = None
        if at_char == None:
            return
        url = url.split(at_char)
        url = url[0]
        if not ':' in url:
            return url
        else:
            url = url.split(':')
            return url[0]

    def parse_password(self, url):
        """A method to parse the url password."""
        if '@' in url: at_char = '@'
        elif '%40' in url: at_char = '%40'
        else: at_char = None
        if at_char == None:
            return
        url = url.split(at_char)
        url = url[0]
        self.url = self.url.replace(url+at_char, '')
        if not ':' in url:
            return url
        else:
            url = url.split(':')
            return url[1]

    def parse_hostname(self, url):
        """A method to parse the url hostname."""
        if 'www.' in url:
            # self.url = url.replace('www.', '')
            return self.url.replace('www.', '')

    def parse_port(self, url):
        """A method to parse the url port."""
        port = ""
        if self.parsed_url.get_attr('scheme').lower() != 'urn':
            if ':' in url:
                col_id = url.find(':')
                if url[-1].isdigit():
                    port = url[col_id+1:]
                self.url = url.replace(':'+port, '')
        if port == '':
            return port
        return int(port)

    def parse(self):
        """A method to parse the url. It is called from the class constructor."""
        url = self.url
        self.parsed_url.set_attr('scheme', self.parse_scheme(self.url))
        # self.parsed_url.set_attr('params', self.parse_params(self.url))
        self.parsed_url.set_attr('fragment', self.parse_fragment(self.url))
        self.parsed_url.set_attr('query', self.parse_query(self.url))
        self.parsed_url.set_attr('path', self.parse_path(self.url))
        self.parsed_url.set_attr('username', self.parse_username(self.url))
        self.parsed_url.set_attr('password', self.parse_password(self.url))
        self.parsed_url.set_attr('port', self.parse_port(self.url))
        # self.parsed_url.set_attr('hostname', self.parse_hostname(self.url))
        self.parsed_url.set_attr('netloc', self.parse_netloc(self.url))
        # print(self.parsed_url)
        # print self.url
        return

    def get_url(self):
        """Getter method to retrieve url string."""
        return self.url_string

    def url_join(self, url, str):
        raise NotImplemented

    def url_defrag(self):
        raise NotImplemented

    def url_unparse(self, parsed_url=None):
        """A method to reconstruct the url string from the parsed url."""
        if parsed_url is None: parsed_url = self.parsed_url
        url = list()
        if type(parsed_url) is URL:
            scheme = parsed_url.get_attr('scheme')
            if scheme != '':
                url.extend([scheme,'://'])
            username = parsed_url.get_attr('username')
            if username is not None:
                url.append(username)
            password = parsed_url.get_attr('password')
            if password is not None:
                url.extend([':', password, '@'])
            netloc = parsed_url.get_attr('netloc')
            url.append(netloc)
            port = parsed_url.get_attr('port')
            if port != '':
                url.extend([':', port])
            path = parsed_url.get_attr('path')
            if path != '':
                url.append(path)
            query = self.query_unparse(parsed_url.get_attr('query'))
            if len(query) != 0:
                url.extend(['?', query])
            fragment = parsed_url.get_attr('fragment')
            if fragment != '':
                url.extend(['#', fragment])
            return ''.join(url)
        elif type(parsed_url) is dict:
            if parsed_url['scheme'] != '':
                url = url + parsed_url['scheme'] + '://'
            if parsed_url['username'] is not None:
                url = url + parsed_url['username']
            if parsed_url['password'] is not None:
                url = url + ':' + parsed_url['password'] + '@'
            url = url + parsed_url['netloc']
            if parsed_url['port'] != '':
                url = url + ':' + parsed_url['port']
            if parsed_url['path'] != '':
                url = url + parsed_url['path']
            query = self.query_unparse(parsed_url['query'])
            if len(query) != 0:
                url = url + '?' + query
            if parsed_url['fragment'] != '':
                url = url + '#' + parsed_url['fragment']
            return url

    def query_unparse(self, query):
        output = ''
        for key in query:
            output = output + key + '=' + query[key] + '&'
        output = output[:-1]
        return output

    def query_parse(self, query_string):
        query = dict()
        for raw_query in query_string.split('&'):
            raw_query = raw_query.split('=')
            query[raw_query[0]] = raw_query[1]
        return query

    def update_query(self, query):
        """Method to update the query in the parsed url."""
        if type(query) == dict:
            self.parsed_url.set_attr('query', query)
        else:
            self.parsed_url.set_attr('query', self.query_parse(query))

# help(ParseURL)