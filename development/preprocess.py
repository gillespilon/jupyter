#! /usr/bin/python

"""
A few convenient transformations for Pandoc HTML 5 output.
"""

import re
from xml.sax.saxutils import quoteattr

from bs4 import BeautifulSoup


_ELEMENT_OF_INTEREST = re.compile('^dt|h[1-6]$')


def xfrm_ids(name):
    """
    Coerce some text into something suitable for a fragment identifier.
    """
    return ''.join(filter(lambda c: c.isalnum() or c in '_-',
                          name.lower().translate({ord(c): '-'
                                                  for c in '\N{EM DASH}'
                                                           '\N{EN DASH}'
                                                           '\N{SPACE}'
                                                           '\N{LINE FEED}'})))


def autoid_elements(soup):
    """
    Add an id to all definition term and headers based on their contents.


    For example, there is no *nice* way to let Pandoc still parse markdown
    inside the following div:

        <div class="slide">
          <h1>Foo</h1>
          […]
        </div>
    """
    for element in soup.find_all(_ELEMENT_OF_INTEREST):
        if 'id' not in element.attrs:
            element.attrs['id'] = xfrm_ids(str(element.string))
    return soup


def figure_hyperlink(soup):
    """
    Make figures out of images in links.

    By default, pandoc transforms

        [![foo](bar)](baz)

        ![foo](bar)

    into (minus whitespace)

        <p><a href="baz"><img alt="bar" /></p>
        <figure>
          <img alt="foo" src="bar" />
          <figcaption>foo</figcaption>
        </figure>

    We want the first to also be a figure.
    """
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

    # Let BS4 deal with the BS of Windows encoding
    soup = BeautifulSoup(stdin.buffer, 'html5lib')

    # TODO: Replace with functools.reduce
    autoided = autoid_elements(soup)
    figured = figure_hyperlink(autoided)

    # hack to remove double/triple dashes from comments
    # .encode('utf-8')? We don't give BS output! Sigh. Windows!
    stdout.buffer.write(str(figured).replace('---', '&mdash;').encode('utf-8'))
