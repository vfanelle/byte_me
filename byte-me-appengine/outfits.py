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

#creates a clothing object
class Clothing(ndb.Model):
    article = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    temp = ndb.IntegerProperty(required=True)
    gender = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)


class AdminHandler(webapp2.RequestHandler):
    #takes user to admin page
    def get(self):
        #allows AdminHandler to display admin.html
        template = jinja_environment.get_template('admin.html')
        self.response.write(template.render())

    #collect user's input for a clothing object and creates one if the input is valid
    def post(self):
        article = self.request.get('kind')
        name = self.request.get('name')
        temp = self.request.get('temp')
        gender = self.request.get('gender')
        url = self.request.get('URL')
        if article != "" and name  != "" and gender != "" and url != "" and temp >-40:
          clothing = Clothing(article=article, name=name, temp=int(temp),
          gender=gender, url=url)
          key = clothing.put()
          my_ID = Clothing.get_by_id(key.id()).name
          template = jinja_environment.get_template('admin.html')
          self.response.write(template.render())
        else:
            print "User did not fill all entries on admin page."
            self.response.write("<div class= 'boxed'><h2><Please enter a valid city</h2></div>")
            template = jinja_environment.get_template('admin.html')
            self.response.write(template.render())
