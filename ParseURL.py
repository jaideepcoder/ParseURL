from URL import *


class ParseURL(object):
    def __init__(self, url):
        self.url = url
        self.url_string = url
        self.parsed_url = URL()

    def parse_scheme(self, url):
        scheme = ""
        for char in url:
            if char == '.':
                scheme = ""
                break
            elif char == ':':
                break
            else: scheme = scheme + char
        # if url[0] == '/':
        #     scheme = 'http'
        if scheme != "":
            # Removing explicitly typed scheme from the URI to handle special schemes like URN
            self.url = url[len(scheme)+3:]
        return scheme.lower()

    def parse_netloc(self, url):
        self.url = ''
        return url

    def parse_path(self, url):
        ind = url.find('/')
        if ind != -1:
            self.url = url.replace(url[ind:], '')
            return url[ind:]
        return ''

    def parse_params(self, url):
        raise NotImplemented

    def parse_query(self, url):
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
        ind = url.find('#')
        if ind != -1:
            self.url = url[:ind]
            return url[ind+1:]
        return ''

    def parse_username(self, url):
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
        if 'www.' in url:
            # self.url = url.replace('www.', '')
            return self.url.replace('www.', '')

    def parse_port(self, url):
        port = ""
        if self.parsed_url.get_attr('scheme').lower() != 'urn':
            if ':' in url:
                for char in url[::-1]:
                    if char != ":":
                        if not char.isdigit():
                            break
                        port = char + port
                    else: break
                self.url = url.replace(':'+port, '')
                if port != '':
                    port = int(port)
        return port

    def parse(self):
        self.parsed_url.set_attr('scheme', self.parse_scheme(self.url))
        # self.parsed_url.set_attr('params', self.parse_params(self.url))
        self.parsed_url.set_attr('fragment', self.parse_fragment(self.url))
        self.parsed_url.set_attr('query', self.parse_query(self.url))
        self.parsed_url.set_attr('path', self.parse_path(self.url))
        self.parsed_url.set_attr('username', self.parse_username(self.url))
        self.parsed_url.set_attr('password', self.parse_password(self.url))
        self.parsed_url.set_attr('port', self.parse_port(self.url))
        self.parsed_url.set_attr('hostname', self.parse_hostname(self.url))
        self.parsed_url.set_attr('netloc', self.parse_netloc(self.url))
        print self.parsed_url
        # print self.url
        return

    def get_url(self):
        return self.url_string

    def url_join(self, url, str):
        raise NotImplemented

    def url_defrag(self):
        raise NotImplemented

    def url_unparse(self, parsed_url):
        url = ''
        if type(parsed_url) is URL:
            scheme = parsed_url.get_attr('scheme')
            if scheme != '':
                url = url + scheme + '://'
            username = parsed_url.get_attr('username')
            if username is not None:
                url = url + username
            password = parsed_url.get_attr('password')
            if password is not None:
                url = url + ':' + password + '@'
            netloc = parsed_url.get_attr('netloc')
            url = url + netloc
            port = parsed_url.get_attr('port')
            if port != '':
                url = url + ':' + port
            path = parsed_url.get_attr('path')
            if path != '':
                url = url + path
            query = self.query_unparse(parsed_url.get_attr('query'))
            if len(query) != 0:
                url = url + '?' + query
            fragment = parsed_url.get_attr('fragment')
            if fragment != '':
                url = url + '#' + fragment
            return url
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