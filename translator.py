import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/plain'
        self.response.write('Hello, webapp2 world')

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
