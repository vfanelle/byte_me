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

class Clothing(ndb.Model):
    article = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    temp = ndb.IntegerProperty(required=True)
    gender = ndb.StringProperty(required=True)

    #url = ndb.StringProperty(required=True)
#add a couple of degrees to actual temp when deciding clothing for cold people

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        #allows AdminHandler to display admin.html
        template = jinja_environment.get_template('admin.html')
        self.response.write(template.render())

        article = self.request.get('kind')
        name = self.request.get('name')
        temp = self.request.get('temp')
        #max_temp = self.request.get('max_temp')
        gender = self.request.get('gender')
        #url = self.request.get('URL')

        clothing = Clothing(article=article, name=name, temp=int(temp),
        gender=gender)
        key = clothing.put()
        my_ID = Clothing.get_by_id(key.id()).name
