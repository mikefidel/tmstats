#!/usr/bin/env python3
""" Replace URL domains in a text string"""

from bs4 import BeautifulSoup


def change_hrefs(html_doc, old_href_fragment, new_href_fragment):
    html_doc = BeautifulSoup(html_doc, "html.parser")
    for a in html_doc.findAll('a'):
        a['href'] = a['href'].replace(old_href_fragment, new_href_fragment)
    return str(html_doc)


### The main program begins in the "if" statement below.

if __name__ == "__main__":
    # TODO BEGIN - tests function change_hrefs
    html_string = ('<html>'
                   '<head>'
                   '<title>Some HTML page</title>'
                   '<body>'
                   '<p>Blah blah blah <a href="https://d101tm.com">Google</a></p>'
                   '<p>Yada yada yada <a href="https://d101tm.com">Google</a></p>'
                   '</body>'
                   '</html>')

    from_fragment = "//d101tm"
    to_fragment = "//newurl"
    print('old_html=', html_string)
    new_html = change_hrefs(html_string, from_fragment, to_fragment)
    print('new_html=', new_html)
    # TODO END - tests function change_hrefs
