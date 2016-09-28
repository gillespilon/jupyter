#! /usr/bin/python

import re
from xml.sax.saxutils import quoteattr

from bs4 import BeautifulSoup


_ELEMENT_OF_INTEREST = re.compile('^dt|h[1-6]$')

def xfrm_ids(name):
    return ''.join(filter(lambda c: c.isalnum() or c in '_-',
                          name.lower().translate({ord(c): '-'
                                                  for c in '\N{EM DASH}'
                                                           '\N{EN DASH}'
                                                           '\N{SPACE}'
                                                           '\N{LINE FEED}'})))


def autoid_elements(soup):
    for element in soup.find_all(_ELEMENT_OF_INTEREST):
        if 'id' not in element.attrs:
            element.attrs['id'] = xfrm_ids(str(element.string))
    return soup


def figure_hyperlink(soup):
    # BeautifulSoup 4, as of this writing, doesn't support these
    # pseudo-classes.
    #for img in soup.select('p > a:only-child > img:only-child[alt]'):
    for img in soup.select('p > a > img[alt]'):
        # <p><a><img alt='not blank' /></a></p>
        a = img.parent
        p = a.parent
        if len(a.contents) != 1 or \
           len(p.contents) != 1:
            continue
        figure = soup.new_tag('figure')
        figcaption = soup.new_tag('figcaption')
        figcaption.append(img.attrs['alt'])
        a.append(figcaption)
        figure.append(a)
        p.replaceWith(figure)

    return soup


if __name__ == '__main__':
    from sys import stdin, stdout

    soup = BeautifulSoup(stdin, 'html5lib')

    # TODO: Replace with functools.reduce
    autoided = autoid_elements(soup)
    figured = figure_hyperlink(autoided)

    # hack to remove double/triple dashes from comments
    stdout.write(str(figured).replace('---', '&mdash;'))
