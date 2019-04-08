#!/usr/bin/env python3
""" Replace URL domains in a text string"""

from bs4 import BeautifulSoup


def change_hrefs(html, from_url_fragment, to_url_fragment):
    soup = BeautifulSoup(html, features="lxml")
    for a in soup.findAll('a'):
        a['href'] = a['href'].replace(from_url_fragment, to_url_fragment)
    return soup


### The main program begins in the "if" statement below.

if __name__ == "__main__":
    x = '<p>Blah blah blah <a href="http://d101tm.com">Google</a></p>'
    y = "http://d101tm"
    z = "http://newurl"
    print('old_html=', x)
    new_html = change_hrefs(x, y, z)
    print('new_html=', new_html)
