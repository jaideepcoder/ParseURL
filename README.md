[![Build Status](https://travis-ci.org/jaideepcoder/ParseURL.svg?branch=master)](https://travis-ci.org/jaideepcoder/ParseURL)

# ParseURL
This is a small project to emulate the existing urllib.urlparse() module.

## Usage

    parser = ParseURL('http://username:password@www.my_site.com')
    print parser.parsed_url
    >>>> ParseURL(scheme="http", netloc="www.my_site.com", path="", params="", query="{}",
    fragment="", username="username", password="password", hostname="my_site.com", port=)
