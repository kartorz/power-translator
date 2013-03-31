"""

"""
import urllib
import shutil

from HTMLParser import HTMLParser
from google.appengine.api import urlfetch


class TranslationGoogle(HTMLParser):
    """ Parsing the google translation websit, the folowing url can be use as the google translantion api.
    http://translate.google.com.hk/translate_a/t?client=t&text=boy&hl=en&sl=en&tl=zh-CN&ie=UTF-8&oe=UTF-8&multires=1&otf=1&ssel=0&tsel=0&sc=1
    """
    def __init__(self, src, dst, instring):
        self.srclan = src
        self.srcdst = dst
        self.instring = unicode(instring)
        HTMLParser.__init__(self)

    def translate(self):
        url = unicode("http://translate.google.com.hk/translate_a/t?client=t&text=u{0!s}&hl=en&sl={1!s}&tl={2!s}&ie=UTF-8&oe=UTF-8&multires=1&otf=1&ssel=0&tsel=0&sc=1")
        url = url.format(self.instring, self.srclan, self.srcdst)
        #sock = urllib.urlopen(url)
        response = urlfetch.fetch(url)
        if response.status_code == 200:
            htmlSource = response.content
            return htmlSource
