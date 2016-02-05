import unittest
from ParseURL import ParseURL


class TestParsing(unittest.TestCase):

    def test_url1(self):
        url = 'https://www.google.com:80/login?username=johndoe&password=nanananabatman'
        parser = ParseURL(url)
        self.assertEqual("https", parser.parsed_url.get_attr('scheme'))
        self.assertEqual({'username': 'johndoe', 'password': 'nanananabatman'}, parser.parsed_url.get_attr('query'))
        self.assertEqual("/login", parser.parsed_url.get_attr('path'))
        self.assertEqual("", parser.parsed_url.get_attr('fragment'))
        self.assertEqual(80, parser.parsed_url.get_attr('port'))

    def test_url2(self):
        url = 'https://www.google.com:80/login#dashboard'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('fragment'), "dashboard")
        self.assertEqual(parser.parsed_url.get_attr('query'), {})

    def test_url3(self):
        url = 'https://www.quora.com/notifications'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('path'), "/notifications")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.quora.com")

    def test_url4(self):
        url = 'HTTP://www.Python.org/doc/#'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.Python.org")

    def test_url5(self):
        url = 'http://www.ics.uci.edu/pub/ietf/uri/#Related'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.ics.uci.edu")
        self.assertEqual(parser.parsed_url.get_attr('path'), "/pub/ietf/uri/")
        self.assertEqual(parser.parsed_url.get_attr('fragment'), "Related")

    def test_url6(self):
        url = 'http://username:password@www.my_site.com'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.my_site.com")
        self.assertEqual(parser.parsed_url.get_attr('username'), "username")
        self.assertEqual(parser.parsed_url.get_attr('password'), "password")

    def test_url7(self):
        url = 'https://github.com/jaideepcoder/ParseURL'
        parser = ParseURL(url)
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "github.com")
        self.assertEqual(parser.parsed_url.get_attr('path'), "/jaideepcoder/ParseURL")

    def test_unparse(self):
        url = 'https://github.com/jaideepcoder/ParseURL'
        parser = ParseURL(url)
        self.assertEqual(parser.url_unparse(), 'https://github.com/jaideepcoder/ParseURL')

    def test_addquery(self):
        url = 'https://github.com/jaideepcoder/ParseURL'
        parser = ParseURL(url)
        query = {'q': 'My+test+query'}
        parser.update_query(query)
        self.assertEqual({'q': 'My+test+query'}, parser.parsed_url.get_attr('query'))
        self.assertEqual('https://github.com/jaideepcoder/ParseURL?q=My+test+query', parser.url_unparse())

if "__name__" == "__main__":
    unittest.main()
