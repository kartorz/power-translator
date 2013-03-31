import webapp2

import homeview

class HomePage(webapp2.RequestHandler):
    def get(self):        
        self.response.headers['content-type'] = 'text/html'
        
        args = {}
        args['srclan'] = self.request.get('srclan')
        args['dstlan'] = self.request.get('dstlan')
        args['input'] = self.request.get('input')

        self.response.write(homeview.HomeView(args).GetHtml())

app = webapp2.WSGIApplication([('/',HomePage)],debug=True)

