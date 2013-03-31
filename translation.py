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
    def __init__(self, src, dst, InString):
        self.srclan = src
        self.srcdst = dst
        self.InString = InString
        self.result = ''
        self.ExtractingState = 0
        HTMLParser.__init__(self)

    def translate(self):
        url = "http://translate.google.com.hk/translate_a/t?client=t&text=boy&hl=en&sl=en&tl=zh-CN&ie=UTF-8&oe=UTF-8&multires=1&otf=1&ssel=0&tsel=0&sc=1"
        url = "https://translate.google.com.hk/?hl=en&tab=wT#"+self.srclan+"/"+self.srcdst+"/"+self.InString
        #sock = urllib.urlopen(url)
        response = urlfetch.fetch(url,validate_certificate=False)
        if response.status_code == 200:
    	    htmlSource = response.content
            return htmlSource
            #self.feed(htmlSource)
            #self.close()
            #return self.result;
        
    def handle_starttag(self, tag, attrs):
        if tag == "span":
            attrVal = [ k for k, v in attrs if k == 'id' and v == 'result_box']
            if attrVal:
                self.ExtractingState = 1

    def handle_data(self, data):
        if self.ExtractingState == 1 or self.ExtractingState == 2:
            print data
            self.result += data;
            self.ExtractingState = 2

    def handle_endtag(self, tag):
        if self.ExtractingState == 2:
            if tag != "span":
                self.ExtractingState = 0

       
        
