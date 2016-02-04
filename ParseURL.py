from URL import *


class ParseURL(object):
    def __init__(self, url):
        self.url = url
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
            query = dict()
            for raw_query in url[start_ind+1:].split('&'):
                raw_query = raw_query.split('=')
                query[raw_query[0]] = raw_query[1]
            self.url = url.replace(url[start_ind:], '')
        else:
            query = dict()
            for raw_query in url[start_ind+1:end_ind].split('&'):
                raw_query = raw_query.split('=')
                query[raw_query[0]] = raw_query[1]
            self.url = url.replace(url[start_ind:end_ind], '')
        return query

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
