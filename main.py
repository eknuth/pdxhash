#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, cgi
from google.appengine.ext.webapp import template
import Geohash, simplejson


class PDXHash(webapp.RequestHandler):
    def get(self):

        template_values = {
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        lat = cgi.escape(self.request.get('lat'))
        lon = cgi.escape(self.request.get('lon'))
        geohash = Geohash.encode(float(lat), float(lon))
        if geohash.startswith('c2'):
            pdxhash = {'pdxhash': geohash.replace('c2', '')}
        else:
            pdxhash = {'error': 'Not in Portland'}
        self.response.out.write(simplejson.dumps(pdxhash))
        
application = webapp.WSGIApplication(
                                     [('/', PDXHash),],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
