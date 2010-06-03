#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, cgi
from google.appengine.ext.webapp import template
import Geohash, simplejson
from geopy import geocoders 


api_key='ABQIAAAAkUlmIW1X-La8Y_JDbMsIaBQdkgRPlMVKT1vD1nTRJCRPuPWGKxT4RPVCd15nQW5msLk-f0ljd7C1Eg'


class PDXHash(webapp.RequestHandler):
    def get(self):
     
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):

        if cgi.escape(self.request.get('lat')) and cgi.escape(self.request.get('lat')):
            lat = cgi.escape(self.request.get('lat'))
            lon = cgi.escape(self.request.get('lon'))
        if self.request.get('address'):
            lat = 0
            lon = 0
            
        precision = cgi.escape(self.request.get('precision')) or 20

        geohash = Geohash.encode(float(lat), float(lon))
        if geohash.startswith('c2'):
            geohash = geohash.replace('c2', '')
            geohash = geohash[0:int(precision)]
            pdxhash = {'pdxhash': geohash}
        else:
            pdxhash = {'error': 'Not in Portland'}
        self.response.out.write(simplejson.dumps(pdxhash) + "\n")
        
application = webapp.WSGIApplication(
                                     [('/', PDXHash),],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
