import webapp2

import htmlsource

class HomePage(webapp2.RequestHandler):
    def get(self):
        
        self.response.headers['content-type'] = 'text/html'

        self.response.write(htmlsource.HtmlSourceEn.strHtmlHome)

app = webapp2.WSGIApplication([('/',HomePage)],debug=True)

