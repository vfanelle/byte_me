from google.appengine.ext import ndb
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2

#tells jinja2 where to look for future files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class clothing(ndb.Model):
    article = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    min_temp = ndb.StringProperty(required=True)
    max_temp = ndb.StringProperty(required=True)
    gender = ndb.StringProperty(required=True)
#add a couple of degrees to actual temp when deciding clothing for cold people

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('admin.html')
        self.response.write(template.render())
