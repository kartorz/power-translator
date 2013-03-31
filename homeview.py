""" HTML source  class.

Note: General dynimical html source wirted back by Request Handler response.

Content: 
"""
import translation
import string

class HomeView():
    """ 
    """
    def __init__(self, args):
        self.srcLan = args['srclan']
        self.detLan = args['dstlan']
        self.input = args['input']

    def GetHtml(self):
        htmlSource = open("home.html").read()
        google = ""
        if self.srcLan and self.detLan and self.input:
            google = translation.TranslationGoogle(self.srcLan, self.detLan, self.input).translate()

        htmlSource = htmlSource.format(google)
        return htmlSource
        
