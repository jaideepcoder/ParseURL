from urllib.parse import urlparse
import timeit
from ParseURL import *


def native_urlparse(url):
    o = urlparse(url)
    # print(o)


def custom_urlparse(url):
    parser = ParseURL(url)
    parser.parse()
    # print(parser.parsed_url)

# Performance Benchmark
url = 'http://www.cwi.nl:80/%7Eguido/Python.html'
print(timeit.timeit('native_urlparse(url)', "from __main__ import native_urlparse, url"))
print(timeit.timeit('custom_urlparse(url)', "from __main__ import custom_urlparse, url"))